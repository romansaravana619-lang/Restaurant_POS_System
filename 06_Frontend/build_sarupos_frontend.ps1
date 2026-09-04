$ErrorActionPreference = "Stop"

$root = Get-Location
$src = Join-Path $root "src"

New-Item -ItemType Directory -Force "$src\components\layouts" | Out-Null
New-Item -ItemType Directory -Force "$src\components\ui" | Out-Null
New-Item -ItemType Directory -Force "$src\contexts" | Out-Null
New-Item -ItemType Directory -Force "$src\hooks" | Out-Null
New-Item -ItemType Directory -Force "$src\lib" | Out-Null
New-Item -ItemType Directory -Force "$src\pages" | Out-Null
New-Item -ItemType Directory -Force "$src\services" | Out-Null

function Write-File($path, $content) {
    $full = Join-Path $root $path
    $dir = Split-Path $full -Parent
    New-Item -ItemType Directory -Force $dir | Out-Null
    Set-Content -Path $full -Value $content -Encoding UTF8
    Write-Host "Written: $path"
}

Write-File "vite.config.js" @'
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
});
'@

Write-File "src/index.css" @'
@import "tailwindcss";

:root {
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: #f8fafc;
  background: #0b0d12;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
}

* {
  box-sizing: border-box;
}

html,
body,
#root {
  min-height: 100%;
  margin: 0;
}

body {
  min-width: 320px;
  background:
    radial-gradient(circle at top right, rgba(124, 58, 237, 0.08), transparent 28%),
    #0b0d12;
}

button,
input,
select,
textarea {
  font: inherit;
}

button {
  cursor: pointer;
}

::selection {
  background: rgba(139, 92, 246, 0.35);
}

::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: #0b0d12;
}

::-webkit-scrollbar-thumb {
  background: #252a35;
  border-radius: 999px;
}

::-webkit-scrollbar-thumb:hover {
  background: #3a4150;
}
 
/* SaruPOS Login */
.sarupos-login-shell {
  min-height: 100vh;
  display: grid;
  grid-template-columns: minmax(0, 1.35fr) minmax(420px, 0.65fr);
  background: #0b0d12;
}

.sarupos-login-visual {
  position: relative;
  min-height: 100vh;
  overflow: hidden;
  background:
    linear-gradient(90deg, rgba(11, 13, 18, 0.18), rgba(11, 13, 18, 0.74)),
    url("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=2400&q=90")
      center / cover no-repeat;
}

.sarupos-login-visual::after {
  content: "";
  position: absolute;
  inset: 0;
  background:
    linear-gradient(180deg, rgba(11, 13, 18, 0.08), rgba(11, 13, 18, 0.78)),
    radial-gradient(circle at 70% 35%, rgba(139, 92, 246, 0.12), transparent 36%);
}

.sarupos-login-brand {
  position: relative;
  z-index: 1;
  padding: 48px;
}

.sarupos-login-brand-title {
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #ffffff;
}

.sarupos-login-brand-title span {
  color: #a78bfa;
}

.sarupos-login-brand-subtitle {
  margin-top: 6px;
  font-size: 13px;
  color: #cbd5e1;
}

.sarupos-login-content {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
  background:
    radial-gradient(circle at top right, rgba(139, 92, 246, 0.08), transparent 30%),
    #0b0d12;
}

.sarupos-login-card {
  width: min(100%, 430px);
  padding: 36px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 24px;
  background: rgba(16, 19, 26, 0.94);
  box-shadow:
    0 24px 60px rgba(0, 0, 0, 0.38),
    0 0 0 1px rgba(139, 92, 246, 0.04);
  backdrop-filter: blur(18px);
}

.sarupos-login-card h1,
.sarupos-login-card h2 {
  margin: 0;
  color: #f8fafc;
}

.sarupos-login-card p {
  color: #94a3b8;
}

.sarupos-login-card label {
  color: #cbd5e1;
}

.sarupos-login-card input {
  width: 100%;
  border: 1px solid #2d3340;
  border-radius: 12px;
  background: #10131a;
  color: #f8fafc;
  outline: none;
}

.sarupos-login-card input:focus {
  border-color: #8b5cf6;
  box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.14);
}

.sarupos-login-card button[type="submit"] {
  border-radius: 12px;
}

@media (max-width: 980px) {
  .sarupos-login-shell {
    grid-template-columns: 1fr;
  }

  .sarupos-login-visual {
    display: none;
  }

  .sarupos-login-content {
    min-height: 100vh;
    padding: 24px;
  }
}
 
/* ===== SaruPOS Login UI ===== */

.sarupos-login-shell {
  position: relative;
  min-height: 100vh;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #090b10;
}

.sarupos-login-bg {
  position: absolute;
  inset: 0;
  background:
    linear-gradient(90deg, rgba(7, 9, 13, 0.30), rgba(7, 9, 13, 0.72)),
    url("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=2400&q=90")
      center / cover no-repeat;
  transform: scale(1.02);
}

.sarupos-login-vignette {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at center, transparent 20%, rgba(7, 9, 13, 0.45) 68%, rgba(7, 9, 13, 0.82) 100%),
    linear-gradient(180deg, rgba(7, 9, 13, 0.18), rgba(7, 9, 13, 0.55));
}

.sarupos-login-grid {
  position: absolute;
  inset: 0;
  opacity: 0.18;
  background-image:
    linear-gradient(rgba(255,255,255,0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.035) 1px, transparent 1px);
  background-size: 44px 44px;
  mask-image: linear-gradient(to bottom, transparent, black 20%, black 80%, transparent);
}

.sarupos-login-content {
  position: relative;
  z-index: 2;
  width: min(100%, 520px);
  padding: 28px 20px;
}

.sarupos-login-card {
  width: 100%;
  padding: 34px;
  border: 1px solid rgba(255,255,255,0.10);
  border-radius: 24px;
  background: rgba(12, 15, 22, 0.88);
  box-shadow:
    0 30px 80px rgba(0,0,0,0.48),
    0 0 0 1px rgba(139,92,246,0.04);
  backdrop-filter: blur(22px);
}

.sarupos-brand {
  display: flex;
  align-items: center;
  gap: 13px;
}

.sarupos-brand-mark {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 0 0 auto;
  border-radius: 13px;
  background: linear-gradient(135deg, #8b5cf6, #6d28d9);
  color: white;
  font-size: 20px;
  font-weight: 800;
  box-shadow: 0 10px 28px rgba(124,58,237,0.28);
}

.sarupos-brand-name {
  color: #f8fafc;
  font-size: 21px;
  font-weight: 800;
  letter-spacing: -0.03em;
}

.sarupos-brand-name span {
  color: #a78bfa;
}

.sarupos-brand-subtitle {
  margin-top: 3px;
  color: #64748b;
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.sarupos-field label {
  display: block;
  margin-bottom: 8px;
  color: #cbd5e1;
  font-size: 13px;
  font-weight: 600;
}

.sarupos-input-wrap {
  position: relative;
  display: flex;
  align-items: center;
  min-height: 44px;
  border: 1px solid #2a303c;
  border-radius: 12px;
  background: rgba(255,255,255,0.035);
  transition: border-color 0.2s, box-shadow 0.2s, background 0.2s;
}

.sarupos-input-wrap:focus-within {
  border-color: #8b5cf6;
  background: rgba(255,255,255,0.055);
  box-shadow: 0 0 0 3px rgba(139,92,246,0.12);
}

.sarupos-input-wrap > svg {
  flex: 0 0 auto;
  margin-left: 13px;
  color: #64748b;
}

.sarupos-input-wrap input {
  width: 100%;
  min-width: 0;
  border: 0;
  outline: 0;
  background: transparent;
  color: #f8fafc;
  padding: 11px 12px;
  font-size: 14px;
}

.sarupos-input-wrap input::placeholder {
  color: #475569;
}

.sarupos-field-dot {
  width: 6px;
  height: 6px;
  margin-right: 13px;
  flex: 0 0 auto;
  border-radius: 999px;
  background: #22c55e;
  box-shadow: 0 0 10px rgba(34,197,94,0.45);
}

.sarupos-forgot {
  border: 0;
  background: transparent;
  color: #a78bfa;
  font-size: 12px;
  cursor: pointer;
}

.sarupos-forgot:hover {
  color: #c4b5fd;
}

.sarupos-eye {
  margin-right: 10px;
  border: 0;
  background: transparent;
  color: #64748b;
  cursor: pointer;
}

.sarupos-eye:hover {
  color: #e2e8f0;
}

.sarupos-error {
  margin-top: 12px;
  padding: 10px 12px;
  border: 1px solid rgba(239,68,68,0.25);
  border-radius: 10px;
  background: rgba(239,68,68,0.10);
  color: #fca5a5;
  font-size: 12px;
}

.sarupos-signin-btn {
  width: 100%;
  margin-top: 18px;
  min-height: 46px;
  border: 0;
  border-radius: 12px;
  background: linear-gradient(135deg, #8b5cf6, #7c3aed);
  color: #fff;
  font-weight: 700;
  box-shadow: 0 12px 28px rgba(124,58,237,0.24);
}

.sarupos-signin-btn:hover {
  filter: brightness(1.06);
}

.sarupos-options {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-top: 14px;
  color: #94a3b8;
  font-size: 12px;
}

.sarupos-check {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.sarupos-check input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.sarupos-check-box {
  width: 16px;
  height: 16px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #3a4250;
  border-radius: 5px;
  background: #11151d;
  color: white;
  font-size: 10px;
}

.sarupos-check input:checked + .sarupos-check-box {
  border-color: #8b5cf6;
  background: #8b5cf6;
}

.sarupos-request {
  border: 0;
  background: transparent;
  color: #a78bfa;
  font-size: 12px;
  cursor: pointer;
}

.sarupos-divider {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 22px 0 14px;
}

.sarupos-divider span {
  flex: 1;
  height: 1px;
  background: rgba(255,255,255,0.07);
}

.sarupos-divider small {
  color: #475569;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.13em;
}

.sarupos-extra-actions {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.sarupos-secondary-btn {
  min-height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 10px;
  background: rgba(255,255,255,0.025);
  color: #64748b;
  font-size: 11px;
}

.sarupos-secondary-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.sarupos-card-footer {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-top: 18px;
  color: #475569;
  font-size: 10px;
}

.sarupos-status-dot {
  width: 5px;
  height: 5px;
  border-radius: 999px;
  background: #22c55e;
  box-shadow: 0 0 8px rgba(34,197,94,0.5);
}

@media (max-width: 640px) {
  .sarupos-login-content {
    padding: 16px;
  }

  .sarupos-login-card {
    padding: 24px;
    border-radius: 20px;
  }

  .sarupos-extra-actions {
    grid-template-columns: 1fr;
  }

  .sarupos-options {
    align-items: flex-start;
    flex-direction: column;
  }
}
 
/* ===== Login Final Layout Override ===== */

.sarupos-login-shell {
  display: grid;
  grid-template-columns: 1.55fr 0.75fr;
  align-items: stretch;
  justify-content: stretch;
}

.sarupos-login-bg {
  position: absolute;
  inset: 0;
  background:
    linear-gradient(90deg, rgba(7, 9, 13, 0.18), rgba(7, 9, 13, 0.68)),
    url("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=2400&q=90")
      center / cover no-repeat;
}

.sarupos-login-vignette {
  background:
    linear-gradient(
      90deg,
      rgba(7, 9, 13, 0.04) 0%,
      rgba(7, 9, 13, 0.18) 38%,
      rgba(7, 9, 13, 0.82) 78%,
      #090b10 100%
    );
}

.sarupos-login-grid {
  opacity: 0.08;
}

.sarupos-login-content {
  position: relative;
  z-index: 3;
  grid-column: 2;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px;
  background: rgba(8, 10, 15, 0.90);
  border-left: 1px solid rgba(255,255,255,0.07);
  backdrop-filter: blur(14px);
}

.sarupos-login-card {
  width: min(100%, 430px);
  padding: 34px;
  border: 1px solid rgba(255,255,255,0.10);
  border-radius: 22px;
  background: rgba(13, 16, 23, 0.96);
  box-shadow:
    0 30px 80px rgba(0,0,0,0.48),
    0 0 0 1px rgba(139,92,246,0.04);
}

@media (max-width: 980px) {
  .sarupos-login-shell {
    display: flex;
  }

  .sarupos-login-bg {
    opacity: 0.42;
  }

  .sarupos-login-content {
    grid-column: auto;
    min-height: 100vh;
    border-left: 0;
    background: rgba(8, 10, 15, 0.58);
    backdrop-filter: blur(10px);
    padding: 24px;
  }
}

/* ===== FINAL LOGIN: CENTER CARD ===== */

.sarupos-login-shell {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background: #090b10;
}

.sarupos-login-bg {
  position: absolute;
  inset: 0;
  background:
    linear-gradient(
      90deg,
      rgba(7, 9, 13, 0.38),
      rgba(7, 9, 13, 0.48)
    ),
    url("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=2400&q=90")
      center / cover no-repeat;
}

.sarupos-login-vignette {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(
      circle at center,
      rgba(7, 9, 13, 0.08) 0%,
      rgba(7, 9, 13, 0.28) 62%,
      rgba(7, 9, 13, 0.68) 100%
    );
}

.sarupos-login-grid {
  position: absolute;
  inset: 0;
  opacity: 0.06;
}

.sarupos-login-content {
  position: relative;
  z-index: 5;
  width: min(100%, 540px);
  min-height: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 20px;
  background: transparent;
  border: 0;
  backdrop-filter: none;
}

.sarupos-login-card {
  width: min(100%, 500px);
  padding: 38px;
  border: 1px solid rgba(255,255,255,0.11);
  border-radius: 24px;
  background: rgba(10, 13, 19, 0.90);
  box-shadow:
    0 30px 90px rgba(0,0,0,0.52),
    0 0 0 1px rgba(139,92,246,0.04);
  backdrop-filter: blur(22px);
}

@media (max-width: 640px) {
  .sarupos-login-content {
    width: 100%;
    padding: 20px 14px;
  }

  .sarupos-login-card {
    padding: 26px 22px;
    border-radius: 20px;
  }
}
 
/* SARUPOS FINAL LOGIN OVERRIDE */

.sarupos-login-shell {
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background: #090b10;
}

.sarupos-login-bg {
  position: absolute;
  inset: 0;
  background:
    linear-gradient(
      90deg,
      rgba(7, 9, 13, 0.30),
      rgba(7, 9, 13, 0.48)
    ),
    url("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=2400&q=90")
      center / cover no-repeat;
}

.sarupos-login-vignette {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(
      circle at center,
      rgba(7, 9, 13, 0.08) 0%,
      rgba(7, 9, 13, 0.24) 58%,
      rgba(7, 9, 13, 0.62) 100%
    );
  pointer-events: none;
}

.sarupos-login-grid {
  position: absolute;
  inset: 0;
  opacity: 0.04;
  pointer-events: none;
}

.sarupos-login-content {
  position: relative;
  z-index: 5;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 28px 20px;
}

.sarupos-login-card {
  width: min(100%, 430px);
  padding: 30px;
  border: 1px solid rgba(255,255,255,0.10);
  border-radius: 22px;
  background: rgba(10, 13, 19, 0.93);
  box-shadow:
    0 28px 75px rgba(0,0,0,0.50),
    0 0 0 1px rgba(139,92,246,0.035);
  backdrop-filter: blur(20px);
}

.sarupos-brand-mark {
  width: 42px;
  height: 42px;
}

.sarupos-brand-name {
  font-size: 20px;
}

.sarupos-input-wrap {
  min-height: 44px;
}

.sarupos-signin-btn {
  min-height: 45px;
}

@media (max-width: 640px) {
  .sarupos-login-content {
    padding: 18px 14px;
  }

  .sarupos-login-card {
    width: min(100%, 430px);
    padding: 24px 20px;
    border-radius: 20px;
  }
}

/* ===== FINAL LOGIN CENTER + CLEAN INPUT FOCUS FIX ===== */

.sarupos-login-shell {
  position: relative !important;
  width: 100% !important;
  min-height: 100vh !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  overflow: hidden !important;
}

.sarupos-login-content {
  position: absolute !important;
  inset: 0 !important;
  z-index: 10 !important;
  width: 100% !important;
  min-height: 100vh !important;
  max-width: none !important;
  margin: 0 !important;
  padding: 24px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  background: transparent !important;
  border: 0 !important;
  backdrop-filter: none !important;
}

.sarupos-login-card {
  position: relative !important;
  width: min(430px, calc(100vw - 40px)) !important;
  max-width: 430px !important;
  margin: 0 auto !important;
  transform: none !important;
}

/* Only the outer wrapper gets the focus glow */
.sarupos-input-wrap {
  border: 1px solid #2a303c !important;
  box-shadow: none !important;
  outline: none !important;
}

.sarupos-input-wrap:focus-within {
  border-color: #8b5cf6 !important;
  box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.18) !important;
}

/* Inner input must NEVER create another box */
.sarupos-input-wrap input,
.sarupos-input-wrap input:focus,
.sarupos-input-wrap input:hover,
.sarupos-input-wrap input:active {
  border: 0 !important;
  outline: 0 !important;
  box-shadow: none !important;
  border-radius: 0 !important;
  background: transparent !important;
  appearance: none !important;
  -webkit-appearance: none !important;
}

/* Remove Chrome autofill visual treatment */
.sarupos-input-wrap input:-webkit-autofill,
.sarupos-input-wrap input:-webkit-autofill:hover,
.sarupos-input-wrap input:-webkit-autofill:focus,
.sarupos-input-wrap input:-webkit-autofill:active {
  -webkit-text-fill-color: #f8fafc !important;
  -webkit-box-shadow: 0 0 0 1000px transparent inset !important;
  box-shadow: 0 0 0 1000px transparent inset !important;
  transition: background-color 9999s ease-out 0s !important;
}

@media (max-width: 640px) {
  .sarupos-login-content {
    padding: 16px !important;
  }

  .sarupos-login-card {
    width: min(430px, calc(100vw - 28px)) !important;
  }
}
'@

Write-File "src/lib/cn.js" @'
import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs) {
  return twMerge(clsx(inputs));
}
'@

Write-File "src/services/api.js" @'
const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:5000";

export function getToken() {
  return localStorage.getItem("sarupos_access_token");
}

export function clearAuth() {
  localStorage.removeItem("sarupos_access_token");
  localStorage.removeItem("sarupos_user");
}

export function getStoredUser() {
  try {
    return JSON.parse(localStorage.getItem("sarupos_user") || "null");
  } catch {
    return null;
  }
}

async function request(path, options = {}) {
  const token = getToken();

  const headers = {
    Accept: "application/json",
    ...(options.body !== undefined
      ? { "Content-Type": "application/json" }
      : {}),
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    ...(options.headers || {}),
  };

  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...options,
    headers,
  });

  let data = {};
  try {
    data = await response.json();
  } catch {
    data = {};
  }

  if (response.status === 401) {
    clearAuth();
    window.dispatchEvent(new Event("sarupos:unauthorized"));
  }

  if (!response.ok) {
    const message =
      data?.message ||
      data?.error ||
      `Request failed with status ${response.status}`;
    const error = new Error(message);
    error.status = response.status;
    error.data = data;
    throw error;
  }

  return data;
}

export const api = {
  get: (path) => request(path),
  post: (path, body) =>
    request(path, {
      method: "POST",
      body: JSON.stringify(body),
    }),
  put: (path, body) =>
    request(path, {
      method: "PUT",
      body: JSON.stringify(body),
    }),
  delete: (path) =>
    request(path, {
      method: "DELETE",
    }),
};

export async function login(username, password) {
  return api.post("/login", { username, password });
}

export const services = {
  customers: {
    list: () => api.get("/customers"),
    get: (id) => api.get(`/customers/${id}`),
    create: (body) => api.post("/customers", body),
    update: (id, body) => api.put(`/customers/${id}`, body),
    remove: (id) => api.delete(`/customers/${id}`),
  },

  suppliers: {
    list: () => api.get("/suppliers"),
    get: (id) => api.get(`/suppliers/${id}`),
    create: (body) => api.post("/suppliers", body),
    update: (id, body) => api.put(`/suppliers/${id}`, body),
    remove: (id) => api.delete(`/suppliers/${id}`),
  },

  inventory: {
    list: () => api.get("/inventory-items"),
    get: (id) => api.get(`/inventory-items/${id}`),
    create: (body) => api.post("/inventory-items", body),
    update: (id, body) => api.put(`/inventory-items/${id}`, body),
    remove: (id) => api.delete(`/inventory-items/${id}`),
  },

  categories: {
    list: () => api.get("/categories"),
    get: (id) => api.get(`/categories/${id}`),
    create: (body) => api.post("/categories", body),
    update: (id, body) => api.put(`/categories/${id}`, body),
    remove: (id) => api.delete(`/categories/${id}`),
  },

  menuItems: {
    list: () => api.get("/menu-items"),
    get: (id) => api.get(`/menu-items/${id}`),
    create: (body) => api.post("/menu-items", body),
    update: (id, body) => api.put(`/menu-items/${id}`, body),
    remove: (id) => api.delete(`/menu-items/${id}`),
  },

    tables: {
    list: () => api.get("/restaurant-tables"),
    get: (id) => api.get(`/restaurant-tables/${id}`),
    create: (body) => api.post("/restaurant-tables", body),
    update: (id, body) => api.put(`/restaurant-tables/${id}`, body),
    updateStatus: (id, status) =>
      api.put(`/restaurant-tables/${id}/status`, { status }),
    remove: (id) => api.delete(`/restaurant-tables/${id}`),
  },

  bills: {
    list: () => api.get("/bills"),
    get: (id) => api.get(`/bills/${id}`),
    create: (body) => api.post("/bills", body),
    update: (id, body) => api.put(`/bills/${id}`, body),
    remove: (id) => api.delete(`/bills/${id}`),
  },

  billItems: {
    list: () => api.get("/bill-items"),
    get: (id) => api.get(`/bill-items/${id}`),
    create: (body) => api.post("/bill-items", body),
    update: (id, body) => api.put(`/bill-items/${id}`, body),
    remove: (id) => api.delete(`/bill-items/${id}`),
  },

  payments: {
    list: () => api.get("/payments"),
    get: (id) => api.get(`/payments/${id}`),
    create: (body) => api.post("/payments", body),
    update: (id, body) => api.put(`/payments/${id}`, body),
    remove: (id) => api.delete(`/payments/${id}`),
  },

  employees: {
    list: () => api.get("/employees"),
    get: (id) => api.get(`/employees/${id}`),
    create: (body) => api.post("/employees", body),
    update: (id, body) => api.put(`/employees/${id}`, body),
    remove: (id) => api.delete(`/employees/${id}`),
  },

  settings: {
    list: () => api.get("/settings"),
    get: (id) => api.get(`/settings/${id}`),
    create: (body) => api.post("/settings", body),
    update: (id, body) => api.put(`/settings/${id}`, body),
    remove: (id) => api.delete(`/settings/${id}`),
  },

  users: {
    list: () => api.get("/users"),
    get: (id) => api.get(`/users/${id}`),
    create: (body) => api.post("/users", body),
    update: (id, body) => api.put(`/users/${id}`, body),
    remove: (id) => api.delete(`/users/${id}`),
  },
};
'@

Write-File "src/contexts/auth-context.jsx" @'
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
'@

Write-File "src/hooks/use-auth.js" @'
export { useAuth } from "../contexts/auth-context";
'@

Write-File "src/components/ui/index.jsx" @'
import { Loader2, Search, X } from "lucide-react";
import { cn } from "../../lib/cn";

export function Button({
  variant = "primary",
  size = "md",
  loading = false,
  className,
  children,
  ...props
}) {
  const variants = {
    primary:
      "bg-violet-500 text-white hover:bg-violet-400 border-violet-400/20",
    secondary:
      "bg-[#151923] text-slate-200 hover:bg-[#191e28] border-[#252a35]",
    ghost:
      "bg-transparent text-slate-300 hover:bg-white/[0.04] border-transparent",
    danger:
      "bg-red-500/10 text-red-300 hover:bg-red-500/20 border-red-500/20",
  };

  const sizes = {
    sm: "px-3 py-2 text-xs",
    md: "px-4 py-2.5 text-sm",
    lg: "px-5 py-3 text-sm",
  };

  return (
    <button
      className={cn(
        "inline-flex items-center justify-center gap-2 rounded-xl border font-medium transition disabled:cursor-not-allowed disabled:opacity-50",
        variants[variant],
        sizes[size],
        className,
      )}
      disabled={loading || props.disabled}
      {...props}
    >
      {loading && <Loader2 size={15} className="animate-spin" />}
      {children}
    </button>
  );
}

export function Input({ label, error, className, ...props }) {
  return (
    <label className="block">
      {label && (
        <span className="mb-2 block text-xs font-medium text-slate-400">
          {label}
        </span>
      )}
      <input
        className={cn(
          "w-full rounded-xl border border-[#252a35] bg-[#10131a] px-3.5 py-2.5 text-sm text-slate-100 outline-none transition placeholder:text-slate-600 focus:border-violet-500/60 focus:ring-2 focus:ring-violet-500/10",
          className,
        )}
        {...props}
      />
      {error && <span className="mt-1 block text-xs text-red-400">{error}</span>}
    </label>
  );
}

export function Select({ label, options = [], className, ...props }) {
  return (
    <label className="block">
      {label && (
        <span className="mb-2 block text-xs font-medium text-slate-400">
          {label}
        </span>
      )}
      <select
        className={cn(
          "w-full rounded-xl border border-[#252a35] bg-[#10131a] px-3.5 py-2.5 text-sm text-slate-100 outline-none focus:border-violet-500/60",
          className,
        )}
        {...props}
      >
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </label>
  );
}

export function Textarea({ label, className, ...props }) {
  return (
    <label className="block">
      {label && (
        <span className="mb-2 block text-xs font-medium text-slate-400">
          {label}
        </span>
      )}
      <textarea
        className={cn(
          "min-h-24 w-full rounded-xl border border-[#252a35] bg-[#10131a] px-3.5 py-2.5 text-sm text-slate-100 outline-none focus:border-violet-500/60",
          className,
        )}
        {...props}
      />
    </label>
  );
}

export function Card({ className, children }) {
  return (
    <div
      className={cn(
        "rounded-2xl border border-[#252a35] bg-[#10131a]",
        className,
      )}
    >
      {children}
    </div>
  );
}

export function Badge({ value }) {
  const normalized = String(value || "").toLowerCase();

  let tone = "bg-slate-500/10 text-slate-300 border-slate-500/20";

  if (
    normalized.includes("active") ||
    normalized.includes("available") ||
    normalized.includes("paid") ||
    normalized.includes("completed")
  ) {
    tone = "bg-emerald-500/10 text-emerald-300 border-emerald-500/20";
  }

  if (
    normalized.includes("low") ||
    normalized.includes("reserved") ||
    normalized.includes("pending")
  ) {
    tone = "bg-amber-500/10 text-amber-300 border-amber-500/20";
  }

  if (
    normalized.includes("inactive") ||
    normalized.includes("critical") ||
    normalized.includes("failed")
  ) {
    tone = "bg-red-500/10 text-red-300 border-red-500/20";
  }

  if (normalized.includes("occupied")) {
    tone = "bg-violet-500/10 text-violet-300 border-violet-500/20";
  }

  return (
    <span
      className={cn(
        "inline-flex rounded-full border px-2.5 py-1 text-[11px] font-medium",
        tone,
      )}
    >
      {value || "â€”"}
    </span>
  );
}

export function SearchBox({ value, onChange, placeholder = "Search..." }) {
  return (
    <div className="relative">
      <Search
        size={16}
        className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-600"
      />
      <input
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        className="w-full rounded-xl border border-[#252a35] bg-[#10131a] py-2.5 pl-9 pr-3 text-sm text-slate-200 outline-none focus:border-violet-500/60"
      />
    </div>
  );
}

export function EmptyState({ title = "No records found", text }) {
  return (
    <div className="flex min-h-52 flex-col items-center justify-center p-8 text-center">
      <div className="mb-3 rounded-full border border-[#252a35] bg-[#151923] p-3">
        <Search size={18} className="text-slate-500" />
      </div>
      <h3 className="text-sm font-semibold text-slate-200">{title}</h3>
      {text && <p className="mt-1 max-w-sm text-xs text-slate-500">{text}</p>}
    </div>
  );
}

export function Skeleton({ className }) {
  return (
    <div
      className={cn(
        "animate-pulse rounded-xl bg-[#191d27]",
        className,
      )}
    />
  );
}

export function Modal({ open, title, onClose, children, wide = false }) {
  if (!open) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/65 p-4 backdrop-blur-sm">
      <div
        className={cn(
          "max-h-[90vh] w-full overflow-auto rounded-2xl border border-[#252a35] bg-[#10131a] shadow-2xl",
          wide ? "max-w-3xl" : "max-w-lg",
        )}
      >
        <div className="sticky top-0 flex items-center justify-between border-b border-[#252a35] bg-[#10131a] px-5 py-4">
          <h2 className="text-sm font-semibold text-white">{title}</h2>
          <button
            onClick={onClose}
            className="rounded-lg p-1.5 text-slate-500 hover:bg-white/[0.04] hover:text-slate-200"
          >
            <X size={17} />
          </button>
        </div>

        <div className="p-5">{children}</div>
      </div>
    </div>
  );
}
'@

Write-File "src/components/layouts/sidebar.jsx" @'
import {
  BarChart3,
  Boxes,
  CreditCard,
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
'@

Write-File "src/components/layouts/topbar.jsx" @'
import { Bell, Menu, RefreshCw } from "lucide-react";
import { useLocation } from "react-router-dom";
import { useAuth } from "../../contexts/auth-context";
import { Button } from "../ui";

const titles = {
  "/dashboard": ["Dashboard", "Live operational overview"],
  "/pos": ["POS / Billing", "Fast order and checkout workflow"],
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
'@

Write-File "src/components/layouts/app-layout.jsx" @'
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
'@

Write-File "src/pages/login.jsx" @'
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
'@

Write-File "src/pages/dashboard.jsx" @'
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

  const sales = data.bills.reduce(
    (sum, bill) => sum + Number(bill.total_amount || 0),
    0,
  );

  const paid = data.payments.reduce(
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
              data.bills.slice(0, 6).map((bill) => (
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
'@

Write-File "src/pages/resource-page.jsx" @'
import { useEffect, useMemo, useState } from "react";
import { Pencil, Plus, Trash2 } from "lucide-react";
import { Button, Card, EmptyState, Input, Modal, SearchBox, Select, Badge, Textarea } from "../components/ui";
import { services } from "../services/api";

const configs = {
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
    ],
    columns: ["customer_id", "customer_name", "phone", "email", "status"],
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
    load();
  }, [resource]);

  const filtered = rows.filter((row) =>
    Object.values(row)
      .join(" ")
      .toLowerCase()
      .includes(query.toLowerCase()),
  );

  function startCreate() {
    setEditing(null);
    setForm(emptyForm);
    setError("");
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
'@

Write-File "src/pages/tables.jsx" @'
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
'@

Write-File "src/pages/pos.jsx" @'
import { useEffect, useMemo, useState } from "react";
import { Minus, Plus, Search, ShoppingCart, Trash2 } from "lucide-react";
import { Button, Card, Input, Select } from "../components/ui";
import { services } from "../services/api";
import { useAuth } from "../contexts/auth-context";

const money = (value) =>
  new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
  }).format(Number(value || 0));

function nextId(prefix) {
  return `${prefix}${Date.now()}`;
}

export default function POS() {
  const { user } = useAuth();

  const [menu, setMenu] = useState([]);
  const [customers, setCustomers] = useState([]);
  const [tables, setTables] = useState([]);
  const [query, setQuery] = useState("");
  const [cart, setCart] = useState([]);
  const [customerId, setCustomerId] = useState("");
  const [tableId, setTableId] = useState("");
  const [orderType, setOrderType] = useState("Dine-In");
  const [paymentMethod, setPaymentMethod] = useState("Cash");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const [processing, setProcessing] = useState(false);
  const [completedBill, setCompletedBill] = useState(null);

  useEffect(() => {
    async function load() {
      const [menuResult, customerResult, tableResult] =
        await Promise.allSettled([
          services.menuItems.list(),
          services.customers.list(),
          services.tables.list(),
        ]);

      if (menuResult.status === "fulfilled") {
        setMenu(menuResult.value.menu_items || []);
      }

      if (customerResult.status === "fulfilled") {
        setCustomers(customerResult.value.customers || []);
      }

      if (tableResult.status === "fulfilled") {
        setTables(tableResult.value.restaurant_tables || []);
      }
    }

    load();
  }, []);

  const visibleMenu = menu.filter((item) => {
    const available = String(item.availability || "").toLowerCase() === "available";

    return (
      available &&
      `${item.item_name} ${item.category_id}`
        .toLowerCase()
        .includes(query.toLowerCase())
    );
  });

  function addItem(item) {
    setCart((current) => {
      const existing = current.find(
        (line) => line.menu_item_id === item.menu_item_id,
      );

      if (existing) {
        return current.map((line) =>
          line.menu_item_id === item.menu_item_id
            ? { ...line, quantity: line.quantity + 1 }
            : line,
        );
      }

      return [
        ...current,
        {
          menu_item_id: item.menu_item_id,
          item_name: item.item_name,
          price: Number(item.price || 0),
          quantity: 1,
        },
      ];
    });
  }

  function changeQty(id, amount) {
    setCart((current) =>
      current
        .map((line) =>
          line.menu_item_id === id
            ? { ...line, quantity: Math.max(0, line.quantity + amount) }
            : line,
        )
        .filter((line) => line.quantity > 0),
    );
  }

  const subtotal = useMemo(
    () =>
      cart.reduce(
        (sum, line) => sum + line.price * Number(line.quantity || 0),
        0,
      ),
    [cart],
  );

 async function checkout() {
  setError("");
  setMessage("");

  if (!cart.length) {
    setError("Add at least one menu item.");
    return;
  }

  if (!customerId || !tableId) {
    setError("Customer and table selection are required for billing.");
    return;
  }

  if (!user?.employee_id) {
    setError("Logged-in employee information is missing.");
    return;
  }

  setProcessing(true);

   try {
    const billId = nextId("BILL");
    const invoiceNumber = `INV-${new Date().getFullYear()}-${Date.now()}`;
    const billDate = new Date().toISOString().slice(0, 10);
    const orderTotal = Number(subtotal.toFixed(2));

    const selectedTable = tables.find(
      (table) => table.table_id === tableId,
    );

    if (
      !selectedTable ||
      String(selectedTable.status).toLowerCase() !== "available"
    ) {
      setError("Selected table is no longer available.");
      return;
    }

    await services.tables.updateStatus(tableId, "Occupied");

    setTables((current) =>
      current.map((table) =>
        table.table_id === tableId
          ? { ...table, status: "Occupied" }
          : table,
      ),
    );

    await services.bills.create({
      bill_id: billId,
      customer_id: customerId,
      employee_id: user.employee_id,
      table_id: tableId,
      invoice_number: invoiceNumber,
      bill_date: billDate,
      total_amount: orderTotal,
      status: "Completed",
    });

    for (const line of cart) {
      await services.billItems.create({
        bill_item_id: nextId("BITEM"),
        bill_id: billId,
        menu_item_id: line.menu_item_id,
        quantity: Number(line.quantity),
        unit_price: Number(line.price),
        subtotal: Number((line.price * line.quantity).toFixed(2)),
      });
    }

    await services.payments.create({
      payment_id: nextId("PAY"),
      bill_id: billId,
      payment_method: paymentMethod,
      payment_status: "Paid",
      payment_date: billDate,
      paid_amount: orderTotal,
    });
    
    await services.tables.updateStatus(tableId, "Available");

    setTables((current) =>
      current.map((table) =>
        table.table_id === tableId
          ? { ...table, status: "Available" }
          : table,
      ),
    );

    setCompletedBill({
      billId,
      invoiceNumber,
      billDate,
      total: orderTotal,
      paymentMethod,
      customerId,
      tableId,
      items: cart,
    });

    setMessage(
      `Bill ${invoiceNumber} created successfully. Payment received: ${money(
        orderTotal
      )}`
    );
  } catch (err) {
    setError(err.message || "Checkout failed.");
  } finally {
    setProcessing(false);
  }
}


function startNewOrder() {
  setCompletedBill(null);
  setMessage("");
  setError("");
  setCart([]);
  setCustomerId("");
  setTableId("");
  setOrderType("Dine-In");
  setPaymentMethod("Cash");
}

  return (
    <div className="grid gap-5 xl:grid-cols-[1fr_390px]">
      <section className="space-y-4">
        <div className="flex flex-col gap-3 md:flex-row">
          <div className="relative flex-1">
            <Search
              size={16}
              className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-600"
            />
            <input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search menu items..."
              className="w-full rounded-xl border border-[#252a35] bg-[#10131a] py-3 pl-9 pr-3 text-sm text-slate-200 outline-none focus:border-violet-500/60"
            />
          </div>
        </div>

        <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
          {visibleMenu.map((item) => (
            <button
              key={item.menu_item_id}
              onClick={() => addItem(item)}
              className="group rounded-2xl border border-[#252a35] bg-[#10131a] p-4 text-left transition hover:border-violet-500/30 hover:bg-[#151923]"
            >
              <div className="mb-3 flex items-start justify-between gap-3">
                <div className="rounded-xl bg-violet-500/10 p-2.5 text-violet-300">
                  <ShoppingCart size={16} />
                </div>
                <span className="text-sm font-semibold text-white">
                  {money(item.price)}
                </span>
              </div>

              <div className="text-sm font-medium text-slate-200">
                {item.item_name}
              </div>
              <div className="mt-1 text-[11px] text-slate-600">
                {item.category_id}
              </div>

              <div className="mt-4 flex items-center gap-1.5 text-[10px] font-medium text-emerald-400">
                <span className="h-1.5 w-1.5 rounded-full bg-emerald-400" />
                Available
              </div>
            </button>
          ))}
        </div>
      </section>

      <Card className="h-fit xl:sticky xl:top-6">
        <div className="flex items-center justify-between border-b border-[#252a35] px-5 py-4">
          <div>
            <h2 className="text-sm font-semibold text-white">Current order</h2>
            <p className="text-xs text-slate-600">{cart.length} line items</p>
          </div>
          <ShoppingCart size={17} className="text-violet-300" />
        </div>

        <div className="space-y-3 p-5">
          {!cart.length ? (
            <div className="rounded-xl border border-dashed border-[#252a35] p-8 text-center text-xs text-slate-600">
              Tap menu items to start an order.
            </div>
          ) : (
            cart.map((line) => (
              <div
                key={line.menu_item_id}
                className="rounded-xl border border-[#252a35] bg-[#151923] p-3"
              >
                <div className="flex items-start justify-between gap-3">
                  <div className="min-w-0">
                    <div className="truncate text-sm font-medium text-slate-200">
                      {line.item_name}
                    </div>
                    <div className="mt-1 text-xs text-slate-600">
                      {money(line.price)}
                    </div>
                  </div>

                  <button
                    onClick={() => changeQty(line.menu_item_id, -line.quantity)}
                    className="text-slate-600 hover:text-red-300"
                  >
                    <Trash2 size={14} />
                  </button>
                </div>

                <div className="mt-3 flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => changeQty(line.menu_item_id, -1)}
                      className="rounded-lg border border-[#252a35] p-1.5 text-slate-500"
                    >
                      <Minus size={13} />
                    </button>
                    <span className="w-6 text-center text-xs text-slate-200">
                      {line.quantity}
                    </span>
                    <button
                      onClick={() => changeQty(line.menu_item_id, 1)}
                      className="rounded-lg border border-[#252a35] p-1.5 text-slate-500"
                    >
                      <Plus size={13} />
                    </button>
                  </div>

                  <div className="text-sm font-semibold text-white">
                    {money(line.price * line.quantity)}
                  </div>
                </div>
              </div>
            ))
          )}

                    <div className="space-y-3 border-t border-[#252a35] pt-4">
            <Select
              label="Order Type"
              value={orderType}
              onChange={(e) => {
                setOrderType(e.target.value);
                if (e.target.value !== "Dine-In") {
                  setTableId("");
                }
                if (e.target.value === "Takeaway") {
                  setCustomerId("");
                }
              }}
              options={[
                { value: "Dine-In", label: "Dine-In" },
                { value: "Takeaway", label: "Takeaway" },
                { value: "Delivery", label: "Delivery" },
              ]}
            />

            <Select
              label="Customer"
              value={customerId}
              onChange={(e) => setCustomerId(e.target.value)}
              options={[
                { value: "", label: "Select customer" },
                ...customers.map((customer) => ({
                  value: customer.customer_id,
                  label: `${customer.customer_name} Â· ${customer.phone || "No phone"}`,
                })),
              ]}
            />

            <Select
              label="Table"
              value={tableId}
              onChange={(e) => setTableId(e.target.value)}
              options={[
                { value: "", label: "Select table" },
                ...tables
                  .filter(
                    (table) =>
                      String(table.status).toLowerCase() === "available",
                  )
                  .map((table) => ({
                    value: table.table_id,
                    label: `${table.table_number} Â· ${table.capacity} seats`,
                  })),
              ]}
            />

            <Select
              label="Payment method"
              value={paymentMethod}
              onChange={(e) => setPaymentMethod(e.target.value)}
              options={[
                { value: "Cash", label: "Cash" },
                { value: "UPI", label: "UPI" },
                { value: "Card", label: "Card" },
              ]}
            />
          </div>

          <div className="flex items-center justify-between pt-2">
            <span className="text-sm text-slate-500">Total</span>
            <span className="text-2xl font-semibold text-white">
              {money(subtotal)}
            </span>
          </div>

          {error && (
            <div className="rounded-xl border border-red-500/20 bg-red-500/10 px-3 py-2.5 text-xs text-red-300">
              {error}
            </div>
          )}

          {message && (
            <div className="rounded-xl border border-emerald-500/20 bg-emerald-500/10 px-3 py-2.5 text-xs text-emerald-300">
              {message}
            </div>
          )}

          {completedBill ? (
  <div className="space-y-3">
    <div className="rounded-xl border border-emerald-500/20 bg-emerald-500/10 px-3 py-3">
      <div className="text-sm font-semibold text-emerald-300">
        Payment Completed
      </div>

      <div className="mt-1 text-xs text-slate-300">
        Invoice: {completedBill.invoiceNumber}
      </div>

      <div className="mt-3 flex items-center justify-between">
        <span className="text-sm text-slate-400">Paid</span>
        <span className="text-lg font-semibold text-white">
          {money(completedBill.total)}
        </span>
      </div>

      <div className="mt-1 text-xs text-slate-400">
        {completedBill.paymentMethod} Â· {completedBill.billDate}
      </div>
    </div>

    <Button
      className="w-full"
      onClick={startNewOrder}
    >
      New Order
    </Button>
  </div>
) : (
  <Button
    className="w-full"
    loading={processing}
    onClick={checkout}
    disabled={!cart.length}
  >
    Complete payment Â· {money(subtotal)}
  </Button>
)}
        </div>
      </Card>
    </div>
  );
}
'@

Write-File "src/pages/settings.jsx" @'
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
'@

Write-File "src/App.jsx" @'
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
'@

Write-File "src/main.jsx" @'
import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import { AuthProvider } from "./contexts/auth-context";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <App />
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>,
);
'@

Write-File "src/App.css" @'
/* SaruPOS uses Tailwind 4 utilities and src/index.css for global styling. */
'@

Write-Host ""
Write-Host "============================================"
Write-Host " SARUPOS FRONTEND PACK INSTALLED"
Write-Host "============================================"
Write-Host ""
Write-Host "Run:"
Write-Host "  npm run build"
Write-Host ""
Write-Host "Then:"
Write-Host "  npm run dev"
Write-Host ""

Write-Host "Done."






