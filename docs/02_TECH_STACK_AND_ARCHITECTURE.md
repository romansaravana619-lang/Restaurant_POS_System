# SaruPOS — Technology Stack & Architecture

![SaruPOS Technology Stack & Architecture](images/02_tech_architecture.png)

## Technology stack

| Layer | Technology |
|---|---|
| Frontend | React |
| Tooling | Vite |
| Backend | Python + Flask |
| API | REST-style HTTP/JSON |
| Database | SQLite |
| Authentication | JWT |
| Password hashing | Argon2 |
| Authorization | RBAC |
| Testing | Pytest |
| Draft persistence | sessionStorage |

## Layered architecture

React/Vite → HTTP/JSON → Flask Routes → Validation/Auth → Service Layer → SQLite.

Routes handle HTTP concerns. Services handle business rules, database operations and transaction logic.

## Frontend
Pages, components, authentication context/hooks, API service layer and POS state.

## Database domains
Users, employees, customers, restaurant tables, dining sessions, categories, menu items, suppliers, inventory items, bills, bill items, payments and settings.

## Interview takeaway
“I separated UI, API routing and business services so validation and transaction rules remain in the backend rather than being coupled to the frontend.”
