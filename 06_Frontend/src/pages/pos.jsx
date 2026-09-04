import { useEffect, useMemo, useState } from "react";
import { Minus, Plus, Search, ShoppingCart, Trash2 } from "lucide-react";
import { Button, Card, Input, Select } from "../components/ui";
import { services } from "../services/api";
import { useAuth } from "../contexts/auth-context";

const money = (value) =>
  new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
  }).format(Number(value || 0));

export default function POS() {
  const { user } = useAuth();

  // Keep an unfinished POS order alive while the operator moves between pages.
  // It is cleared only after a successful payment or when "New Order" is chosen.
  const DRAFT_KEY = "sarupos_pos_draft";

  function loadDraft() {
    try {
      const raw = sessionStorage.getItem(DRAFT_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch {
      return null;
    }
  }

  const draft = loadDraft();

  const [menu, setMenu] = useState([]);
  const [customers, setCustomers] = useState([]);
  const [tables, setTables] = useState([]);
  const [query, setQuery] = useState("");
  const [cart, setCart] = useState(() => draft?.cart || []);
  const [customerId, setCustomerId] = useState(() => draft?.customerId || "");
  const [tableId, setTableId] = useState(() => draft?.tableId || "");
  const [paymentMethod, setPaymentMethod] = useState(() => draft?.paymentMethod || "Cash");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const [processing, setProcessing] = useState(false);
  const [completedBill, setCompletedBill] = useState(null);
  const [customerTable, setCustomerTable] = useState(() => draft?.customerTable || null);

  useEffect(() => {
    async function load() {
      const [menuResult, customerResult, tableResult] =
        await Promise.allSettled([
          services.menuItems.list(),
          services.customers.list(),
          services.tables.list(),
        ]);

      if (menuResult.status === "fulfilled") {
        setMenu(menuResult.value.menu_items || []);
      }

      if (customerResult.status === "fulfilled") {
        setCustomers(customerResult.value.customers || []);
      }

      if (tableResult.status === "fulfilled") {
        setTables(tableResult.value.restaurant_tables || []);
      }
    }

    load();
  }, []);

  useEffect(() => {
    const hasDraft = cart.length || customerId || tableId;
    if (!hasDraft) {
      sessionStorage.removeItem(DRAFT_KEY);
      return;
    }

    sessionStorage.setItem(
      DRAFT_KEY,
      JSON.stringify({
        cart,
        customerId,
        tableId,
        paymentMethod,
        customerTable,
      }),
    );
  }, [cart, customerId, tableId, paymentMethod, customerTable]);

  const visibleMenu = menu.filter((item) => {
    const available = String(item.availability || "").toLowerCase() === "available";

    return (
      available &&
      `${item.item_name} ${item.category_id}`
        .toLowerCase()
        .includes(query.toLowerCase())
    );
  });

  function addItem(item) {
    setCart((current) => {
      const existing = current.find(
        (line) => line.menu_item_id === item.menu_item_id,
      );

      if (existing) {
        return current.map((line) =>
          line.menu_item_id === item.menu_item_id
            ? { ...line, quantity: line.quantity + 1 }
            : line,
        );
      }

      return [
        ...current,
        {
          menu_item_id: item.menu_item_id,
          item_name: item.item_name,
          price: Number(item.price || 0),
          quantity: 1,
        },
      ];
    });
  }

  function changeQty(id, amount) {
    setCart((current) =>
      current
        .map((line) =>
          line.menu_item_id === id
            ? { ...line, quantity: Math.max(0, line.quantity + amount) }
            : line,
        )
        .filter((line) => line.quantity > 0),
    );
  }

  const subtotal = useMemo(
    () =>
      cart.reduce(
        (sum, line) => sum + line.price * Number(line.quantity || 0),
        0,
      ),
    [cart],
  );

 async function handleCustomerChange(nextCustomerId) {
    setCustomerId(nextCustomerId);
    setTableId("");
    setCustomerTable(null);
    setError("");
    if (!nextCustomerId) return;
    try {
      const result = await services.diningSessions.activeByCustomer(nextCustomerId);
      const session = result.dining_session;
      setCustomerTable(session);
      setTableId(session.table_id);
    } catch (err) {
      if (err.status !== 404) setError(err.message);
    }
  }

async function checkout() {
  setError("");
  setMessage("");

  if (!cart.length) {
    setError("Add at least one menu item.");
    return;
  }

  if (!customerId || !tableId) {
    setError("Customer and table selection are required for billing.");
    return;
  }

  if (!user?.employee_id) {
    setError("Logged-in employee information is missing.");
    return;
  }

  setProcessing(true);

  try {
    const invoiceNumber = `INV-${new Date().getFullYear()}-${Date.now()}`;
    const billDate = new Date().toISOString().slice(0, 10);
    const result = await services.checkout({
      customer_id: customerId,
      table_id: tableId,
      invoice_number: invoiceNumber,
      bill_date: billDate,
      payment_method: paymentMethod,
      items: cart.map((line) => ({
        menu_item_id: line.menu_item_id,
        quantity: Number(line.quantity),
      })),
    });

    const bill = result.bill;

    // The draft is no longer needed once payment succeeds.
    sessionStorage.removeItem(DRAFT_KEY);

    setCompletedBill({
      billId: bill.bill_id,
      invoiceNumber: bill.invoice_number,
      billDate: bill.bill_date,
      total: bill.total_amount,
      subtotal: bill.subtotal,
      taxAmount: bill.tax_amount,
      paymentMethod: bill.payment_method,
      customerId: bill.customer_id,
      tableId: bill.table_id,
      items: bill.items,
    });
    setMessage(`Bill ${bill.invoice_number} created successfully. Payment received: ${money(bill.total_amount)}`);
  } catch (err) {
    setError(err.message || "Checkout failed.");
  } finally {
    setProcessing(false);
  }
}


function printReceipt(bill) {
  const receipt = window.open("", "sarupos-receipt", "width=420,height=700");
  if (!receipt) return;

  const items = (bill.items || [])
    .map((item) => `<tr><td>${item.item_name}</td><td>${item.quantity}</td><td>${money(item.subtotal)}</td></tr>`)
    .join("");

  receipt.document.write(`<!doctype html><html><head><title>${bill.invoiceNumber}</title><style>body{font-family:Arial,sans-serif;padding:24px;color:#111}h1{font-size:20px;margin:0 0 4px}p{margin:4px 0;font-size:12px;color:#555}table{width:100%;border-collapse:collapse;margin-top:18px;font-size:12px}th,td{padding:7px 0;border-bottom:1px solid #ddd;text-align:left}th:last-child,td:last-child{text-align:right}.total{margin-top:16px;text-align:right;font-size:18px;font-weight:700}</style></head><body><h1>SARUPOS</h1><p>Invoice: ${bill.invoiceNumber}</p><p>Date: ${bill.billDate}</p><table><thead><tr><th>Item</th><th>Qty</th><th>Amount</th></tr></thead><tbody>${items}</tbody></table><p style="margin-top:14px">Subtotal: ${money(bill.subtotal)}</p><p>Tax: ${money(bill.taxAmount)}</p><div class="total">Total: ${money(bill.total)}</div><p>Payment: ${bill.paymentMethod}</p></body></html>`);
  receipt.document.close();
  receipt.focus();
  receipt.print();
}

function startNewOrder() {
  sessionStorage.removeItem(DRAFT_KEY);
  setCompletedBill(null);
  setMessage("");
  setError("");
  setCart([]);
  setCustomerId("");
  setTableId("");
  setCustomerTable(null);
  setPaymentMethod("Cash");
}

  return (
    <div className="grid gap-5 xl:grid-cols-[1fr_390px]">
      <section className="space-y-4">
        <div className="flex flex-col gap-3 md:flex-row">
          <div className="relative flex-1">
            <Search
              size={16}
              className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-600"
            />
            <input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search menu items..."
              className="w-full rounded-xl border border-[#252a35] bg-[#10131a] py-3 pl-9 pr-3 text-sm text-slate-200 outline-none focus:border-violet-500/60"
            />
          </div>
        </div>

        <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
          {visibleMenu.map((item) => (
            <button
              key={item.menu_item_id}
              onClick={() => addItem(item)}
              className="group rounded-2xl border border-[#252a35] bg-[#10131a] p-4 text-left transition hover:border-violet-500/30 hover:bg-[#151923]"
            >
              <div className="mb-3 flex items-start justify-between gap-3">
                <div className="rounded-xl bg-violet-500/10 p-2.5 text-violet-300">
                  <ShoppingCart size={16} />
                </div>
                <span className="text-sm font-semibold text-white">
                  {money(item.price)}
                </span>
              </div>

              <div className="text-sm font-medium text-slate-200">
                {item.item_name}
              </div>
              <div className="mt-1 text-[11px] text-slate-600">
                {item.category_id}
              </div>

              <div className="mt-4 flex items-center gap-1.5 text-[10px] font-medium text-emerald-400">
                <span className="h-1.5 w-1.5 rounded-full bg-emerald-400" />
                Available
              </div>
            </button>
          ))}
        </div>
      </section>

      <Card className="h-fit xl:sticky xl:top-6">
        <div className="flex items-center justify-between border-b border-[#252a35] px-5 py-4">
          <div>
            <h2 className="text-sm font-semibold text-white">Current order</h2>
            <p className="text-xs text-slate-600">{cart.length} line items</p>
          </div>
          <ShoppingCart size={17} className="text-violet-300" />
        </div>

        <div className="space-y-3 p-5">
          {!cart.length ? (
            <div className="rounded-xl border border-dashed border-[#252a35] p-8 text-center text-xs text-slate-600">
              Tap menu items to start an order.
            </div>
          ) : (
            cart.map((line) => (
              <div
                key={line.menu_item_id}
                className="rounded-xl border border-[#252a35] bg-[#151923] p-3"
              >
                <div className="flex items-start justify-between gap-3">
                  <div className="min-w-0">
                    <div className="truncate text-sm font-medium text-slate-200">
                      {line.item_name}
                    </div>
                    <div className="mt-1 text-xs text-slate-600">
                      {money(line.price)}
                    </div>
                  </div>

                  <button
                    onClick={() => changeQty(line.menu_item_id, -line.quantity)}
                    className="text-slate-600 hover:text-red-300"
                  >
                    <Trash2 size={14} />
                  </button>
                </div>

                <div className="mt-3 flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => changeQty(line.menu_item_id, -1)}
                      className="rounded-lg border border-[#252a35] p-1.5 text-slate-500"
                    >
                      <Minus size={13} />
                    </button>
                    <span className="w-6 text-center text-xs text-slate-200">
                      {line.quantity}
                    </span>
                    <button
                      onClick={() => changeQty(line.menu_item_id, 1)}
                      className="rounded-lg border border-[#252a35] p-1.5 text-slate-500"
                    >
                      <Plus size={13} />
                    </button>
                  </div>

                  <div className="text-sm font-semibold text-white">
                    {money(line.price * line.quantity)}
                  </div>
                </div>
              </div>
            ))
          )}

                    <div className="space-y-3 border-t border-[#252a35] pt-4">
            <Select
              label="Customer"
              value={customerId}
              onChange={(e) => handleCustomerChange(e.target.value)}
              options={[
                { value: "", label: "Select customer" },
                ...customers.map((customer) => ({
                  value: customer.customer_id,
                  label: `${customer.customer_name} Â· ${customer.phone || "No phone"}`,
                })),
              ]}
            />

            <Select
              label="Table"
              value={tableId}
              onChange={(e) => setTableId(e.target.value)}
              disabled={Boolean(customerTable)}
              options={[
                { value: "", label: "Select table" },
                ...(customerTable
                  ? tables
                      .filter((table) => table.table_id === customerTable.table_id)
                      .map((table) => ({
                        value: table.table_id,
                        label: `${table.table_number} · ${table.capacity} seats · Occupied for this customer`,
                      }))
                  : tables
                      .filter((table) => String(table.status).toLowerCase() === "available")
                      .map((table) => ({
                        value: table.table_id,
                        label: `${table.table_number} · ${table.capacity} seats · Available`,
                      })))
              ]}
            />

            <Select
              label="Payment method"
              value={paymentMethod}
              onChange={(e) => setPaymentMethod(e.target.value)}
              options={[
                { value: "Cash", label: "Cash" },
                { value: "UPI", label: "UPI" },
                { value: "Card", label: "Card" },
              ]}
            />
          </div>

          <div className="flex items-center justify-between pt-2">
            <span className="text-sm text-slate-500">Total</span>
            <span className="text-2xl font-semibold text-white">
              {money(subtotal)}
            </span>
          </div>

          {error && (
            <div className="rounded-xl border border-red-500/20 bg-red-500/10 px-3 py-2.5 text-xs text-red-300">
              {error}
            </div>
          )}

          {message && (
            <div className="rounded-xl border border-emerald-500/20 bg-emerald-500/10 px-3 py-2.5 text-xs text-emerald-300">
              {message}
            </div>
          )}

          {completedBill ? (
  <div className="space-y-3">
    <div className="rounded-xl border border-emerald-500/20 bg-emerald-500/10 px-3 py-3">
      <div className="text-sm font-semibold text-emerald-300">
        Payment Completed
      </div>

      <div className="mt-1 text-xs text-slate-300">
        Invoice: {completedBill.invoiceNumber}
      </div>

      <div className="mt-3 space-y-1 text-xs text-slate-400">
        <div className="flex justify-between"><span>Subtotal</span><span>{money(completedBill.subtotal)}</span></div>
        <div className="flex justify-between"><span>Tax</span><span>{money(completedBill.taxAmount)}</span></div>
        <div className="flex justify-between pt-1 text-sm text-white"><span>Total paid</span><span className="font-semibold">{money(completedBill.total)}</span></div>
      </div>

      <div className="mt-1 text-xs text-slate-400">
        {completedBill.paymentMethod} Â· {completedBill.billDate}
      </div>
    </div>

    <div className="grid grid-cols-2 gap-2">
      <Button
        variant="secondary"
        className="w-full"
        onClick={() => printReceipt(completedBill)}
      >
        Print receipt
      </Button>
      <Button className="w-full" onClick={startNewOrder}>
        New Order
      </Button>
    </div>
  </div>
) : (
  <Button
    className="w-full"
    loading={processing}
    onClick={checkout}
    disabled={!cart.length}
  >
    Complete payment Â· {money(subtotal)}
  </Button>
)}
        </div>
      </Card>
    </div>
  );
}
