import { motion } from "motion/react";
import {
  Eye,
  EyeOff,
  Fingerprint,
  LockKeyhole,
  LogIn,
  ScanLine,
  UserRound,
} from "lucide-react";
import { useState } from "react";
import { Navigate, useLocation, useNavigate } from "react-router-dom";
import { Button, Input } from "../components/ui";
import { useAuth } from "../contexts/auth-context";

export default function Login() {
  const { authenticated, login, loading } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [remember, setRemember] = useState(true);
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");

  if (authenticated) {
    return <Navigate to="/dashboard" replace />;
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");

    if (!username.trim() || !password) {
      setError("Username and password are required.");
      return;
    }

    try {
      await login(username.trim(), password);

      if (remember) {
        localStorage.setItem("sarupos_remember", "true");
      } else {
        localStorage.removeItem("sarupos_remember");
      }

      navigate(location.state?.from?.pathname || "/dashboard", {
        replace: true,
      });
    } catch (err) {
      setError(err.message || "Unable to sign in.");
    }
  }

  return (
    <main className="sarupos-login-shell">
      <div className="sarupos-login-bg" />
      <div className="sarupos-login-vignette" />
      <div className="sarupos-login-grid" />

      <div className="sarupos-login-content">
        <motion.div
          initial={{ opacity: 0, y: 18 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.45, ease: "easeOut" }}
          className="sarupos-login-card"
        >
          <div className="sarupos-brand">
            <div className="sarupos-brand-mark">
              <span>S</span>
            </div>

            <div>
              <div className="sarupos-brand-name">
                Saru<span>POS</span>
              </div>

              <div className="sarupos-brand-subtitle">
                Premium Restaurant POS
              </div>
            </div>
          </div>

          <form onSubmit={handleSubmit} className="mt-7" autoComplete="off">
            <div className="sarupos-field">
              <label htmlFor="username">Username / Employee ID</label>

              <div className="sarupos-input-wrap">
                <UserRound size={15} />
                <input
                  id="username"
                  type="text"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  placeholder="Enter username"
                  autoComplete="off"
                  autoFocus
                />
                <span className="sarupos-field-dot" />
              </div>
            </div>

            <div className="sarupos-field mt-4">
              <div className="flex items-center justify-between gap-3">
                <label htmlFor="password">Password</label>

                <button
                  type="button"
                  className="sarupos-forgot"
                  onClick={() =>
                    setError("Password recovery is managed by your administrator.")
                  }
                >
                  Forgot Password?
                </button>
              </div>

              <div className="sarupos-input-wrap">
                <LockKeyhole size={15} />

                <input
                  id="password"
                  type={showPassword ? "text" : "password"}
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Enter password"
                  autoComplete="new-password"
                />

                <button
                  type="button"
                  className="sarupos-eye"
                  onClick={() => setShowPassword((value) => !value)}
                  aria-label={showPassword ? "Hide password" : "Show password"}
                >
                  {showPassword ? <EyeOff size={15} /> : <Eye size={15} />}
                </button>
              </div>
            </div>

            {error && (
              <motion.div
                initial={{ opacity: 0, y: -4 }}
                animate={{ opacity: 1, y: 0 }}
                className="sarupos-error"
              >
                {error}
              </motion.div>
            )}

            <Button
              type="submit"
              loading={loading}
              className="sarupos-signin-btn"
            >
              <LogIn size={15} />
              SIGN IN
            </Button>

            <div className="sarupos-options">
              <label className="sarupos-check">
                <input
                  type="checkbox"
                  checked={remember}
                  onChange={(e) => setRemember(e.target.checked)}
                />
                <span className="sarupos-check-box">
                  {remember ? "âœ“" : ""}
                </span>
                <span>Remember Me</span>
              </label>

              <button
                type="button"
                className="sarupos-request"
                onClick={() =>
                  setError("Access requests should be submitted to your administrator.")
                }
              >
                Request Access
              </button>
            </div>

            <div className="sarupos-divider">
              <span />
              <small>SECURE ACCESS</small>
              <span />
            </div>

            <div className="sarupos-extra-actions">
              <button
                type="button"
                className="sarupos-secondary-btn"
                disabled
                title="Biometric hardware integration is not enabled yet"
              >
                <Fingerprint size={15} />
                Biometric Login
              </button>

              <button
                type="button"
                className="sarupos-secondary-btn"
                disabled
                title="Employee badge scanner integration is not enabled yet"
              >
                <ScanLine size={15} />
                Scan Employee Badge
              </button>
            </div>
          </form>

          <div className="sarupos-card-footer">
            <span>JWT secured access</span>
            <span className="sarupos-status-dot" />
            <span>SaruPOS v1.0</span>
          </div>
        </motion.div>
      </div>

      <div className="sarupos-corner-label">
        <span>RESTAURANT OPERATIONS PLATFORM</span>
      </div>
    </main>
  );
}
