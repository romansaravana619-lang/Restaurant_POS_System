# 11 — SaaS POS Architecture Planning

## Goal

Evolve SaruPOS v1.0 from a single-restaurant POS into a tenant-aware SaaS platform without destabilizing the existing v1.0 application.

## Target architecture

```text
Web / POS Client
      ↓
API Gateway / Flask API
      ↓
Authentication + Tenant Context + RBAC
      ↓
Modular Service Layer
      ↓
Tenant-aware Data Access
      ↓
Production Relational Database
```

## Core domain hierarchy

```text
Platform
 └── Tenant / Restaurant
      ├── Branches
      ├── Users / Employees
      ├── Customers
      ├── Tables
      ├── Menu / Categories
      ├── Inventory / Suppliers
      └── Bills / Payments / Dining Sessions
```

## Tenant isolation rule

Every tenant-owned resource must be resolved inside the authenticated tenant context. A request authenticated for Tenant A must never read, update or delete Tenant B data.

## Evolution principles

1. Preserve current v1.0 behavior while introducing SaaS capabilities.
2. Make tenant context explicit rather than inferred from client-provided IDs.
3. Keep authentication and authorization separate from business services.
4. Enforce tenant isolation in backend data access, not only in the frontend.
5. Design for branch support even if the first SaaS release has one branch per tenant.
6. Move from SQLite toward a production relational database before cloud scale.

## SaaS phases

- Phase 1: Tenant-aware architecture and data model.
- Phase 2: Tenant-aware authentication and RBAC.
- Phase 3: SaaS service/API integration.
- Phase 4: Production database and cloud deployment.
- Phase 5: subscriptions, observability, backups and operational hardening.

## Boundary

This document defines the target architecture. It does not claim that the existing v1.0 database is already multi-tenant.
