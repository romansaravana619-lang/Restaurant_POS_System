import { useEffect, useMemo, useState } from "react";
import { Pencil, Plus, Trash2 } from "lucide-react";
import { Button, Card, EmptyState, Input, Modal, SearchBox, Select, Badge, Textarea } from "../components/ui";
import { services } from "../services/api";

const configs = {
  bills: {
    title: "Bills",
    subtitle: "Billing history and completed invoices",
    service: services.bills,
    collection: "bills",
    id: "bill_id",
    readOnly: true,
    fields: [
      ["bill_id", "Bill ID", "text", true],
      ["customer_id", "Customer ID", "text", true],
      ["employee_id", "Employee ID", "text", true],
      ["table_id", "Table ID", "text", true],
      ["invoice_number", "Invoice Number", "text", true],
      ["bill_date", "Bill Date", "date", true],
      ["total_amount", "Total Amount", "number", true],
      ["status", "Status", "status", true],
    ],
    columns: ["invoice_number", "bill_date", "customer_id", "table_id", "total_amount", "status"],
  },

  categories: {
    title: "Categories",
    subtitle: "Manage menu classification",
    service: services.categories,
    collection: "categories",
    id: "category_id",
    fields: [
      ["category_id", "Category ID", "text", true],
      ["category_name", "Category Name", "text", true],
      ["description", "Description", "textarea", false],
      ["status", "Status", "status", true],
    ],
    columns: ["category_id", "category_name", "description", "status"],
  },

  menu: {
    title: "Menu",
    subtitle: "Manage dishes and availability",
    service: services.menuItems,
    collection: "menu_items",
    id: "menu_item_id",
    fields: [
      ["menu_item_id", "Menu Item ID", "text", true],
      ["category_id", "Category ID", "text", true],
      ["item_name", "Item Name", "text", true],
      ["price", "Price", "number", true],
      ["description", "Description", "textarea", false],
      ["availability", "Availability", "availability", true],
    ],
    columns: ["menu_item_id", "category_id", "item_name", "price", "availability"],
  },

  inventory: {
    title: "Inventory",
    subtitle: "Monitor stock and reorder levels",
    service: services.inventory,
    collection: "inventory_items",
    id: "inventory_id",
    fields: [
      ["inventory_id", "Inventory ID", "text", true],
      ["supplier_id", "Supplier ID", "text", true],
      ["item_name", "Item Name", "text", true],
      ["unit", "Unit", "text", true],
      ["quantity", "Quantity", "number", true],
      ["unit_cost", "Unit Cost", "number", true],
      ["reorder_level", "Reorder Level", "number", true],
      ["status", "Status", "status", true],
    ],
    columns: [
      "inventory_id",
      "supplier_id",
      "item_name",
      "unit",
      "quantity",
      "unit_cost",
      "reorder_level",
      "status",
    ],
  },

  suppliers: {
    title: "Suppliers",
    subtitle: "Manage supplier relationships",
    service: services.suppliers,
    collection: "suppliers",
    id: "supplier_id",
    fields: [
      ["supplier_id", "Supplier ID", "text", true],
      ["supplier_name", "Supplier Name", "text", true],
      ["contact_person", "Contact Person", "text", false],
      ["phone", "Phone", "text", false],
      ["email", "Email", "email", false],
      ["address", "Address", "textarea", false],
      ["status", "Status", "status", true],
    ],
    columns: [
      "supplier_id",
      "supplier_name",
      "contact_person",
      "phone",
      "email",
      "status",
    ],
  },

  customers: {
    title: "Customers",
    subtitle: "Fast customer lookup for billing",
    service: services.customers,
    collection: "customers",
    id: "customer_id",
    fields: [
     
      ["customer_name", "Customer Name", "text", true],
      ["phone", "Phone", "text", false],
      ["email", "Email", "email", false],
      ["status", "Status", "status", true],
      ["table_id", "Table", "table", true],
    ],
    columns: ["customer_id", "customer_name", "phone", "email", "active_table_number", "status"],
  },

  payments: {
    title: "Payments",
    subtitle: "Payment records and status",
    service: services.payments,
    collection: "payments",
    id: "payment_id",
    readOnly: true,
    fields: [
      ["payment_id", "Payment ID", "text", true],
      ["bill_id", "Bill ID", "text", true],
      ["payment_method", "Payment Method", "payment", true],
      ["payment_status", "Payment Status", "status", true],
      ["payment_date", "Payment Date", "date", true],
      ["paid_amount", "Paid Amount", "number", true],
    ],
    columns: [
      "payment_id",
      "bill_id",
      "payment_method",
      "payment_status",
      "payment_date",
      "paid_amount",
    ],
  },

  employees: {
    title: "Employees",
    subtitle: "Staff and workforce management",
    service: services.employees,
    collection: "employees",
    id: "employee_id",
    fields: [
      ["employee_id", "Employee ID", "text", true],
      ["full_name", "Full Name", "text", true],
      ["phone", "Phone", "text", false],
      ["email", "Email", "email", false],
      ["designation", "Designation", "text", false],
      ["address", "Address", "textarea", false],
      ["role", "Role", "role", true],
      ["hire_date", "Hire Date", "date", false],
      ["salary", "Salary", "number", false],
      ["status", "Status", "status", true],
    ],
    columns: [
      "employee_id",
      "full_name",
      "designation",
      "phone",
      "role",
      "salary",
      "status",
    ],
  },

  users: {
    title: "Users",
    subtitle: "Manage secure login accounts",
    service: services.users,
    collection: "users",
    id: "user_id",
    fields: [
      ["user_id", "User ID", "text", true],
      ["employee_id", "Employee ID", "text", true],
      ["username", "Username", "text", true],
      ["password", "Password", "password", false],
      ["role", "Role", "role", true],
      ["status", "Status", "status", true],
    ],
    columns: ["user_id", "employee_id", "username", "role", "status"],
  },
};

function emptyValue(type) {
  if (type === "status") return "Active";
  if (type === "availability") return "Available";
  if (type === "payment") return "Cash";
  if (type === "role") return "Staff";
  return "";
}

function displayValue(value, key) {
  if (["price", "unit_cost", "unit_price", "paid_amount", "salary"].includes(key)) {
    return Number(value || 0).toLocaleString("en-IN", {
      style: "currency",
      currency: "INR",
      maximumFractionDigits: 2,
    });
  }

  if (["status", "availability", "payment_status"].includes(key)) {
    return <Badge value={value} />;
  }

  return String(value ?? "â€”");
}

export default function ResourcePage({ resource }) {
  const config = configs[resource];
  const [rows, setRows] = useState([]);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(true);
  const [modalOpen, setModalOpen] = useState(false);
  const [editing, setEditing] = useState(null);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  const [tables, setTables] = useState([]);

  const emptyForm = useMemo(
    () =>
      Object.fromEntries(
        config.fields.map(([key, , type]) => [
          key,
          key === config.id ? "" : emptyValue(type),
        ]),
      ),
    [config],
  );

  const [form, setForm] = useState(emptyForm);

  async function load() {
    setLoading(true);
    setError("");

    try {
      const result = await config.service.list();
      setRows(result[config.collection] || []);
      if (resource === "customers") {
        try {
          const tableResult = await services.tables.list();
            setTables(
               Array.isArray(tableResult.restaurant_tables)
              ? tableResult.restaurant_tables
          : []
    );
        } catch {
          setTables([]);
        }
      }
    } catch (err) {
      if (err.status === 404) {
        setRows([]);
      } else {
        setError(err.message);
      }
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    setForm(emptyForm);
    if (resource !== "customers") setTables([]);
    load();
  }, [resource]);

  const filtered = rows.filter((row) =>
    Object.values(row)
      .join(" ")
      .toLowerCase()
      .includes(query.toLowerCase()),
  );

  async function startCreate() {
  setEditing(null);
  setForm(emptyForm);
  setError("");

  if (resource === "customers") {
    try {
      const tableResult = await services.tables.list();

      const availableTables = Array.isArray(tableResult.restaurant_tables)
        ? tableResult.restaurant_tables
        : [];

      setTables(availableTables);
    } catch (err) {
      setTables([]);
      setError(`Unable to load tables: ${err.message}`);
    }
  }

  setModalOpen(true);
}

  function startEdit(row) {
    const next = { ...emptyForm };

    config.fields.forEach(([key]) => {
      next[key] = row[key] ?? "";
    });

    setEditing(row);
    setForm(next);
    setError("");
    setModalOpen(true);
  }

  async function handleSave(event) {
    event.preventDefault();
    setSaving(true);
    setError("");

    try {
      const body = { ...form };

      config.fields.forEach(([key, , type]) => {
        if (type === "number" && body[key] !== "") {
          body[key] = Number(body[key]);
        }
      });

      if (editing) {
        delete body[config.id];
        if (config.id === "customer_id") {
          delete body.table_id;
        }

        if (config.id === "user_id" && !body.password) {
          delete body.password;
        }

        await config.service.update(editing[config.id], body);
      } else {
        if (config.id === "user_id" && !body.password) {
          throw new Error("Password is required when creating a user.");
        }

        await config.service.create(body);
      }

      setModalOpen(false);
      await load();
    } catch (err) {
      setError(err.message);
    } finally {
      setSaving(false);
    }
  }

  async function handleDelete(row) {
    if (!window.confirm(`Delete ${row[config.id]}?`)) return;

    try {
      await config.service.remove(row[config.id]);
      await load();
    } catch (err) {
      setError(err.message);
    }
  }

  const canCreate = !config.readOnly;
  const canDelete = !config.readOnly && !["employees", "users"].includes(resource) || resource === "employees" || resource === "users";

  return (
    <div className="space-y-5">
      <div className="flex flex-col justify-between gap-4 md:flex-row md:items-end">
        <div>
          <h2 className="text-xl font-semibold text-white">{config.title}</h2>
          <p className="mt-1 text-sm text-slate-600">{config.subtitle}</p>
        </div>

        <div className="flex gap-2">
          <div className="w-60">
            <SearchBox value={query} onChange={setQuery} />
          </div>

          {canCreate && (
            <Button onClick={startCreate}>
              <Plus size={15} />
              Add
            </Button>
          )}
        </div>
      </div>

      {error && (
        <div className="rounded-xl border border-red-500/20 bg-red-500/10 px-4 py-3 text-xs text-red-300">
          {error}
        </div>
      )}

      <Card className="overflow-hidden">
        {loading ? (
          <div className="p-6 text-sm text-slate-600">Loading records...</div>
        ) : !filtered.length ? (
          <EmptyState
            title={`No ${config.title.toLowerCase()} found`}
            text={query ? "Try another search." : "Create your first record to get started."}
          />
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full min-w-[780px] text-left">
              <thead className="border-b border-[#252a35] bg-[#151923]/70">
                <tr>
                  {config.columns.map((column) => (
                    <th
                      key={column}
                      className="px-4 py-3 text-[10px] font-semibold uppercase tracking-[0.12em] text-slate-600"
                    >
                      {column.replaceAll("_", " ")}
                    </th>
                  ))}
                  <th className="px-4 py-3 text-right text-[10px] font-semibold uppercase tracking-[0.12em] text-slate-600">
                    Actions
                  </th>
                </tr>
              </thead>

              <tbody className="divide-y divide-[#252a35]">
                {filtered.map((row) => (
                  <tr key={row[config.id]} className="hover:bg-white/[0.018]">
                    {config.columns.map((column) => (
                      <td
                        key={column}
                        className="px-4 py-3 text-xs text-slate-300"
                      >
                        {displayValue(row[column], column)}
                      </td>
                    ))}

                    <td className="px-4 py-3">
                      <div className="flex justify-end gap-1">
                        {!config.readOnly && (
                          <button
                            onClick={() => startEdit(row)}
                            className="rounded-lg p-2 text-slate-600 hover:bg-white/[0.04] hover:text-slate-200"
                          >
                            <Pencil size={14} />
                          </button>
                        )}

                        {canDelete && (
                          <button
                            onClick={() => handleDelete(row)}
                            className="rounded-lg p-2 text-slate-600 hover:bg-red-500/10 hover:text-red-300"
                          >
                            <Trash2 size={14} />
                          </button>
                        )}
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </Card>

      <Modal
        open={modalOpen}
        onClose={() => setModalOpen(false)}
        title={editing ? `Edit ${config.title}` : `Add ${config.title}`}
        wide
      >
        <form onSubmit={handleSave} className="space-y-4">
          <div className="grid gap-4 sm:grid-cols-2">
            {config.fields.map(([key, label, type, required]) => {
              if (type === "table") {
                const availableTables = tables.filter(
                  (table) => String(table.status).toLowerCase() === "available"
                );
                return (
                  <Select
                    key={key}
                    label="Table"
                    value={form[key]}
                    onChange={(e) =>
                      setForm((prev) => ({ ...prev, [key]: e.target.value }))
                    }
                    options={[
                      { value: "", label: "Select available table" },
                      ...availableTables.map((table) => ({
                        value: table.table_id,
                        label: `${table.table_number} · ${table.capacity} seats · Available`,
                      })),
                    ]}
                    required
                  />
                );
              }

              if (type === "textarea") {
                return (
                  <div key={key} className="sm:col-span-2">
                    <Textarea
                      label={label}
                      value={form[key]}
                      onChange={(e) =>
                        setForm((prev) => ({ ...prev, [key]: e.target.value }))
                      }
                      required={required}
                    />
                  </div>
                );
              }

              if (type === "status") {
                return (
                  <Select
                    key={key}
                    label={label}
                    value={form[key]}
                    onChange={(e) =>
                      setForm((prev) => ({ ...prev, [key]: e.target.value }))
                    }
                    options={[
                      { value: "Active", label: "Active" },
                      { value: "Inactive", label: "Inactive" },
                    ]}
                    required={required}
                  />
                );
              }

              if (type === "availability") {
                return (
                  <Select
                    key={key}
                    label={label}
                    value={form[key]}
                    onChange={(e) =>
                      setForm((prev) => ({ ...prev, [key]: e.target.value }))
                    }
                    options={[
                      { value: "Available", label: "Available" },
                      { value: "Unavailable", label: "Unavailable" },
                    ]}
                    required={required}
                  />
                );
              }

              if (type === "payment") {
                return (
                  <Select
                    key={key}
                    label={label}
                    value={form[key]}
                    onChange={(e) =>
                      setForm((prev) => ({ ...prev, [key]: e.target.value }))
                    }
                    options={[
                      { value: "Cash", label: "Cash" },
                      { value: "UPI", label: "UPI" },
                      { value: "Card", label: "Card" },
                    ]}
                    required={required}
                  />
                );
              }

              if (type === "role") {
                return (
                  <Select
                    key={key}
                    label={label}
                    value={form[key]}
                    onChange={(e) =>
                      setForm((prev) => ({ ...prev, [key]: e.target.value }))
                    }
                    options={[
                      { value: "Admin", label: "Admin" },
                      { value: "Manager", label: "Manager" },
                      { value: "Staff", label: "Staff" },
                    ]}
                    required={required}
                  />
                );
              }

              return (
                <Input
                  key={key}
                  label={label}
                  type={type === "number" ? "number" : type}
                  value={form[key]}
                  onChange={(e) =>
                    setForm((prev) => ({ ...prev, [key]: e.target.value }))
                  }
                  required={
                    editing && key === "password" ? false : required
                  }
                  placeholder={
                    editing && key === "password"
                      ? "Leave blank to keep current password"
                      : undefined
                  }
                  disabled={editing && key === config.id}
                />
              );
            })}
          </div>

          {error && (
            <div className="rounded-xl border border-red-500/20 bg-red-500/10 px-3 py-2.5 text-xs text-red-300">
              {error}
            </div>
          )}

          <div className="flex justify-end gap-2 border-t border-[#252a35] pt-4">
            <Button
              type="button"
              variant="secondary"
              onClick={() => setModalOpen(false)}
            >
              Cancel
            </Button>
            <Button type="submit" loading={saving}>
              {editing ? "Save changes" : "Create record"}
            </Button>
          </div>
        </form>
      </Modal>
    </div>
  );
}
