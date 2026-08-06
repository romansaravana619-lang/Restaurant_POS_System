# ============================================================
# SARU SYSTEMS
# DATABASE SCHEMA
# ============================================================

## Document Information

| Field | Details |
|--------|---------|
| Document ID | SS-POS-DB-002 |
| Document Name | Database Schema |
| Product | Saru POS |
| Product Code | SS-POS-001 |
| Version | 1.0 |
| Status | Approved |

---

# 1. Purpose

This document defines the complete database schema for the Saru POS Version 1.0 application.

It specifies the database tables, relationships, primary keys, foreign keys, constraints, and naming standards required for implementation.

---

# 2. Database Overview

Database Name

restaurant_pos.db

Database Engine

SQLite 3

Total Tables

11

---

# 3. Database Tables

| No | Table Name | Purpose |
|----|------------|---------|
| 1 | users | Login Accounts |
| 2 | employees | Employee Information |
| 3 | customers | Customer Details |
| 4 | suppliers | Supplier Information |
| 5 | categories | Menu Categories |
| 6 | menu_items | Restaurant Menu |
| 7 | bills | Billing Header |
| 8 | bill_items | Billing Line Items |
| 9 | payments | Payment Records |
|10 | restaurant_tables | Restaurant Tables |
|11 | inventory_items | Inventory Management |

---

# 4. Primary Keys

| Table | Primary Key |
|--------|-------------|
| users | user_id |
| employees | employee_id |
| customers | customer_id |
| suppliers | supplier_id |
| categories | category_id |
| menu_items | menu_item_id |
| bills | bill_id |
| bill_items | bill_item_id |
| payments | payment_id |
| restaurant_tables | table_id |
| inventory_items | inventory_id |

---

# 5. Foreign Keys

| Table | Foreign Key | References |
|--------|-------------|------------|
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

# 6. Relationships

- Employees → Users (1:1)
- Categories → Menu Items (1:N)
- Suppliers → Inventory Items (1:N)
- Customers → Bills (1:N)
- Employees → Bills (1:N)
- Restaurant Tables → Bills (1:N)
- Bills → Bill Items (1:N)
- Menu Items → Bill Items (1:N)
- Bills → Payments (1:1)

---

# 7. Naming Standards

- Table Names → snake_case
- Column Names → snake_case
- Primary Keys → table_name_id
- Foreign Keys → referenced_table_id

---

# 8. Constraints

- Every table has a Primary Key.
- Foreign Keys maintain referential integrity.
- Primary Keys are unique.
- Required fields use NOT NULL.
- Unique fields use UNIQUE constraint where applicable.

---

# 9. Version Scope

## Version 1.0

- 11 Tables
- Primary Keys
- Foreign Keys
- Basic Constraints

## Version 2.0

- Views
- Triggers
- Indexes
- Audit Tables

## Version 3.0

- Stored Procedures (Migration)
- Replication
- Cloud Database Support

---

# 10. Approval

The database schema for Saru POS Version 1.0 has been reviewed and approved for implementation.

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