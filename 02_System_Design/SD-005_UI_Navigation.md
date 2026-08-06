# ============================================================
# SARU SYSTEMS
# UI NAVIGATION DESIGN
# ============================================================

## Document Information

| Field | Details |
|--------|---------|
| Document ID | SS-POS-SD-005 |
| Document Name | UI Navigation Design |
| Product | Saru POS |
| Product Code | SS-POS-001 |
| Version | 1.0 |
| Status | Approved |

---

# 1. Purpose

This document defines the user interface navigation flow for the Saru POS Version 1.0 application.

It specifies how users move between screens and how each module is connected within the application.

---

# 2. Navigation Objectives

The UI navigation is designed to provide:

- Simple user experience
- Fast access to major functions
- Logical screen transitions
- Consistent navigation
- Easy learning for restaurant staff

---

# 3. Navigation Architecture

Login

↓

Dashboard

├── Billing

├── Menu Management

├── Customer Management

├── Inventory

├── Settings

└── Logout

---

# 4. Application Screens

| No | Screen | Purpose |
|----|--------|---------|
| 1 | Login | User Authentication |
| 2 | Dashboard | Main Navigation |
| 3 | Billing | Generate Bills |
| 4 | Invoice Preview | Preview & Print Invoice |
| 5 | Menu Management | Manage Menu Items |
| 6 | Customer Management | Add & View Customers |
| 7 | Inventory | View Inventory |
| 8 | Settings | Application Configuration |

---

# 5. Screen Navigation Flow

## Login

↓

Dashboard

↓

Select Module

↓

Perform Operation

↓

Return to Dashboard

↓

Logout

---

# 6. Dashboard Navigation

The Dashboard serves as the central navigation hub.

Available Modules:

- Billing
- Menu Management
- Customer Management
- Inventory
- Settings
- Logout

---

# 7. Billing Navigation

Dashboard

↓

Billing

↓

Create Bill

↓

Add Menu Items

↓

Preview Invoice

↓

Payment

↓

Generate Invoice

↓

Return to Dashboard

---

# 8. Menu Navigation

Dashboard

↓

Menu Management

↓

View Menu

↓

Add Menu Item

↓

Update Menu Item

↓

Delete Menu Item

↓

Return to Dashboard

---

# 9. Customer Navigation

Dashboard

↓

Customer Management

↓

View Customers

↓

Add Customer

↓

Return to Dashboard

---

# 10. Inventory Navigation

Dashboard

↓

Inventory

↓

View Stock

↓

Return to Dashboard

---

# 11. Settings Navigation

Dashboard

↓

Settings

↓

Update Restaurant Information

↓

Save Settings

↓

Return to Dashboard

---

# 12. Navigation Rules

- Login is required before accessing any module.
- Dashboard is the main entry point after login.
- Users can return to the Dashboard from any module.
- Logout ends the current session and redirects to the Login page.
- Unauthorized users cannot access protected pages.

---

# 13. Version Scope

## Version 1.0

- Login
- Dashboard
- Billing
- Invoice Preview
- Menu Management
- Customer Management
- Inventory
- Settings

## Version 2.0

- Employee Management
- Supplier Management
- Reports
- Table Management

## Version 3.0

- Multi-Branch Dashboard
- Online Orders
- Analytics Dashboard
- Customer Loyalty

---

# 14. Navigation Statistics

| Item | Count |
|------|------:|
| Total Screens | 8 |
| Main Navigation Hub | 1 |
| Core Modules | 5 |
| Authentication Screens | 1 |

---

# 15. Approval

The UI Navigation Design for Saru POS Version 1.0 has been reviewed and approved for frontend implementation.

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