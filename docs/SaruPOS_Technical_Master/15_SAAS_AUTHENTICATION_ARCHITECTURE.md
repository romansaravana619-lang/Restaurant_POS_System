# 15 — SaaS Authentication Architecture

## Objective

Extend the current SaruPOS authentication model so authenticated users operate inside a trusted restaurant/tenant context.

## Target flow

```text
Login
  ↓
Credential Verification
  ↓
User Identity
  ↓
Tenant Membership Resolution
  ↓
Role / Permission Resolution
  ↓
JWT / Session Context
  ↓
Protected API Request
  ↓
Tenant + Role Authorization
  ↓
Service Layer
```

## Identity model

A SaaS identity should conceptually resolve to:

```text
User
 ├── Tenant Membership(s)
 ├── Role(s)
 └── Permission Set
```

If a user can belong to more than one restaurant, the active tenant context must be explicitly selected and validated before tenant-scoped operations are allowed.

## Authorization rules

1. Authenticate the user.
2. Establish the trusted tenant context.
3. Verify the requested resource belongs to that tenant.
4. Verify the user's role/permission for the operation.
5. Execute business logic only after both checks succeed.

## Security boundary

Never rely on a tenant ID, role or permission value supplied only by the browser. The backend must derive or validate authorization context from authenticated server-trusted information.

## JWT evolution

The existing v1.0 JWT concept can be extended with carefully selected claims or server-side membership resolution. Sensitive authorization decisions should remain enforceable server-side and token contents should not become the sole source of truth for mutable permissions.

## Operational considerations

- Token expiration and refresh strategy.
- Logout / revocation strategy where required.
- Password reset and account recovery.
- Tenant membership changes.
- Role changes taking effect safely.
- Audit logging for privileged actions.

> Architecture only: this document does not modify the v1.0 authentication implementation.
