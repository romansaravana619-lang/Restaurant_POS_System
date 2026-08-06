# ===================================================================
# SARU SYSTEMS
# SYSTEM DESIGN DOCUMENT
# ===================================================================

# Document Information

| Field | Details |
|--------|---------|
| Document ID | SS-POS-SD-001 |
| Document Name | System Architecture |
| Product Name | Saru POS |
| Product Code | SS-POS-001 |
| Version | 1.0 |
| Status | Planning |
| Owner | Saravana Kumar |
| Created Date | 31 July 2026 |
| Last Updated | 31 July 2026 |

---

# Purpose

This document defines the overall architecture of the Saru POS system. It explains how different layers of the application interact, how data flows through the system, and the architectural principles followed during development.

---

# Architecture Overview

Saru POS follows a **Three-Tier Architecture**, where the application is divided into three independent layers:

1. Presentation Layer (Frontend)
2. Application Layer (Backend)
3. Data Layer (Database)

This architecture improves maintainability, scalability, security, and modularity.

---

# System Architecture Diagram

```
+------------------------------------------------------+
|                  Presentation Layer                  |
|           HTML | CSS | JavaScript | Browser          |
+------------------------------------------------------+
                        │
                        │ HTTP Request / Response
                        ▼
+------------------------------------------------------+
|                 Application Layer                    |
|          Flask Framework + Python Business Logic     |
+------------------------------------------------------+
                        │
                        │ SQL Queries
                        ▼
+------------------------------------------------------+
|                    Data Layer                        |
|              SQLite Database (v1.0)                 |
+------------------------------------------------------+
```

---

# Architecture Layers

## 1. Presentation Layer (Frontend)

### Responsibilities

- Display user interface
- Capture user input
- Send requests to the backend
- Display responses received from the backend

### Technologies

- HTML5
- CSS3
- JavaScript

### Example Screens

- Login
- Dashboard
- Billing
- Inventory
- Customer Management
- Reports
- Settings

---

## 2. Application Layer (Backend)

### Responsibilities

- Handle HTTP requests
- Authenticate users
- Execute business logic
- Validate user input
- Generate invoices
- Process billing
- Generate reports
- Communicate with the database

### Technologies

- Python
- Flask Framework

---

## 3. Data Layer (Database)

### Responsibilities

- Store application data
- Retrieve records
- Update records
- Delete records
- Maintain data integrity

### Database

Version 1.0

- SQLite

Future Versions

- MySQL

---

# Request–Response Flow

Every user action follows the Request–Response Cycle.

```
User
   │
   ▼
Frontend (HTML/CSS/JS)
   │
   ▼
Flask Application
   │
   ▼
Python Business Logic
   │
   ▼
SQLite Database
   │
   ▼
Python Business Logic
   │
   ▼
Flask Response
   │
   ▼
Frontend
   │
   ▼
User
```

---

# Example Workflow

## User Login

```
User enters Username & Password
            │
            ▼
HTML Login Form
            │
            ▼
Flask Route (/login)
            │
            ▼
Python Authentication Logic
            │
            ▼
SQLite User Verification
            │
            ▼
Authentication Success
            │
            ▼
Dashboard Displayed
```

---

# Architectural Principles

The Saru POS system follows the following software engineering principles:

### Separation of Concerns

Each layer performs only its own responsibility.

### Loose Coupling

Each layer can be modified independently without affecting other layers.

### High Cohesion

Modules contain related functionalities grouped together.

### Reusability

Business logic can be reused across multiple modules.

### Scalability

The architecture supports future enhancements such as:

- Cloud deployment
- Mobile application
- Multi-branch support
- API integrations

---

# Design Decisions

| Decision | Reason |
|----------|--------|
| Flask Framework | Lightweight, simple, ideal for Version 1.0 |
| SQLite | Easy deployment and zero configuration |
| Three-Tier Architecture | Clear separation between UI, logic, and data |
| Modular Design | Easier maintenance and future expansion |
| Browser-Based Application | No software installation required |

---

# Advantages of the Architecture

- Easy to maintain
- Secure architecture
- Modular development
- Better performance
- Faster debugging
- Scalable for future versions
- Supports team development
- Easy database migration

---

# Limitations (Version 1.0)

- Supports a single restaurant
- Uses SQLite instead of an enterprise database
- Web application only
- No offline synchronization
- Limited third-party integrations

---

# Future Enhancements

The architecture is designed to support:

- MySQL Database
- REST API
- Mobile Application
- Cloud Deployment
- Multi-Branch Management
- Online Payment Integration
- AI-Based Sales Analytics

---

# Related Documents

## Previous

- SD-000 – System Profile
- PB-000 to PB-010

## Next

- SD-002 – Module Architecture

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