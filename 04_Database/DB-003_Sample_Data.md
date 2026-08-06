# ============================================================
# SARU SYSTEMS
# SAMPLE DATA
# ============================================================

## Document Information

| Field | Details |
|--------|---------|
| Document ID | SS-POS-DB-003 |
| Document Name | Sample Data |
| Product | Saru POS |
| Product Code | SS-POS-001 |
| Version | 1.0 |
| Status | Approved |

---

# 1. Purpose

This document defines the default sample data required for the Saru POS Version 1.0 application.

The sample data is used for initial system setup, development, testing, and demonstration purposes.

---

# 2. Objectives

The sample data is designed to:

- Initialize the application.
- Verify database functionality.
- Support application testing.
- Demonstrate system features.
- Reduce manual data entry during development.

---

# 3. Default System Configuration

| Setting | Value |
|----------|-------|
| Restaurant Name | Saru Restaurant |
| Currency | INR |
| Tax Percentage | 0 |
| Receipt Footer | Thank You! Visit Again. |
| Application Version | 1.0 |

---

# 4. Default User Account

| Field | Value |
|--------|-------|
| Username | admin |
| Password | admin123 *(Development Only)* |
| Role | Owner |
| Status | Active |

**Note:** Passwords must be stored as hashed values during implementation.

---

# 5. Default Employee

| Field | Value |
|--------|-------|
| Employee ID | EMP001 |
| Name | Administrator |
| Role | Owner |
| Phone | 9999999999 |
| Status | Active |

---

# 6. Default Customer

| Field | Value |
|--------|-------|
| Customer ID | CUS001 |
| Name | Walk-in Customer |
| Phone | 0000000000 |

---

# 7. Default Categories

| Category ID | Category Name |
|--------------|---------------|
| CAT001 | Veg |
| CAT002 | Non-Veg |
| CAT003 | Beverages |

---

# 8. Default Menu Items

| Menu ID | Item | Category | Price |
|----------|------|----------|------:|
| MENU001 | Veg Fried Rice | Veg | 120 |
| MENU002 | Chicken Fried Rice | Non-Veg | 180 |
| MENU003 | Fresh Lime Juice | Beverages | 60 |

---

# 9. Default Supplier

| Supplier ID | Supplier Name |
|--------------|---------------|
| SUP001 | Local Supplier |

---

# 10. Default Inventory Items

| Inventory ID | Item | Supplier | Quantity |
|---------------|------|----------|---------:|
| INVITEM001 | Rice | SUP001 | 100 |
| INVITEM002 | Chicken | SUP001 | 50 |
| INVITEM003 | Soft Drink | SUP001 | 75 |

---

# 11. Default Restaurant Tables

| Table ID | Table Name | Capacity | Status |
|-----------|------------|---------:|--------|
| T01 | Table 1 | 4 | Available |
| T02 | Table 2 | 4 | Available |
| T03 | Table 3 | 6 | Available |

---

# 12. Default Bill Status

| Status |
|---------|
| Pending |
| Paid |
| Cancelled |
| Refunded |

---

# 13. Sample ID Standards

| Module | Format | Example |
|---------|--------|---------|
| Employee | EMP### | EMP001 |
| Customer | CUS### | CUS001 |
| Supplier | SUP### | SUP001 |
| Category | CAT### | CAT001 |
| Menu | MENU### | MENU001 |
| Inventory | INVITEM### | INVITEM001 |
| Bill | INV-###### | INV-000001 |
| Payment | PAY### | PAY001 |
| Table | T## | T01 |

---

# 14. Development Notes

- Sample data is intended only for development and testing.
- Production environments must replace all default records.
- Default passwords must be changed before production deployment.
- Sample data should never contain sensitive business information.

---

# 15. Version Scope

## Version 1.0

- Default Owner Account
- Default Employee
- Walk-in Customer
- Basic Categories
- Sample Menu
- Sample Supplier
- Sample Inventory
- Restaurant Tables

## Version 2.0

- Bulk Sample Data
- Demo Sales Data
- Inventory History

## Version 3.0

- Multi-Branch Sample Dataset
- Analytics Sample Records

---

# 16. Approval

The sample data specification for Saru POS Version 1.0 has been reviewed and approved for implementation.

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