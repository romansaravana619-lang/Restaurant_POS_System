# ============================================================
# SARU SYSTEMS
# API DESIGN
# ============================================================

## Document Information

| Field | Details |
|--------|---------|
| Document ID | SS-POS-SD-004 |
| Document Name | API Design |
| Product | Saru POS |
| Product Code | SS-POS-001 |
| Version | 1.0 |
| Status | Approved |

---

# 1. Purpose

This document defines the API architecture for the Saru POS Version 1.0 application.

The APIs act as the communication layer between the HTML frontend, Flask backend, Python business logic, and SQLite database.

---

# 2. API Architecture

Frontend (HTML)

↓

Flask Routes (API)

↓

Python Business Logic

↓

SQLite Database

↓

JSON Response

↓

Frontend

---

# 3. API Objectives

The API layer is responsible for:

- Processing client requests
- Validating input data
- Executing business logic
- Reading and writing database records
- Returning appropriate responses
- Maintaining application security

---

# 4. API Modules

| Module | Description |
|----------|---------------------------|
| Authentication | User Login & Logout |
| Dashboard | Dashboard Summary |
| Billing | Billing Operations |
| Menu | Menu Management |
| Customer | Customer Management |
| Inventory | Inventory View |
| Settings | Application Settings |

---

# 5. API Communication Standard

| Item | Standard |
|------|----------|
| Protocol | HTTP |
| Backend Framework | Flask |
| Response Format | JSON |
| Database | SQLite |
| Architecture | REST-style |

---

# 6. HTTP Methods

| Method | Purpose |
|----------|-------------------------|
| GET | Retrieve Data |
| POST | Create New Data |
| PUT | Update Existing Data |
| DELETE | Delete Records (Future Use) |

Version 1 primarily uses GET and POST.

---

# 7. API Endpoints

## Authentication

| Method | Endpoint | Purpose |
|----------|------------------|----------------|
| POST | /login | User Login |
| GET | /logout | User Logout |
| GET | /dashboard | Dashboard Access |

---

## Billing

| Method | Endpoint | Purpose |
|----------|-----------------------------|----------------------------|
| POST | /billing/create | Create Bill |
| POST | /billing/add-item | Add Item to Bill |
| POST | /billing/remove-item | Remove Bill Item |
| POST | /billing/payment | Process Payment |
| GET | /billing/history | Billing History |
| GET | /billing/invoice/<bill_id> | Generate Invoice |

---

## Menu

| Method | Endpoint | Purpose |
|----------|------------------------------|--------------------|
| GET | /menu/list | View Menu |
| POST | /menu/add | Add Menu Item |
| PUT | /menu/update/<menu_item_id> | Update Menu Item |
| DELETE | /menu/delete/<menu_item_id> | Delete Menu Item |

---

## Customer

| Method | Endpoint | Purpose |
|----------|----------------|----------------|
| GET | /customer/list | View Customers |
| POST | /customer/add | Add Customer |

---

## Inventory

| Method | Endpoint | Purpose |
|----------|-----------------|----------------|
| GET | /inventory/list | View Inventory |

---

## Settings

| Method | Endpoint | Purpose |
|----------|--------------------|----------------|
| GET | /settings | View Settings |
| POST | /settings/update | Update Settings |

---

# 8. Validation Rules

Every API validates:

- Required fields
- Empty values
- Duplicate records
- Invalid data
- Database existence
- Business rules

Examples:

- Username cannot be empty.
- Price must be greater than zero.
- Quantity must be greater than zero.
- Invoice number must be unique.

---

# 9. Standard Response Format

## Success Response

```json
{
    "status": "success",
    "message": "Operation Completed Successfully"
}
```

## Error Response

```json
{
    "status": "error",
    "message": "Unable to Process Request"
}
```

---

# 10. HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 201 | Resource Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Internal Server Error |

---

# 11. Error Handling

The API follows a centralized error handling strategy.

Rules:

- Validate all inputs.
- Return user-friendly error messages.
- Do not expose database or Python exceptions.
- Log internal errors for debugging.

---

# 12. Version Scope

## Version 1.0

- Authentication APIs
- Dashboard APIs
- Billing APIs
- Menu APIs
- Customer APIs
- Inventory View API
- Settings APIs

## Version 2.0

- Employee APIs
- Supplier APIs
- Table Management APIs
- GST
- Coupons
- Reports

## Version 3.0

- Multi-Branch APIs
- Cloud Synchronization
- Online Ordering
- Loyalty Program
- Analytics APIs

---

# 13. API Statistics

| Item | Count |
|------|------:|
| Total Modules | 6 |
| Total APIs | 18 |
| HTTP Methods | 4 |
| Response Format | JSON |
| Database | SQLite |

---

# 14. Approval

The Saru POS Version 1.0 API Design has been reviewed and approved for backend implementation.

**Status:** ✅ Approved

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0 | 01 August 2026 | Initial Release |

---

# Approved By

**Founder**

**Saravana Kumar**

---

# End of Document