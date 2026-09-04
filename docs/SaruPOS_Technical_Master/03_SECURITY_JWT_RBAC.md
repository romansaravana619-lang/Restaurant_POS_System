# SaruPOS — Security, JWT & RBAC

![SaruPOS Security, JWT & RBAC](../images/03_security_jwt_rbac.svg)

## Authentication
Login validates credentials through the authentication service and returns an authentication result used for protected API access.

## JWT lifecycle
Login → credential verification → JWT generation → frontend authenticated state → Bearer token → JWT validation → role authorization → service → database.

## Password security
Argon2 is used for password hashing and verification.

## Secret handling
The JWT signing secret is supplied through `SARU_POS_JWT_SECRET`. The real secret must remain outside source control; `.env.example` is a configuration template.

## RBAC
The application distinguishes Admin, Manager and Staff permissions. Management operations are restricted while operational functions remain available to the appropriate roles.

## Checkout security
The backend validates customer, employee, table/session, menu availability, current menu prices, tax configuration and payment method. Client-supplied prices are not authoritative.

## Atomic checkout
Validate → Begin transaction → Bill + Items + Payment → Close Dining Session → Table Available → Commit.

## Portfolio statement
“I implemented JWT authentication, Argon2 password hashing and RBAC, and protected checkout integrity by keeping price/tax authority in the backend and grouping related writes into an atomic transaction.”