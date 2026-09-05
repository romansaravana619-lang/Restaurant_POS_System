# 13 — SaaS POS Architecture Planning

## Objective

Define how SaruPOS v1.0 can evolve into a multi-restaurant SaaS platform while preserving the existing POS foundation.

## Target architecture

```text
Web / POS Clients
        ↓
Flask REST API
        ↓
Authentication + Tenant Context + RBAC
        ↓
Modular Service Layer
        ↓
Tenant-aware Data Access
        ↓
Production Relational Database
```

## Domain hierarchy

```text
SaaS Platform
 └── Restaurant / Tenant
      ├── Branches
      ├── Users / Employees
      ├── Customers
      ├── Tables / Dining Sessions
      ├── Categories / Menu Items
      ├── Inventory / Suppliers
      └── Bills / Payments
```

## Non-negotiable tenant rule

Tenant identity must come from trusted authenticated context. Tenant A must never read, modify or delete Tenant B data.

## Design principles

1. Preserve working v1.0 behavior while adding SaaS capabilities.
2. Keep tenant context explicit in backend services and data access.
3. Keep authentication, authorization and business logic separated.
4. Enforce tenant isolation server-side, never only in the UI.
5. Design for branches from the beginning.
6. Plan migration from SQLite to a production relational database before cloud scale.

## Result

This becomes the architectural blueprint for the next database, authentication and implementation phases.

> Planning only: this document does not claim that v1.0 is already multi-tenant.
