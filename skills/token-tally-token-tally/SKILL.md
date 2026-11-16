---
name: token-tally-token-tally
description: Count text tokens using the tokenizer for the selected model/provider and estimate context use for prompts, files, and tool results.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Token Counting and Context Budgeting

Use when the user asks how many tokens a prompt or dataset consumes, whether it fits a context budget, or how to reduce token overhead.

## Workflow

1. Identify the provider and exact model/tokenizer version. Different tokenizers produce different counts.
2. Use the official tokenizer or provider-supported counting method where available. Never present character count or word count as an exact token count.
3. Count the exact text/input representation, including system instructions, tool schemas, metadata, and file conversions when relevant.
4. Distinguish estimated input tokens from actual usage returned after a model request.
5. Account for images, audio, PDFs, and tool outputs separately when the tokenizer does not expose a reliable count.
6. Calculate remaining context only when the model's actual context window and reserved output budget are known.
7. Recommend compression by removing redundant context, narrowing retrieval, and summarizing older material while preserving essential facts.
8. Keep private prompts and documents local unless the user explicitly authorizes an external tokenizer service.

## Verification checklist

- Tokenizer matches the model/provider.
- Exact and estimated counts are distinguished.
- Multimodal payloads are not miscounted.
- Context window and output reserve are verified.
- Private text stays local by default.

## Reporting

Report source, period, model/provider, scope, measured values, estimates, data completeness, privacy handling, and the exact checks performed. Never claim a quota, cache hit, token count, or cost unless the underlying source supports that field.

## References

- https://platform.openai.com/tokenizer
- https://platform.openai.com/docs/guides/text

This is an independently authored usage workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
