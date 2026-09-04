import { Bell, Menu, RefreshCw } from "lucide-react";
import { useLocation } from "react-router-dom";
import { useAuth } from "../../contexts/auth-context";
import { Button } from "../ui";

const titles = {
  "/dashboard": ["Dashboard", "Live operational overview"],
  "/pos": ["POS / Billing", "Fast order and checkout workflow"],
  "/bills": ["Bills", "Billing history and completed invoices"],
  "/tables": ["Tables", "Restaurant floor and table status"],
  "/menu": ["Menu", "Manage dishes and availability"],
  "/categories": ["Categories", "Organize your menu"],
  "/inventory": ["Inventory", "Monitor stock and reorder levels"],
  "/suppliers": ["Suppliers", "Supplier relationships"],
  "/customers": ["Customers", "Customer directory"],
  "/payments": ["Payments", "Payment records and status"],
  "/employees": ["Employees", "Staff and workforce management"],
  "/users": ["Users", "Login accounts and permissions"],
  "/settings": ["Settings", "Restaurant configuration"],
};

export default function Topbar({ onOpenSidebar, onRefresh }) {
  const location = useLocation();
  const { user } = useAuth();
  const [title, subtitle] = titles[location.pathname] || ["SaruPOS", "Restaurant operations"];

  return (
    <header className="flex min-h-16 items-center justify-between border-b border-[#252a35] bg-[#0d1016]/90 px-4 backdrop-blur lg:px-6">
      <div className="flex items-center gap-3">
        <button
          onClick={onOpenSidebar}
          className="rounded-xl border border-[#252a35] p-2 text-slate-500 hover:text-white lg:hidden"
        >
          <Menu size={18} />
        </button>

        <div>
          <h1 className="text-sm font-semibold text-white">{title}</h1>
          <p className="text-[11px] text-slate-600">{subtitle}</p>
        </div>
      </div>

      <div className="flex items-center gap-2">
        <div className="hidden items-center gap-2 rounded-full border border-[#252a35] bg-[#10131a] px-3 py-1.5 text-[10px] text-slate-500 sm:flex">
          <span className="h-1.5 w-1.5 rounded-full bg-emerald-400" />
          API Connected
        </div>

        <button
          onClick={onRefresh}
          className="rounded-xl border border-[#252a35] p-2 text-slate-500 hover:text-slate-200"
          title="Refresh"
        >
          <RefreshCw size={15} />
        </button>

        <button className="relative rounded-xl border border-[#252a35] p-2 text-slate-500 hover:text-slate-200">
          <Bell size={15} />
          <span className="absolute right-1 top-1 h-1.5 w-1.5 rounded-full bg-violet-400" />
        </button>

        <Button variant="secondary" size="sm" className="hidden sm:inline-flex">
          {user?.role || "Staff"}
        </Button>
      </div>
    </header>
  );
}
