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

  checkout: (body) => api.post("/checkout", body),

  diningSessions: {
    create: (body) => api.post("/dining-sessions", body),
    activeByCustomer: (id) => api.get(`/customers/${id}/active-dining-session`),
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
