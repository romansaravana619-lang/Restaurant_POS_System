# ===================================================================
# SARU SYSTEMS
# PRODUCT BLUEPRINT DOCUMENT
# ===================================================================

# Document Information

| Field | Details |
|--------|---------|
| Document ID | SS-POS-PB-009 |
| Document Name | Non-Functional Requirements |
| Product Name | Saru POS |
| Product Code | SS-POS-001 |
| Version | 1.0 |
| Status | Planning |
| Owner | Saravana Kumar |
| Created Date | 31 July 2026 |
| Last Updated | 31 July 2026 |

---

# Purpose

This document defines the quality attributes of Saru POS. Non-functional requirements describe how the system should perform rather than what it should do.

---

# Performance Requirements

| ID | Requirement |
|----|-------------|
| NFR-001 | The system shall load the dashboard within 3 seconds under normal operating conditions. |
| NFR-002 | A bill shall be generated within 2 seconds after payment confirmation. |
| NFR-003 | The system shall support at least 200–300 billing transactions per day without performance issues. |

---

# Security Requirements

| ID | Requirement |
|----|-------------|
| NFR-004 | Every user shall authenticate using a valid username and password. |
| NFR-005 | Passwords shall be stored securely in encrypted (hashed) form. |
| NFR-006 | Users shall access only the modules permitted for their role. |
| NFR-007 | User sessions shall end automatically after logout. |

---

# Reliability Requirements

| ID | Requirement |
|----|-------------|
| NFR-008 | The system shall save completed transactions without data loss. |
| NFR-009 | The application shall continue operating reliably during normal business hours. |

---

# Usability Requirements

| ID | Requirement |
|----|-------------|
| NFR-010 | The interface shall be simple and easy to learn. |
| NFR-011 | Common tasks shall require the minimum number of user actions. |
| NFR-012 | Error messages shall be clear and understandable. |

---

# Compatibility Requirements

| ID | Requirement |
|----|-------------|
| NFR-013 | The application shall run on modern web browsers such as Chrome, Edge, and Firefox. |
| NFR-014 | The system shall support common desktop screen resolutions. |

---

# Maintainability Requirements

| ID | Requirement |
|----|-------------|
| NFR-015 | The source code shall follow the Saru Systems Coding Standards. |
| NFR-016 | The system architecture shall support future feature enhancements with minimal changes. |

---

# Scalability Requirements

| ID | Requirement |
|----|-------------|
| NFR-017 | The system shall be designed to support future migration from SQLite to MySQL. |
| NFR-018 | The application architecture shall support future cloud deployment. |

---

# Availability Requirements

| ID | Requirement |
|----|-------------|
| NFR-019 | The system shall be available whenever the restaurant is operating, subject to planned maintenance. |

---

# Acceptance Criteria

The non-functional requirements will be considered complete when:

- The system performs efficiently.
- Business data remains secure.
- The application is reliable and user-friendly.
- The architecture supports future growth.

---

# Related Documents

- PB-008 Functional Requirements
- PB-010 Success Criteria

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