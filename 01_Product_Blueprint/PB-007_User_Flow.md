# ===================================================================
# SARU SYSTEMS
# PRODUCT BLUEPRINT DOCUMENT
# ===================================================================

# Document Information

| Field | Details |
|--------|---------|
| Document ID | SS-POS-PB-007 |
| Document Name | User Flow |
| Product Name | Saru POS |
| Product Code | SS-POS-001 |
| Version | 1.0 |
| Status | Planning |
| Owner | Saravana Kumar |
| Created Date | 31 July 2026 |
| Last Updated | 31 July 2026 |

---

# Purpose

This document defines how users interact with Saru POS from login to logout. It describes the logical flow of activities for each major operation within the system.

---

# Overall User Flow

```
Login
   ↓
Dashboard
   ↓
Select Module
   ↓
Perform Task
   ↓
Save Data
   ↓
View Confirmation
   ↓
Return to Dashboard
   ↓
Logout
```

---

# Login Flow

```
Open Saru POS
      ↓
Enter Username & Password
      ↓
Validate Credentials
      ↓
Login Successful
      ↓
Open Role-Based Dashboard
```

If login fails:

```
Invalid Credentials
      ↓
Display Error Message
      ↓
Retry Login
```

---

# Billing Flow

```
Dashboard
      ↓
Open Billing
      ↓
Select / Add Customer
      ↓
Add Menu Items
      ↓
Calculate Total
      ↓
Choose Payment Method
      ↓
Generate Bill
      ↓
Print Invoice
      ↓
Save Transaction
```

---

# Customer Management Flow

```
Dashboard
      ↓
Customer Module
      ↓
Search Customer
      ↓
Customer Found?
      ↓
Yes → View Details

No
 ↓
Add New Customer
```

---

# Inventory Flow

```
Dashboard
      ↓
Inventory Module
      ↓
View Stock
      ↓
Update Quantity
      ↓
Save Changes
```

---

# Menu Management Flow

```
Dashboard
      ↓
Menu Module
      ↓
Add / Edit / Delete Item
      ↓
Save Menu
```

---

# Sales Report Flow

```
Dashboard
      ↓
Reports
      ↓
Select Report Type
      ↓
Select Date Range
      ↓
Generate Report
      ↓
View Report
```

---

# Logout Flow

```
Click Logout
      ↓
End User Session
      ↓
Return to Login Page
```

---

# User Experience Guidelines

- Every task should require the minimum number of steps.
- Navigation should be simple and intuitive.
- Error messages should clearly explain the problem.
- Confirmation messages should appear after successful operations.
- Users should always be able to return to the dashboard easily.

---

# Success Criteria

This document is successful when:

- All major workflows are clearly defined.
- Every module has a logical navigation path.
- The development team can implement screens based on these flows.
- Future UI/UX design can directly follow these workflows.

---

# Related Documents

- PB-003 Target Users
- PB-004 Product Features
- PB-006 User Roles
- PB-008 Functional Requirements

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