# ============================================================
# SARU SYSTEMS
# DATABASE DESIGN
# ============================================================

## Document Information

| Field | Details |
|--------|---------|
| Document ID | SS-POS-SD-003 |
| Document Name | Database Design |
| Product | Saru POS |
| Product Code | SS-POS-001 |
| Database | SQLite |
| Database Name | restaurant_pos.db |
| Version | 1.0 |
| Status | Approved |

---

# 1. Purpose

This document defines the complete database architecture for the Saru POS Version 1.0 system.

It specifies the database structure, table design, relationships, standards, constraints, naming conventions, and future scalability strategy. This document serves as the foundation for implementing the SQLite database and backend application.

---

# 2. Database Overview

| Item | Details |
|------|---------|
| Database Engine | SQLite |
| Database Name | restaurant_pos.db |
| Product | Saru POS |
| Version | 1.0 |
| Total Tables | 12 |

---

# 3. Database Objectives

The database is designed to:

- Store restaurant business data securely.
- Support billing and payment operations.
- Maintain data consistency.
- Provide fast transaction processing.
- Support reporting and analytics.
- Allow future feature expansion.

---

# 4. Database Modules

| Module | Tables |
|---------|--------|
| Authentication | users, employees |
| Customer Management | customers |
| Supplier Management | suppliers |
| Menu Management | categories, menu_items |
| Inventory Management | inventory_items |
| Restaurant Management | restaurant_tables |
| Billing | bills, bill_items |
| Payment Management | payments |
| System Configuration | settings |

---

# 5. Database Tables

| No | Table Name | Purpose |
|----|------------|---------|
| 1 | users | Stores login credentials |
| 2 | employees | Stores employee information |
| 3 | customers | Stores customer information |
| 4 | suppliers | Stores supplier information |
| 5 | categories | Stores menu categories |
| 6 | menu_items | Stores food menu |
| 7 | inventory_items | Stores inventory details |
| 8 | restaurant_tables | Stores restaurant tables |
| 9 | bills | Stores billing transactions |
| 10 | bill_items | Stores bill item details |
| 11 | payments | Stores payment information |
| 12 | settings | Stores application settings |

---

# 6. Primary Key Standard

- Every table contains one Primary Key.
- Primary Keys use INTEGER AUTOINCREMENT.
- Primary Keys are unique and NOT NULL.

Examples:

- user_id
- employee_id
- customer_id
- bill_id

---

# 7. Foreign Key Relationships

| Child Table | Foreign Key | Parent Table |
|--------------|-------------|--------------|
| users | employee_id | employees |
| menu_items | category_id | categories |
| inventory_items | supplier_id | suppliers |
| bills | customer_id | customers |
| bills | employee_id | employees |
| bills | table_id | restaurant_tables |
| bill_items | bill_id | bills |
| bill_items | menu_item_id | menu_items |
| payments | bill_id | bills |

---

# 8. Business Codes

| Entity | Format |
|---------|---------|
| Employee | EMP001 |
| Customer | CUS001 |
| Menu Item | MENU001 |
| Inventory | INVITEM001 |
| Invoice | INV-000001 |
| Table | T01 |

---

# 9. Data Standards

## Mandatory Fields

- Username
- Password
- Employee Name
- Menu Item Name
- Invoice Number
- Bill Date
- Total Amount

## Optional Fields

- Email
- Address
- Receipt Footer

---

# 10. Constraints

Implemented Constraints:

- Primary Key
- Foreign Key
- NOT NULL
- UNIQUE
- CHECK
- DEFAULT

Validation Rules:

- Username must be unique.
- Invoice Number must be unique.
- Menu Price > 0
- Quantity >= 0
- Total Amount >= 0

---

# 11. Naming Standards

## Database

restaurant_pos.db

## Tables

snake_case

Examples:

- menu_items
- bill_items
- restaurant_tables

## Columns

snake_case

Examples:

- employee_name
- total_amount
- payment_method

---

# 12. Version Scope

## Version 1.0

- Authentication
- Employees
- Customers
- Menu
- Inventory
- Billing
- Payments
- Restaurant Tables
- Settings

## Version 2.0

- Soft Delete
- GST
- Coupons
- Kitchen Order Ticket (KOT)
- Attendance
- Stock Alerts

## Version 3.0

- Multi Branch
- Cloud Sync
- Online Ordering
- Loyalty Program
- AI Reports

---

# 13. Future Scalability

The database architecture is designed for:

- Modular expansion
- Easy migration
- Performance optimization
- Cloud migration
- Multi-branch support

---

# 14. Database Statistics

| Item | Count |
|------|------:|
| Total Tables | 12 |
| Primary Keys | 12 |
| Foreign Keys | 9 |
| Database Engine | SQLite |
| Database Version | 1.0 |

---

# 15. Approval

The Saru POS Version 1.0 Database Design has been reviewed and approved for implementation.

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