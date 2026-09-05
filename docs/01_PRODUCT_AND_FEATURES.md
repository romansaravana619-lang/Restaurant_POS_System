# SaruPOS — Product & Feature Ecosystem

![SaruPOS Product & Feature Ecosystem](images/01_product_features.png)

## Product overview
SaruPOS is a full-stack Restaurant POS system covering the operational journey from customer/table assignment through ordering, checkout, payment, receipt and billing history.

## Core problem solved
It centralizes customer, table, menu, dining-session, POS, inventory, supplier, employee, billing and payment operations.

## Main roles
- **Admin** — full administration
- **Manager** — management/operational access
- **Staff** — operational restaurant access with selected management restrictions

## Feature inventory
Authentication; users; employees; customers; restaurant tables; dining sessions; categories; menu items; inventory; suppliers; POS/cart; billing; payments; receipt; billing history; settings; POS draft persistence.

## Core workflow
Customer → Available Table → Dining Session → POS → Cart → Checkout → Bill → Payment → Receipt → Table Available.

## Important implementation features
- Server-generated customer IDs
- Unique customer phone protection
- Occupied-table filtering
- Customer/table active dining-session relationship
- Server-side menu price and tax authority at checkout
- Atomic checkout transaction
- POS unfinished-order persistence through browser session storage

## Scope
SaruPOS v1.0 is a completed single-restaurant POS foundation. Multi-tenant SaaS, subscriptions, centralized platform administration and cloud production belong to the next phase.
