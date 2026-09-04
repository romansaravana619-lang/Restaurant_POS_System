import {
  BarChart3,
  Boxes,
  CreditCard,
  FileText,
  LayoutDashboard,
  LogOut,
  Settings,
  ShoppingCart,
  Store,
  Table2,
  Truck,
  Users,
  UsersRound,
  Utensils,
  X,
} from "lucide-react";
import { NavLink } from "react-router-dom";
import { useAuth } from "../../contexts/auth-context";
import { cn } from "../../lib/cn";

const groups = [
  {
    title: "WORKSPACE",
    items: [
      ["Dashboard", "/dashboard", LayoutDashboard, ["Admin", "Manager", "Staff"]],
      ["POS / Billing", "/pos", ShoppingCart, ["Admin", "Manager", "Staff"]],
      ["Bills", "/bills", FileText, ["Admin", "Manager", "Staff"]],
      ["Tables", "/tables", Table2, ["Admin", "Manager", "Staff"]],
    ],
  },
  {
    title: "MANAGEMENT",
    items: [
      ["Menu", "/menu", Utensils, ["Admin", "Manager", "Staff"]],
      ["Categories", "/categories", Boxes, ["Admin", "Manager", "Staff"]],
      ["Inventory", "/inventory", Boxes, ["Admin", "Manager", "Staff"]],
      ["Suppliers", "/suppliers", Truck, ["Admin", "Manager", "Staff"]],
      ["Customers", "/customers", UsersRound, ["Admin", "Manager", "Staff"]],
    ],
  },
  {
    title: "OPERATIONS",
    items: [
      ["Payments", "/payments", CreditCard, ["Admin", "Manager", "Staff"]],
      ["Employees", "/employees", Users, ["Admin", "Manager"]],
    ],
  },
  {
    title: "SYSTEM",
    items: [
      ["Users", "/users", UsersRound, ["Admin"]],
      ["Settings", "/settings", Settings, ["Admin", "Manager"]],
    ],
  },
];

export default function Sidebar({ open, onClose }) {
  const { user, logout } = useAuth();

  return (
    <aside
      className={cn(
        "fixed inset-y-0 left-0 z-40 flex w-[248px] flex-col border-r border-[#252a35] bg-[#0d1016] transition-transform lg:static lg:translate-x-0",
        open ? "translate-x-0" : "-translate-x-full",
      )}
    >
      <div className="flex h-16 items-center justify-between border-b border-[#252a35] px-5">
        <div>
          <div className="text-lg font-bold tracking-tight">
            <span className="text-white">SARU</span>
            <span className="text-violet-400">POS</span>
          </div>
          <div className="text-[9px] font-medium uppercase tracking-[0.2em] text-slate-600">
            Restaurant Operations
          </div>
        </div>

        <button
          onClick={onClose}
          className="rounded-lg p-1.5 text-slate-500 lg:hidden"
        >
          <X size={17} />
        </button>
      </div>

      <nav className="flex-1 overflow-y-auto px-3 py-5">
        {groups.map((group) => {
          const visible = group.items.filter(([, , , roles]) =>
            roles.includes(user?.role),
          );

          if (!visible.length) return null;

          return (
            <div key={group.title} className="mb-6">
              <div className="px-3 pb-2 text-[10px] font-semibold tracking-[0.18em] text-slate-600">
                {group.title}
              </div>

              <div className="space-y-1">
                {visible.map(([label, path, Icon]) => (
                  <NavLink
                    key={path}
                    to={path}
                    onClick={onClose}
                    className={({ isActive }) =>
                      cn(
                        "group flex items-center gap-3 rounded-xl border-l-2 px-3 py-2.5 text-sm transition",
                        isActive
                          ? "border-violet-500 bg-white/[0.045] text-white"
                          : "border-transparent text-slate-500 hover:bg-white/[0.025] hover:text-slate-300",
                      )
                    }
                  >
                    <Icon size={16} />
                    <span>{label}</span>
                  </NavLink>
                ))}
              </div>
            </div>
          );
        })}
      </nav>

      <div className="border-t border-[#252a35] p-3">
        <div className="mb-2 rounded-xl bg-[#151923] px-3 py-2.5">
          <div className="truncate text-xs font-medium text-slate-200">
            {user?.username || "User"}
          </div>
          <div className="mt-0.5 flex items-center gap-1.5 text-[10px] text-slate-500">
            <Store size={11} />
            {user?.role || "Staff"}
          </div>
        </div>

        <button
          onClick={logout}
          className="flex w-full items-center gap-3 rounded-xl px-3 py-2.5 text-sm text-slate-500 hover:bg-red-500/[0.06] hover:text-red-300"
        >
          <LogOut size={16} />
          Sign out
        </button>
      </div>
    </aside>
  );
}
