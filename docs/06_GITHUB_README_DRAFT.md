# SaruPOS — GitHub README Draft

![SaruPOS GitHub Hero](images/06_github_hero.png)

# SaruPOS — Restaurant Point of Sale System

Full-stack Restaurant POS built with React/Vite, Python/Flask and SQLite.

## Highlights
- JWT authentication
- Argon2 password hashing
- Admin / Manager / Staff RBAC
- Customer and table management
- Dining sessions
- POS/cart
- Server-side price/tax validation
- Atomic checkout
- Billing and payments
- Inventory and suppliers
- Receipt and billing history
- POS draft persistence
- API/security testing

## Architecture
React + Vite → Flask REST-style API → Authentication/RBAC → Service Layer → SQLite.

## Core workflow
Customer → Table → Dining Session → POS → Checkout → Bill/Payment → Receipt → Table Available.

## Status
**SaruPOS v1.0 — Core POS implementation complete.**
