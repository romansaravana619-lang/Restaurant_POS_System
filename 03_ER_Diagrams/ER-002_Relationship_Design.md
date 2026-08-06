# ===================================================================
# SARU SYSTEMS
# ENTITY RELATIONSHIP (ER) DOCUMENT
# ===================================================================

# Document Information

| Field | Details |
|--------|---------|
| Document ID | SS-POS-ER-002 |
| Document Name | Relationship Design |
| Product Name | Saru POS |
| Product Code | SS-POS-001 |
| Version | 1.0 |
| Status | Approved |
| Owner | Saravana Kumar |
| Created Date | 31 July 2026 |
| Last Updated | 31 July 2026 |

---

# Purpose

This document defines the relationships between all entities in the Saru POS database.

It explains how tables interact with each other, identifies Primary Key (PK) and Foreign Key (FK) mappings, enforces referential integrity, and establishes business rules that maintain database consistency.

This document serves as the foundation for the Final ER Diagram and Database Design.

---

# Relationship Fundamentals

The Saru POS database follows the following relationship types:

- One-to-One (1:1)
- One-to-Many (1:N)

Version 1.0 does not contain any Many-to-Many (N:N) relationships.

---

# Relationship Matrix

| Parent Entity | Child Entity | Relationship | Foreign Key |
|---------------|--------------|--------------|-------------|
| Employees | Users | 1 : 1 | employee_id |
| Categories | Menu Items | 1 : N | category_id |
| Suppliers | Inventory Items | 1 : N | supplier_id |
| Customers | Bills | 1 : N | customer_id |
| Employees | Bills | 1 : N | employee_id |
| Restaurant Tables | Bills | 1 : N | table_id |
| Bills | Bill Items | 1 : N | bill_id |
| Menu Items | Bill Items | 1 : N | menu_item_id |
| Bills | Payments | 1 : 1 *(Version 1.0)* | bill_id |

---

# Relationship Specifications

## 1. Employees → Users

Relationship

1 : 1

Purpose

Every login account belongs to exactly one employee.

Foreign Key

users.employee_id

---

## 2. Categories → Menu Items

Relationship

1 : N

Purpose

Each menu item belongs to one category.

Foreign Key

menu_items.category_id

---

## 3. Suppliers → Inventory Items

Relationship

1 : N

Purpose

Each inventory item belongs to one supplier.

Foreign Key

inventory_items.supplier_id

---

## 4. Customers → Bills

Relationship

1 : N

Purpose

A customer may have multiple billing transactions.

Foreign Key

bills.customer_id

---

## 5. Employees → Bills

Relationship

1 : N

Purpose

Each bill records the employee responsible for creating it.

Foreign Key

bills.employee_id

---

## 6. Restaurant Tables → Bills

Relationship

1 : N

Purpose

A restaurant table can generate multiple bills over time.

Foreign Key

bills.table_id

---

## 7. Bills → Bill Items

Relationship

1 : N

Purpose

Every bill contains one or more ordered menu items.

Foreign Key

bill_items.bill_id

---

## 8. Menu Items → Bill Items

Relationship

1 : N

Purpose

A menu item can appear in many different bills.

Foreign Key

bill_items.menu_item_id

---

## 9. Bills → Payments

Relationship

1 : 1

Purpose

Each completed bill has one payment transaction in Version 1.0.

Foreign Key

payments.bill_id

Future Note

Version 2.0 may support split payments, changing this relationship to 1:N.

---

# Central Relationship Flow

```
Employees
      │
      ▼
Users

Categories
      │
      ▼
Menu Items
      │
      ▼
Bill Items
      ▲
      │
Bills ─────────────► Payments
 ▲   ▲
 │   │
 │   └──────────── Restaurant Tables
 │
Customers

Suppliers
      │
      ▼
Inventory Items
```

---

# Referential Integrity Rules

The database shall enforce the following rules:

- Every Foreign Key must reference a valid Primary Key.
- Parent records must exist before child records.
- Orphan records are not allowed.
- Primary Keys must never be modified.
- Important business records should use Soft Delete instead of permanent deletion.

---

# Business Rules

The following business rules apply:

- Every user belongs to one employee.
- Every menu item belongs to one category.
- Every bill belongs to one customer.
- Every bill belongs to one employee.
- Every bill contains at least one bill item.
- Every completed bill has one payment.
- Inventory quantity cannot become negative.
- Restaurant table numbers must be unique.

---

# Relationship Validation

The relationship model has been reviewed and validated.

Validation Results:

- No circular dependencies
- No orphan relationships
- No duplicate mappings
- Proper parent-child hierarchy
- Future scalability supported

Status:

Approved

---

# Database Quality Checklist

| Item | Status |
|------|--------|
| Parent Entities Defined | ✅ |
| Child Entities Defined | ✅ |
| Relationship Types Identified | ✅ |
| Foreign Keys Mapped | ✅ |
| Referential Integrity Planned | ✅ |
| Business Rules Defined | ✅ |
| Future Expansion Considered | ✅ |

---

# Future Relationship Expansion

## Version 2.0

- Kitchen Order Token (KOT)
- GST & Tax Relationships
- Offers & Coupons
- Recipe Management

## Version 3.0

- Multi-Branch Relationships
- Cloud Synchronization
- Online Order Relationships
- AI Analytics Data

---

# Related Documents

Previous

- ER-000 – ER Diagram Index
- ER-001 – Entity Design

Next

- ER-003 – Final ER Diagram
- SD-003 – Database Design

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