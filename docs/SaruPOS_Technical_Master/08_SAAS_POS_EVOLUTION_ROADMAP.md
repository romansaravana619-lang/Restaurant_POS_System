# SaruPOS → SaaS POS Evolution Roadmap

![SaruPOS to SaaS POS Evolution](../images/08_saas_evolution.svg)

## Strategy
SaruPOS v1.0 is the foundation. SaaS POS is the next architectural evolution.

## Current → Future
Single restaurant → tenant-aware architecture → multi-tenant platform → restaurant/branch management → subscriptions → centralized administration → cloud deployment.

## Multi-tenancy rule
Tenant A must never read or modify Tenant B data.

## Future authentication
Login → verify user → resolve tenant → issue JWT → validate token → resolve tenant → tenant filter → role check → service.

The exact future JWT claim structure should be finalized during SaaS architecture design.

## Recommended build order
1. SaaS requirements
2. Multi-tenant domain model
3. Tenant isolation strategy
4. Authentication model
5. Database redesign
6. Tenant middleware/context
7. Restaurant/branch APIs
8. Subscription APIs
9. Tenant-aware POS services
10. SaaS frontend
11. Cloud deployment
12. Monitoring/backups

## Learning progression
SaruPOS demonstrates full-stack fundamentals. SaaS POS should demonstrate multi-tenancy, stronger security boundaries, scalable data design, subscription architecture and cloud deployment.