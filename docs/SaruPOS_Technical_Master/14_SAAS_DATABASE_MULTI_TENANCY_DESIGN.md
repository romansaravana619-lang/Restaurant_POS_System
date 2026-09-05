# 14 — SaaS Database / Multi-Tenancy Design

## Objective

Design tenant-aware persistence for multiple restaurants while maintaining strict logical data isolation.

## Recommended hierarchy

```text
Tenant
 └── Branch
      ├── Users / Employees
      ├── Customers
      ├── Tables
      ├── Dining Sessions
      ├── Categories
      ├── Menu Items
      ├── Inventory / Suppliers
      └── Bills / Bill Items / Payments
```

## Tenant ownership

Business records that belong to a restaurant should carry an explicit tenant association directly or through a controlled parent relationship. Branch-scoped records should additionally resolve to a branch.

## Query rule

```text
Authenticated Tenant Context
        ↓
Service / Repository
        ↓
WHERE tenant_id = current_tenant
        ↓
Return only authorized tenant data
```

Client-provided tenant IDs must not be trusted as the authorization source.

## Database direction

Current v1.0 uses SQLite for local persistence. A SaaS deployment should move to a production relational database capable of concurrent cloud workloads, migrations, backups and operational monitoring.

## Integrity strategy

- Primary and foreign keys for relationships.
- Unique constraints scoped to the correct tenant where business rules require uniqueness.
- Required fields enforced at the schema and application layers.
- Transactions for multi-record business operations.
- Migration scripts for controlled schema evolution.

## Isolation strategies

A shared database with tenant keys is the initial practical model. A future scale strategy can evaluate stronger isolation models such as separate schemas or separate databases for selected tenants, depending on operational, compliance and scaling requirements.

> Design only: no multi-tenant database migration is performed by this document.
