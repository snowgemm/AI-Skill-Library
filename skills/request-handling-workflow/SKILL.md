---
name: request-handling-workflow
description: Structured process for receiving, analyzing, researching, planning, executing, verifying, and independently reviewing a software or agent task request. Use for any non-trivial change or new feature work.
license: UNLICENSED
metadata:
  author: AI-Skill-Library contributors
  version: "1.0.0"
  status: independent_original
  reviewed_on: "2026-11-16"
---

# Request Handling Workflow

Use this skill for non-trivial requests (new features, refactors, bug fixes with unclear scope, or multi-step work). Do not use for pure questions or one-line changes.

## Process

1. **Tiếp nhận yêu cầu** — Capture the raw request, constraints, and success criteria. Confirm understanding before proceeding.
2. **Phân tích mục tiêu và phạm vi** — Break down goals, non-goals, and boundaries. Identify what is in scope vs out of scope.
3. **Kiểm tra ngữ cảnh, tài liệu và công việc cũ** — Review existing code, docs, prior decisions, and related work. Avoid duplicating or contradicting previous solutions.
4. **Nghiên cứu nguồn và tài liệu chính thức** — Prefer official documentation, current vendor sources, and pinned references over memory or secondary blogs.
5. **Đánh giá phương án, rủi ro** — List viable approaches. Evaluate trade-offs (complexity, performance, security, maintainability, license). Choose the optimal one with brief rationale.
6. **Lập kế hoạch thực hiện** — Define concrete steps, verification points, and rollback or recovery options.
7. **Thực hiện công việc** — Implement with clean code, security, and performance priority. Add brief comments only for non-obvious logic.
8. **Kiểm tra kết quả** — Run validators, tests, or manual checks against the success criteria.
9. **Đạt yêu cầu?** — If not, fix and re-check (loop). If yes, proceed to independent review.
10. **Review độc lập** — Separate review of the result for correctness, security, consistency, and residual risks.
11. **Báo cáo kết quả và việc còn tồn đọng** — Summarize what was done, what was verified, and any remaining items or known limitations.

## Rules

- Prefer official sources and current documentation.
- Do not copy proprietary or host-managed skill bodies.
- Explicitly record license status and provenance for any new material.
- Distinguish static validation from runtime/host compatibility evidence.
- Security and least-privilege first when touching installers, scripts, or external tools.
- Keep explanations concise; put logic in code comments when implementing.

## When not to use

- Pure informational questions with no change required.
- Trivial one-line fixes with clear scope and no risk.
- Work that already has an approved plan and is only in the execution phase.

This is an independently authored portable guide. It is UNLICENSED and not approved for redistribution until a repository-level license is selected.
