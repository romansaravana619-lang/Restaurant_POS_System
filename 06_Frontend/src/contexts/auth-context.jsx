import { createContext, useContext, useEffect, useMemo, useState } from "react";
import { clearAuth, getStoredUser, login as loginApi } from "../services/api";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(getStoredUser);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const handleUnauthorized = () => {
      setUser(null);
    };

    window.addEventListener("sarupos:unauthorized", handleUnauthorized);
    return () =>
      window.removeEventListener("sarupos:unauthorized", handleUnauthorized);
  }, []);

  async function login(username, password) {
    setLoading(true);

    try {
      const result = await loginApi(username, password);

      localStorage.setItem("sarupos_access_token", result.access_token);
      localStorage.setItem("sarupos_user", JSON.stringify(result.user));
      setUser(result.user);

      return result;
    } finally {
      setLoading(false);
    }
  }

  function logout() {
    clearAuth();
    setUser(null);
  }

  const value = useMemo(
    () => ({
      user,
      loading,
      authenticated: Boolean(user && localStorage.getItem("sarupos_access_token")),
      login,
      logout,
    }),
    [user, loading],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error("useAuth must be used inside AuthProvider");
  }

  return context;
}
