import { Navigate, Route, Routes } from "react-router-dom";
import AppLayout from "./components/layouts/app-layout";
import { useAuth } from "./contexts/auth-context";
import Login from "./pages/login";
import Dashboard from "./pages/dashboard";
import POS from "./pages/pos";
import Tables from "./pages/tables";
import ResourcePage from "./pages/resource-page";
import SettingsPage from "./pages/settings";

function Protected({ children }) {
  const { authenticated } = useAuth();

  return authenticated ? children : <Navigate to="/login" replace />;
}

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />

      <Route
        element={
          <Protected>
            <AppLayout />
          </Protected>
        }
      >
        <Route index element={<Navigate to="/dashboard" replace />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/pos" element={<POS />} />
        <Route path="/bills" element={<ResourcePage resource="bills" />} />
        <Route path="/tables" element={<Tables />} />

        <Route
          path="/menu"
          element={<ResourcePage resource="menu" />}
        />
        <Route
          path="/categories"
          element={<ResourcePage resource="categories" />}
        />
        <Route
          path="/inventory"
          element={<ResourcePage resource="inventory" />}
        />
        <Route
          path="/suppliers"
          element={<ResourcePage resource="suppliers" />}
        />
        <Route
          path="/customers"
          element={<ResourcePage resource="customers" />}
        />
        <Route
          path="/payments"
          element={<ResourcePage resource="payments" />}
        />
        <Route
          path="/employees"
          element={<ResourcePage resource="employees" />}
        />
        <Route
          path="/users"
          element={<ResourcePage resource="users" />}
        />
        <Route path="/settings" element={<SettingsPage />} />
      </Route>

      <Route path="*" element={<Navigate to="/dashboard" replace />} />
    </Routes>
  );
}
