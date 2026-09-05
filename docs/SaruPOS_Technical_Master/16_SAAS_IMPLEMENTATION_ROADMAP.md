# 16 — SaaS Implementation Roadmap

## Objective

Convert the approved SaaS architecture into an incremental implementation plan. Implementation should begin only after the architecture and data/security boundaries are accepted.

## Phase 1 — Foundation

- Create tenant and branch domain models.
- Define tenant-aware relationships for existing business entities.
- Establish schema migrations.
- Introduce a production relational database for the SaaS environment.

## Phase 2 — Identity & Access

- Add tenant membership model.
- Extend authentication to resolve tenant context.
- Implement tenant-aware RBAC.
- Add privileged-action audit logging.
- Add account recovery and token lifecycle handling.

## Phase 3 — API / Service Migration

- Update service-layer queries to require tenant context.
- Apply tenant filtering to every tenant-owned resource.
- Add authorization tests for cross-tenant access attempts.
- Preserve existing POS business rules.

## Phase 4 — SaaS Operations

- Cloud deployment.
- Environment and secret management.
- Database backups and migrations.
- Monitoring and logging.
- Health checks and operational alerts.

## Phase 5 — Productization

- Restaurant onboarding.
- Branch management.
- Subscription and plan management.
- Usage/feature controls.
- Centralized SaaS administration.

## Recommended implementation order

```text
Tenant Model
   ↓
Tenant-aware Database
   ↓
Tenant-aware Authentication
   ↓
Tenant-aware RBAC
   ↓
Service/API Migration
   ↓
Cross-tenant Security Testing
   ↓
Cloud Deployment
   ↓
SaaS Product Features
```

## Safety rule

Do not attempt a large one-shot conversion of v1.0. Keep the current POS stable, introduce one architectural boundary at a time, test it, then continue.

> Roadmap only: no SaaS implementation is claimed by this document.
