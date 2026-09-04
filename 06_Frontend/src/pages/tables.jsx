import { useEffect, useState } from "react";
import { Plus, Users } from "lucide-react";
import { Button, Card, Modal, Input, Select, Badge } from "../components/ui";
import { services } from "../services/api";

const empty = {
  table_id: "",
  table_number: "",
  capacity: 4,
  status: "Available",
};

const tones = {
  Available: "border-emerald-500/20 bg-emerald-500/[0.035]",
  Occupied: "border-violet-500/20 bg-violet-500/[0.04]",
  Reserved: "border-amber-500/20 bg-amber-500/[0.035]",
  Cleaning: "border-cyan-500/20 bg-cyan-500/[0.035]",
  Inactive: "border-red-500/20 bg-red-500/[0.03]",
};

export default function Tables() {
  const [tables, setTables] = useState([]);
  const [modal, setModal] = useState(false);
  const [form, setForm] = useState(empty);
  const [editing, setEditing] = useState(null);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");

  async function load() {
    try {
      const result = await services.tables.list();
      setTables(result.restaurant_tables || []);
    } catch (err) {
      if (err.status !== 404) setError(err.message);
      setTables([]);
    }
  }

  useEffect(() => {
    load();
  }, []);

  function openCreate() {
    setEditing(null);
    setForm(empty);
    setError("");
    setModal(true);
  }

  function openEdit(table) {
    setEditing(table);
    setForm({
      table_id: table.table_id,
      table_number: table.table_number,
      capacity: table.capacity,
      status: table.status,
    });
    setError("");
    setModal(true);
  }

  async function save(event) {
    event.preventDefault();
    setSaving(true);
    setError("");

    try {
      const body = {
        table_number: form.table_number,
        capacity: Number(form.capacity),
        status: form.status,
      };

      if (editing) {
        await services.tables.update(editing.table_id, body);
      } else {
        await services.tables.create({
          ...body,
          table_id: form.table_id,
        });
      }

      setModal(false);
      await load();
    } catch (err) {
      setError(err.message);
    } finally {
      setSaving(false);
    }
  }

  async function remove(table) {
    if (!window.confirm(`Delete ${table.table_number}?`)) return;

    try {
      await services.tables.remove(table.table_id);
      await load();
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <div className="space-y-5">
      <div className="flex flex-col justify-between gap-4 md:flex-row md:items-end">
        <div>
          <h2 className="text-xl font-semibold text-white">Restaurant floor</h2>
          <p className="mt-1 text-sm text-slate-600">
            A spatial view of table availability and seating.
          </p>
        </div>

        <Button onClick={openCreate}>
          <Plus size={15} />
          Add table
        </Button>
      </div>

      {error && (
        <div className="rounded-xl border border-red-500/20 bg-red-500/10 px-4 py-3 text-xs text-red-300">
          {error}
        </div>
      )}

      {!tables.length ? (
        <Card className="p-10 text-center text-sm text-slate-600">
          No restaurant tables found.
        </Card>
      ) : (
        <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
          {tables.map((table) => (
            <Card
              key={table.table_id}
              className={`relative overflow-hidden p-5 ${tones[table.status] || tones.Available}`}
            >
              <div className="flex items-start justify-between">
                <div>
                  <div className="text-lg font-semibold text-white">
                    {table.table_number}
                  </div>
                  <div className="mt-1 text-xs text-slate-500">
                    {table.capacity} seats
                  </div>
                </div>

                <Badge value={table.status} />
              </div>

              <div className="mt-8 flex items-center justify-between">
                <div className="flex items-center gap-2 text-xs text-slate-500">
                  <Users size={14} />
                  Capacity {table.capacity}
                </div>

                <div className="flex gap-1">
                  <button
                    onClick={() => openEdit(table)}
                    className="rounded-lg border border-[#252a35] px-2.5 py-1.5 text-[11px] text-slate-400 hover:text-white"
                  >
                    Edit
                  </button>
                  <button
                    onClick={() => remove(table)}
                    className="rounded-lg border border-red-500/10 px-2.5 py-1.5 text-[11px] text-red-400 hover:bg-red-500/10"
                  >
                    Delete
                  </button>
                </div>
              </div>
            </Card>
          ))}
        </div>
      )}

      <Modal
        open={modal}
        onClose={() => setModal(false)}
        title={editing ? "Edit table" : "Add restaurant table"}
      >
        <form onSubmit={save} className="space-y-4">
          {!editing && (
            <Input
              label="Table ID"
              value={form.table_id}
              onChange={(e) => setForm({ ...form, table_id: e.target.value })}
              required
            />
          )}

          <Input
            label="Table Number"
            value={form.table_number}
            onChange={(e) =>
              setForm({ ...form, table_number: e.target.value })
            }
            required
          />

          <Input
            label="Capacity"
            type="number"
            min="1"
            value={form.capacity}
            onChange={(e) => setForm({ ...form, capacity: e.target.value })}
            required
          />

          <Select
            label="Status"
            value={form.status}
            onChange={(e) => setForm({ ...form, status: e.target.value })}
            options={[
              { value: "Available", label: "Available" },
              { value: "Occupied", label: "Occupied" },
              { value: "Reserved", label: "Reserved" },
              { value: "Cleaning", label: "Cleaning" },
              { value: "Inactive", label: "Inactive" },
            ]}
          />

          {error && (
            <div className="rounded-xl border border-red-500/20 bg-red-500/10 px-3 py-2.5 text-xs text-red-300">
              {error}
            </div>
          )}

          <div className="flex justify-end gap-2">
            <Button
              type="button"
              variant="secondary"
              onClick={() => setModal(false)}
            >
              Cancel
            </Button>
            <Button type="submit" loading={saving}>
              Save table
            </Button>
          </div>
        </form>
      </Modal>
    </div>
  );
}
