# ===================================================================
# SARU SYSTEMS
# ENTITY RELATIONSHIP (ER) DOCUMENT
# ===================================================================

# Document Information

| Field | Details |
|--------|---------|
| Document ID | SS-POS-ER-001 |
| Document Name | Entity Design |
| Product Name | Saru POS |
| Product Code | SS-POS-001 |
| Version | 1.0 |
| Status | Approved |
| Owner | Saravana Kumar |
| Created Date | 31 July 2026 |
| Last Updated | 31 July 2026 |

---

# Purpose

This document defines all database entities (tables) used in the Saru POS system. It explains the purpose, responsibilities, standard columns, keys, constraints, business rules, and design standards for every entity.

This document serves as the foundation for the ER Diagram and Database Design.

---

# Entity Overview

| Entity | Purpose |
|----------|---------|
| users | Stores login accounts and user roles |
| employees | Stores employee information |
| customers | Stores customer records |
| suppliers | Stores supplier information |
| categories | Stores menu categories |
| menu_items | Stores restaurant menu items |
| inventory_items | Stores inventory stock information |
| restaurant_tables | Stores restaurant table details |
| bills | Stores billing transactions |
| bill_items | Stores products inside each bill |
| payments | Stores payment transactions |
| settings | Stores application configuration |

---

# Entity Specifications

## 1. Users

### Purpose

Stores login credentials and user roles.

### Responsibilities

- User authentication
- User authorization
- Role management

### Standard Columns

- user_id
- employee_id
- username
- password_hash
- role
- last_login
- is_active
- created_at
- updated_at

---

## 2. Employees

### Purpose

Stores employee information.

### Responsibilities

- Employee records
- Contact details
- Employment details

### Standard Columns

- employee_id
- employee_code
- employee_name
- phone_number
- email
- designation
- joining_date
- salary
- address
- is_active
- created_at
- updated_at

---

## 3. Customers

### Purpose

Stores customer information.

### Responsibilities

- Customer profile
- Purchase history
- Contact details

### Standard Columns

- customer_id
- customer_name
- phone_number
- email
- address
- created_at
- updated_at

---

## 4. Suppliers

### Purpose

Stores supplier information.

### Responsibilities

- Supplier records
- Contact management

### Standard Columns

- supplier_id
- supplier_name
- contact_person
- phone_number
- email
- address
- created_at
- updated_at

---

## 5. Categories

### Purpose

Organizes menu items into categories.

### Responsibilities

- Category management
- Product grouping

### Standard Columns

- category_id
- category_name
- description
- is_active
- created_at
- updated_at

---

## 6. Menu Items

### Purpose

Stores restaurant menu items.

### Responsibilities

- Product details
- Pricing
- Availability

### Standard Columns

- menu_item_id
- category_id
- item_name
- description
- price
- availability
- created_at
- updated_at

---

## 7. Inventory Items

### Purpose

Stores inventory stock information.

### Responsibilities

- Stock monitoring
- Quantity tracking

### Standard Columns

- inventory_id
- supplier_id
- item_name
- unit
- quantity
- minimum_stock
- created_at
- updated_at

---

## 8. Restaurant Tables

### Purpose

Stores restaurant table information.

### Responsibilities

- Table allocation
- Occupancy tracking

### Standard Columns

- table_id
- table_number
- capacity
- status
- created_at
- updated_at

---

## 9. Bills

### Purpose

Stores billing transactions.

### Responsibilities

- Sales records
- Billing history

### Standard Columns

- bill_id
- bill_number
- customer_id
- employee_id
- table_id
- bill_date
- subtotal
- discount
- total_amount
- bill_status
- created_at
- updated_at

---

## 10. Bill Items

### Purpose

Stores items belonging to each bill.

### Responsibilities

- Product details
- Quantity
- Pricing

### Standard Columns

- bill_item_id
- bill_id
- menu_item_id
- quantity
- unit_price
- total_price
- created_at

---

## 11. Payments

### Purpose

Stores payment transactions.

### Responsibilities

- Payment records
- Payment method tracking

### Standard Columns

- payment_id
- bill_id
- payment_method
- payment_amount
- payment_status
- transaction_reference
- payment_date
- created_at

---

## 12. Settings

### Purpose

Stores application configuration.

### Responsibilities

- Restaurant settings
- System configuration

### Standard Columns

- setting_id
- restaurant_name
- restaurant_address
- phone_number
- email
- currency
- created_at
- updated_at

---

# Database Standards

## Primary Keys

Every entity contains one unique Primary Key.

## Foreign Keys

Entities are connected using Foreign Keys to maintain referential integrity.

## Naming Convention

- Use snake_case.
- Table names use lowercase.
- Primary Keys end with `_id`.
- Foreign Keys match the referenced Primary Key name.

Example:

customer_id

employee_id

bill_id

---

# Common Audit Fields

Most entities include:

- created_at
- updated_at

These fields help track record creation and modification.

---

# Common Constraints

- Primary Keys must be unique.
- Mandatory fields cannot be NULL.
- Usernames must be unique.
- Bill numbers must be unique.
- Table numbers must be unique.

---

# Business Rules

- Every user belongs to one employee.
- Every menu item belongs to one category.
- Every bill belongs to one employee.
- Every bill belongs to one customer.
- Every payment belongs to one bill.
- Inventory quantity cannot become negative.
- Soft delete should be used wherever possible.

---

# Version Scope

## Version 1.0

Included:

- Authentication
- Billing
- Customers
- Employees
- Inventory
- Suppliers
- Reports
- Settings
- Multiple Payment Methods
- Table Management

Future Versions:

- Kitchen Order Token (KOT)
- GST Automation
- Offers & Discounts
- Loyalty Program
- Multi-Branch Support
- Cloud Database
- AI Analytics

---

# Related Documents

Previous

- ER-000 ER Diagram Index

Next

- ER-002 Relationship Design
- ER-003 Final ER Diagram
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