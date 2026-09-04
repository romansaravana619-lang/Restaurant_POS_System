import { useEffect, useState } from "react";
import { Outlet, Navigate } from "react-router-dom";
import Sidebar from "./sidebar";
import Topbar from "./topbar";
import { useAuth } from "../../contexts/auth-context";

export default function AppLayout() {
  const { authenticated } = useAuth();
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [refreshKey, setRefreshKey] = useState(0);

  useEffect(() => {
    if (!authenticated) return;

    setSidebarOpen(false);
  }, [authenticated]);

  if (!authenticated) {
    return <Navigate to="/login" replace />;
  }

  return (
    <div className="min-h-screen bg-[#0b0d12] text-slate-100 lg:flex">
      <Sidebar
        open={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
      />

      <div className="min-w-0 flex-1">
        <Topbar
          onOpenSidebar={() => setSidebarOpen(true)}
          onRefresh={() => setRefreshKey((value) => value + 1)}
        />

        <main className="p-4 lg:p-6">
          <Outlet context={{ refreshKey }} />
        </main>
      </div>

      {sidebarOpen && (
        <button
          onClick={() => setSidebarOpen(false)}
          className="fixed inset-0 z-30 bg-black/60 lg:hidden"
          aria-label="Close navigation"
        />
      )}
    </div>
  );
}
