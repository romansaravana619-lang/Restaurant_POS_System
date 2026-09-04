# ===================================================================
# SARU SYSTEMS
# PRODUCT BLUEPRINT DOCUMENT
# ===================================================================

# Document Information

| Field | Details |
|--------|---------|
| Document ID | SS-POS-PB-006 |
| Document Name | User Roles |
| Product Name | Saru POS |
| Product Code | SS-POS-001 |
| Version | 1.0 |
| Status | Planning |
| Owner | Saravana Kumar |
| Created Date | 31 July 2026 |
| Last Updated | 31 July 2026 |

---

# Purpose

This document defines the user roles, responsibilities, permissions, and access levels within Saru POS. It ensures that each user can access only the features required for their responsibilities.

---

# User Roles Overview

Saru POS supports three user roles:

- Admin
- Manager
- Staff

Each role has different responsibilities and permission levels.

---

# Role 1 – Admin

## Description

The Owner has complete control over the restaurant management system.

## Permissions

- Full dashboard access
- Manage menu items
- Manage employees
- View all reports
- Manage inventory
- Manage customers
- Configure system settings
- Create, edit, and delete users
- View business analytics

## Access Level

**Full Access**

---

# Role 2 – Manager

## Description

The Manager supervises daily restaurant operations and manages staff activities.

## Permissions

- View dashboard
- Manage menu items
- View inventory
- Update inventory
- View customer records
- Generate reports
- Supervise billing
- View employee information

## Restrictions

- Cannot change system settings
- Cannot delete owner account
- Cannot access sensitive business configurations

## Access Level

**Medium Access**

---

# Role 3 – Staff

## Description

The Cashier is responsible for customer billing and payment processing.

## Permissions

- Create bills
- Process payments
- Print invoices
- Search previous bills
- View menu items
- View customer information

## Restrictions

- Cannot edit menu
- Cannot manage inventory
- Cannot view business reports
- Cannot manage employees
- Cannot change system settings

## Access Level

**Limited Access**

---

# Permission Matrix

| Feature | Admin | Manager | Staff |
|---------|:-----:|:-------:|:--------:|
| Dashboard | ✅ | ✅ | ✅ |
| Billing | ✅ | ✅ | ✅ |
| Menu Management | ✅ | ✅ | ❌ |
| Customer Management | ✅ | ✅ | View Only |
| Inventory | ✅ | ✅ | ❌ |
| Reports | ✅ | ✅ | ❌ |
| Employee Management | ✅ | View Only | ❌ |
| User Management | ✅ | ❌ | ❌ |
| System Settings | ✅ | ❌ | ❌ |

---

# Security Principles

- Every user must log in using valid credentials.
- Users can only access authorized modules.
- Sensitive operations should be restricted to authorized users.
- User actions should be recorded for future auditing (future enhancement).

---

# Design Guidelines

The system should:

- Display menus based on the logged-in user's role.
- Hide unauthorized options automatically.
- Prevent direct access to restricted pages.
- Maintain secure session management.

---

# Success Criteria

This document will be considered complete when:

- All user roles are clearly defined.
- Permissions are properly separated.
- Security rules support future system development.

---

# Related Documents

- PB-003 Target Users
- PB-004 Product Features
- PB-005 Product Scope
- PB-007 User Flow

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
