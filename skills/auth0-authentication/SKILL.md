---
name: auth0-authentication
description: Design, integrate, and review Auth0 authentication and authorization in applications and APIs, including OIDC/OAuth flows, sessions, tokens, MFA, Organizations, and RBAC.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Auth0 Identity Integration

Use for app login, API protection, user sessions, MFA, Organizations, role/permission mapping, and Auth0 tenant configuration. Do not assume an SDK or dashboard setting from memory is current.

## Workflow

1. Inspect the application type (SPA, regular web app, native app, machine-to-machine), framework, Auth0 SDK version, tenant region, API audience, and existing callback/logout URLs.
2. Choose the OAuth/OIDC flow for the client type. Prefer Authorization Code with PKCE for public clients; use a confidential-client flow only in a trusted server. Do not introduce legacy implicit or password grants without a documented, platform-supported reason.
3. Configure exact callback, logout, and allowed-origin URLs for each environment. Avoid broad wildcard URLs. Keep client secrets and Management API tokens on trusted servers only.
4. Validate tokens at the resource server: signature from the trusted issuer keys, issuer, audience, expiry, algorithm, and relevant scopes/permissions. Do not trust an ID token as an API access token.
5. Separate authentication from authorization. Define API permissions, RBAC behavior, and Organization-specific membership/role rules explicitly; test both allowed and denied access.
6. Choose session and refresh-token settings based on threat model and UX. Review rotation, expiry, revocation, storage, logout, and reauthentication behavior against current Auth0 docs.
7. Add MFA or step-up requirements only where required by the risk model. Keep Actions narrowly scoped, bounded, and covered by failure-path tests.

## Verification checklist

- Correct app/client type and OAuth flow.
- Redirect URIs are exact and environment-specific.
- No secrets in browser/mobile bundles or repository.
- API validates access-token signature, issuer, audience, expiry, and permissions.
- Negative authorization and expired/revoked token cases fail closed.
- Login, logout, refresh, MFA, and Organization scenarios are tested.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a deployment, domain, worker, database, or setting changed until the relevant result is independently verified.

## Official references

- https://auth0.com/docs
- https://auth0.com/docs/get-started/authentication-and-authorization-flow
- https://auth0.com/docs/secure/tokens
- https://auth0.com/docs/manage-users/organizations
- https://auth0.com/changelog

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
