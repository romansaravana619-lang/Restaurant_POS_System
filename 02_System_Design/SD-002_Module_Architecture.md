# ===================================================================
# SARU SYSTEMS
# SYSTEM DESIGN DOCUMENT
# ===================================================================

# Document Information

| Field | Details |
|--------|---------|
| Document ID | SS-POS-SD-002 |
| Document Name | Module Architecture |
| Product Name | Saru POS |
| Product Code | SS-POS-001 |
| Version | 1.0 |
| Status | Planning |
| Owner | Saravana Kumar |
| Created Date | 31 July 2026 |
| Last Updated | 31 July 2026 |

---

# Purpose

This document defines the functional modules of the Saru POS system, their responsibilities, interactions, and access permissions. It acts as the blueprint for application development and module-level implementation.

---

# Module Overview

Saru POS Version 1.0 consists of the following core modules:

1. Authentication
2. Dashboard
3. Billing
4. Menu Management
5. Category Management
6. Customer Management
7. Inventory Management
8. Supplier Management
9. Employee Management
10. Reports
11. User Management
12. Table Management
13. Settings
14. Backup & Restore

---

# Module Architecture Diagram

                    Saru POS
                        │
 ┌──────────────────────┼──────────────────────┐
 │                      │                      │
 ▼                      ▼                      ▼
Authentication      Dashboard          User Management
                           │
      ┌────────────────────┼────────────────────┐
      ▼                    ▼                    ▼
 Billing            Menu Management      Customer Management
      │                    │
      ▼                    ▼
Inventory         Category Management
      │
      ▼
Supplier Management
      │
      ▼
Employee Management
      │
      ▼
Reports
      │
      ▼
Settings
      │
      ▼
Backup & Restore

---

# Module Details

## 1. Authentication

Purpose

- User Login
- Logout
- Role Verification
- Session Management

Users

- Owner
- Manager
- Cashier

---

## 2. Dashboard

Purpose

- Daily Sales Summary
- Today's Bills
- Low Stock Summary
- Quick Navigation
- Business Overview

---

## 3. Billing

Purpose

- Create Bill
- Add Menu Items
- Update Quantity
- Apply Discount
- Select Payment Method
- Generate Invoice
- Save Billing History

Payment Methods

- Cash
- UPI
- Card

---

## 4. Menu Management

Purpose

- Add Menu Item
- Edit Menu Item
- Delete Menu Item
- Price Management

---

## 5. Category Management

Purpose

- Create Category
- Update Category
- Delete Category

Examples

- Starters
- Main Course
- Beverages
- Desserts

---

## 6. Customer Management

Purpose

- Add Customer
- Search Customer
- Customer Purchase History

---

## 7. Inventory Management

Purpose

- Add Stock
- Update Stock
- View Stock
- Low Stock Alert

Inventory automatically decreases after successful billing.

---

## 8. Supplier Management

Purpose

- Add Supplier
- Update Supplier
- Supplier Contact Information

---

## 9. Employee Management

Purpose

- Employee Records
- Employee Details
- Employee Status

---

## 10. Reports

Purpose

- Daily Sales Report
- Weekly Sales Report
- Monthly Sales Report
- Inventory Report
- Employee Report

---

## 11. User Management

Purpose

- Create Users
- Assign Roles
- Reset Password
- Enable / Disable Users

---

## 12. Table Management

Purpose

- Create Restaurant Tables
- View Table Status
- Assign Bill to Table
- Mark Table as Occupied / Available

---

## 13. Settings

Purpose

- Restaurant Information
- Currency
- Receipt Settings
- Application Preferences

---

## 14. Backup & Restore

Purpose

- Backup Database
- Restore Database
- Backup History

---

# User Access Matrix

| Module | Owner | Manager | Cashier |
|---------|:-----:|:-------:|:--------:|
| Authentication | ✅ | ✅ | ✅ |
| Dashboard | ✅ | ✅ | ✅ |
| Billing | ✅ | ✅ | ✅ |
| Menu Management | ✅ | ✅ | ❌ |
| Category Management | ✅ | ✅ | ❌ |
| Customer Management | ✅ | ✅ | ✅ |
| Inventory | ✅ | ✅ | ❌ |
| Supplier | ✅ | ✅ | ❌ |
| Employee | ✅ | ✅ | ❌ |
| Reports | ✅ | ✅ | ❌ |
| User Management | ✅ | ❌ | ❌ |
| Table Management | ✅ | ✅ | ✅ |
| Settings | ✅ | ❌ | ❌ |
| Backup & Restore | ✅ | ❌ | ❌ |

---

# Module Interaction

Authentication
        │
        ▼
Dashboard
        │
        ├─────────────┐
        ▼             ▼
Billing         Menu Management
        │             │
        ▼             ▼
Customer     Category Management
        │
        ▼
Inventory
        │
        ▼
Supplier
        │
        ▼
Reports

---

# Design Principles

The module architecture follows:

- Modular Development
- High Cohesion
- Loose Coupling
- Role-Based Access Control (RBAC)
- Reusable Components
- Easy Maintenance
- Future Scalability

---

# Version 1.0 Scope

Included

- Authentication
- Billing
- Inventory
- Customers
- Employees
- Reports
- Table Management
- Multiple Payment Methods

Deferred to Future Versions

- Kitchen Order Token (KOT)
- GST & Tax Automation
- Offers & Coupons
- Loyalty Program
- Multi-Branch Support
- Cloud Synchronization
- Mobile Application
- Swiggy / Zomato Integration

---

# Related Documents

Previous

- SD-000 System Profile
- SD-001 System Architecture

Next

- SD-003 Database Design

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0 | 31 July 2026 | Initial Release |

---

# Approved By

Founder

Saravana Kumar

---

# End of Document