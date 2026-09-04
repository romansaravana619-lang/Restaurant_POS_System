import { useEffect, useState } from "react";
import { Settings2 } from "lucide-react";
import { Button, Card, Input } from "../components/ui";
import { services } from "../services/api";

const blank = {
  setting_id: "",
  restaurant_name: "",
  gst_number: "",
  address: "",
  phone: "",
  email: "",
  currency: "INR",
  tax_percentage: 5,
};

export default function SettingsPage() {
  const [settings, setSettings] = useState([]);
  const [form, setForm] = useState(blank);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  async function load() {
    setLoading(true);
    setError("");

    try {
      const result = await services.settings.list();
      const rows = result.settings || [];
      setSettings(rows);

      if (rows[0]) {
        setForm(rows[0]);
      }
    } catch (err) {
      if (err.status !== 404) setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    load();
  }, []);

  async function save() {
    setSaving(true);
    setMessage("");
    setError("");

    try {
      const body = {
        restaurant_name: form.restaurant_name,
        gst_number: form.gst_number,
        address: form.address,
        phone: form.phone,
        email: form.email,
        currency: form.currency,
        tax_percentage: Number(form.tax_percentage),
      };

      if (form.setting_id) {
        await services.settings.update(form.setting_id, body);
      } else {
        await services.settings.create({
          ...body,
          setting_id: `SET${Date.now()}`,
        });
      }

      setMessage("Settings saved successfully.");
      await load();
    } catch (err) {
      setError(err.message);
    } finally {
      setSaving(false);
    }
  }

  return (
    <div className="mx-auto max-w-4xl space-y-5">
      <div>
        <h2 className="text-xl font-semibold text-white">Restaurant settings</h2>
        <p className="mt-1 text-sm text-slate-600">
          Keep business identity, contact and tax configuration in one place.
        </p>
      </div>

      <Card className="p-5">
        <div className="mb-6 flex items-center gap-3">
          <div className="rounded-xl border border-violet-500/20 bg-violet-500/10 p-2.5">
            <Settings2 size={17} className="text-violet-300" />
          </div>
          <div>
            <h3 className="text-sm font-semibold text-white">Restaurant</h3>
            <p className="text-xs text-slate-600">
              Core business configuration
            </p>
          </div>
        </div>

        {loading ? (
          <div className="text-sm text-slate-600">Loading settings...</div>
        ) : (
          <div className="grid gap-4 sm:grid-cols-2">
            <Input
              label="Restaurant Name"
              value={form.restaurant_name}
              onChange={(e) =>
                setForm({ ...form, restaurant_name: e.target.value })
              }
              className="sm:col-span-2"
              required
            />

            <Input
              label="GST Number"
              value={form.gst_number}
              onChange={(e) =>
                setForm({ ...form, gst_number: e.target.value })
              }
            />

            <Input
              label="Currency"
              value={form.currency}
              onChange={(e) => setForm({ ...form, currency: e.target.value })}
              required
            />

            <Input
              label="Phone"
              value={form.phone}
              onChange={(e) => setForm({ ...form, phone: e.target.value })}
            />

            <Input
              label="Email"
              type="email"
              value={form.email}
              onChange={(e) => setForm({ ...form, email: e.target.value })}
            />

            <Input
              label="Tax Percentage"
              type="number"
              min="0"
              step="0.01"
              value={form.tax_percentage}
              onChange={(e) =>
                setForm({ ...form, tax_percentage: e.target.value })
              }
              required
            />

            <Input
              label="Address"
              value={form.address}
              onChange={(e) => setForm({ ...form, address: e.target.value })}
              className="sm:col-span-2"
            />
          </div>
        )}

        {error && (
          <div className="mt-5 rounded-xl border border-red-500/20 bg-red-500/10 px-4 py-3 text-xs text-red-300">
            {error}
          </div>
        )}

        {message && (
          <div className="mt-5 rounded-xl border border-emerald-500/20 bg-emerald-500/10 px-4 py-3 text-xs text-emerald-300">
            {message}
          </div>
        )}

        <div className="mt-6 flex justify-end border-t border-[#252a35] pt-4">
          <Button onClick={save} loading={saving}>
            Save settings
          </Button>
        </div>
      </Card>
    </div>
  );
}
