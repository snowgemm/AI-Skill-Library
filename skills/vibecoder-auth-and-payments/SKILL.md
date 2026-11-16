---
name: vibecoder-auth-and-payments
description: Implement application sign-in, sessions, roles, protected routes, subscriptions, payment checkout, and webhook processing with secure provider boundaries.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Authentication and Payment Integration

Use when adding or fixing application authentication, account management, subscriptions, or online checkout.

## Workflow

1. Identify client type, backend framework, identity provider/payment provider, account model, regions, currencies, and applicable business requirements.
2. Choose a supported authentication flow for the client. Validate tokens and sessions on the server and enforce authorization for every protected resource.
3. Keep private keys and payment secrets server-side. Use hosted checkout/tokenization where appropriate; do not store raw payment-card data.
4. Model subscription state explicitly and treat provider webhooks as the authoritative event stream for payment lifecycle transitions.
5. Verify webhook signatures, timestamps/replay protection, event IDs, idempotency, and safe handling of out-of-order or duplicated events.
6. Design account recovery, email verification, session expiry/revocation, role changes, cancellation, refunds, and failed-payment states.
7. Use sandbox/test mode and test both successful and denied/failed flows. Never use real customer payment data in development.
8. Document provider dependencies, data retention, access boundaries, support/operational procedures, and remaining legal/compliance review requirements.

## Verification checklist

- Authentication and authorization are separate.
- Provider secrets are not client-exposed.
- Raw card data is not stored.
- Webhooks are signature-verified and idempotent.
- Failure, cancellation, and recovery cases are tested.

## Reporting

Report inspected files/context, decisions, exact changes if any, tests/commands and observed results, unresolved defects, and limitations. Never claim a build, deployment, security guarantee, payment operation, or feature works without direct evidence.

## References

- https://owasp.org/www-project-authentication-cheat-sheet/
- https://docs.stripe.com/
- https://auth0.com/docs/

This is an independently authored software-engineering workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
