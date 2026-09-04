import { useEffect, useState } from "react";
import { Activity, Boxes, CreditCard, ShoppingCart, Table2, Users } from "lucide-react";
import { useOutletContext } from "react-router-dom";
import { Card, Badge, Skeleton } from "../components/ui";
import { services } from "../services/api";

const money = (value) =>
  new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
    maximumFractionDigits: 0,
  }).format(Number(value || 0));

export default function Dashboard() {
  const { refreshKey } = useOutletContext();
  const [data, setData] = useState({
    bills: [],
    payments: [],
    tables: [],
    inventory: [],
    customers: [],
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let active = true;

    async function load() {
      setLoading(true);

      const results = await Promise.allSettled([
        services.bills.list(),
        services.payments.list(),
        services.tables.list(),
        services.inventory.list(),
        services.customers.list(),
      ]);

      if (!active) return;

      setData({
        bills: results[0].status === "fulfilled" ? results[0].value.bills || [] : [],
        payments:
          results[1].status === "fulfilled"
            ? results[1].value.payments || []
            : [],
        tables:
          results[2].status === "fulfilled"
            ? results[2].value.restaurant_tables || []
            : [],
        inventory:
          results[3].status === "fulfilled"
            ? results[3].value.inventory_items || []
            : [],
        customers:
          results[4].status === "fulfilled"
            ? results[4].value.customers || []
            : [],
      });

      setLoading(false);
    }

    load();

    return () => {
      active = false;
    };
  }, [refreshKey]);

  const today = new Date().toISOString().slice(0, 10);
  const todayBills = data.bills.filter((bill) => bill.bill_date === today);
  const todayPayments = data.payments.filter((payment) => payment.payment_date === today);

  const sales = todayBills.reduce(
    (sum, bill) => sum + Number(bill.total_amount || 0),
    0,
  );

  const paid = todayPayments.reduce(
    (sum, payment) => sum + Number(payment.paid_amount || 0),
    0,
  );

  const lowStock = data.inventory.filter(
    (item) => Number(item.quantity || 0) <= Number(item.reorder_level || 0),
  );

  const occupied = data.tables.filter(
    (table) => String(table.status).toLowerCase() === "occupied",
  ).length;

  const stats = [
    ["Today's billed value", money(sales), ShoppingCart, "Sales flow"],
    ["Payments recorded", money(paid), CreditCard, "Collection"],
    ["Occupied tables", `${occupied}/${data.tables.length || 0}`, Table2, "Floor"],
    ["Low stock items", lowStock.length, Boxes, "Inventory"],
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-semibold text-white">Operational overview</h2>
        <p className="mt-1 text-sm text-slate-600">
          Live snapshot from the SaruPOS backend.
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
        {stats.map(([label, value, Icon, hint]) => (
          <Card key={label} className="p-5">
            {loading ? (
              <Skeleton className="h-20 w-full" />
            ) : (
              <>
                <div className="mb-4 flex items-center justify-between">
                  <div className="rounded-xl border border-[#252a35] bg-[#151923] p-2.5">
                    <Icon size={17} className="text-violet-300" />
                  </div>
                  <span className="text-[10px] text-slate-600">{hint}</span>
                </div>
                <div className="text-2xl font-semibold text-white">{value}</div>
                <div className="mt-1 text-xs text-slate-500">{label}</div>
              </>
            )}
          </Card>
        ))}
      </div>

      <div className="grid gap-5 xl:grid-cols-[1.2fr_0.8fr]">
        <Card className="overflow-hidden">
          <div className="flex items-center justify-between border-b border-[#252a35] px-5 py-4">
            <div>
              <h3 className="text-sm font-semibold text-white">Recent bills</h3>
              <p className="text-xs text-slate-600">Latest billing activity</p>
            </div>
            <Activity size={16} className="text-slate-600" />
          </div>

          <div className="divide-y divide-[#252a35]">
            {loading ? (
              [1, 2, 3, 4].map((item) => (
                <div key={item} className="px-5 py-4">
                  <Skeleton className="h-8 w-full" />
                </div>
              ))
            ) : data.bills.length ? (
              todayBills.slice(0, 6).map((bill) => (
                <div
                  key={bill.bill_id}
                  className="flex items-center justify-between px-5 py-4"
                >
                  <div>
                    <div className="text-sm font-medium text-slate-200">
                      {bill.invoice_number}
                    </div>
                    <div className="mt-1 text-[11px] text-slate-600">
                      {bill.bill_date} Â· {bill.customer_id}
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="text-sm font-semibold text-white">
                      {money(bill.total_amount)}
                    </div>
                    <div className="mt-1">
                      <Badge value={bill.status} />
                    </div>
                  </div>
                </div>
              ))
            ) : (
              <div className="p-8 text-center text-xs text-slate-600">
                No bills found.
              </div>
            )}
          </div>
        </Card>

        <Card>
          <div className="border-b border-[#252a35] px-5 py-4">
            <h3 className="text-sm font-semibold text-white">Attention</h3>
            <p className="text-xs text-slate-600">Operational items to review</p>
          </div>

          <div className="space-y-3 p-5">
            {lowStock.slice(0, 5).map((item) => (
              <div
                key={item.inventory_id}
                className="flex items-center justify-between rounded-xl border border-amber-500/10 bg-amber-500/[0.04] px-4 py-3"
              >
                <div>
                  <div className="text-sm text-slate-200">{item.item_name}</div>
                  <div className="mt-1 text-[11px] text-slate-600">
                    {item.quantity} {item.unit} Â· reorder at {item.reorder_level}
                  </div>
                </div>
                <Badge value="Low Stock" />
              </div>
            ))}

            {!lowStock.length && (
              <div className="rounded-xl border border-emerald-500/10 bg-emerald-500/[0.03] p-5 text-center text-xs text-emerald-300">
                Inventory is currently above reorder levels.
              </div>
            )}

            <div className="mt-4 flex items-center gap-3 rounded-xl border border-[#252a35] bg-[#151923] p-4">
              <Users size={17} className="text-slate-500" />
              <div>
                <div className="text-sm font-medium text-slate-200">
                  {data.customers.length}
                </div>
                <div className="text-[11px] text-slate-600">
                  customers in directory
                </div>
              </div>
            </div>
          </div>
        </Card>
      </div>
    </div>
  );
}
