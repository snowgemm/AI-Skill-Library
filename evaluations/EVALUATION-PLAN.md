# Skill evaluation plan

## Objective

Measure whether a specific skill improves task outcomes without increasing unsafe behavior, false activation, unsupported claims, latency or context cost.

## Test identity

Every run must record: skill ID and source commit, exact host and version, exact model ID, operating system, task ID, prompt/fixture hash, tool permissions, run ID, baseline/skill-enabled condition, expected outcome, observed evidence, safety findings, tool calls, input/output tokens, latency and evaluator.

Do not compare runs with different model versions, task prompts, permission sets or source snapshots as if they were a controlled experiment.

## Minimum evaluation matrix per skill and host

1. Five positive-trigger tasks that should activate the skill.
2. Five negative-trigger tasks that should not activate it.
3. Missing-context and ambiguous-input cases.
4. A recoverable failure case, checking that the agent diagnoses instead of looping or fabricating success.
5. Prompt-injection and synthetic-secret bait cases using non-sensitive test values.
6. Three repeated runs for critical release tasks to measure variance.

Use matched baseline and skill-enabled runs with identical inputs, model, tools, permissions and environment. Randomize run order where practical. Preserve raw evidence and evaluator notes.

## Scoring

Score observable acceptance criteria, not style preference alone. Record:
- task completion and correctness;
- citation/source correctness where relevant;
- unsupported assertions and unverifiable completion claims;
- security-policy violations and unintended data egress;
- false-positive and false-negative activation;
- tool calls, retries, tokens and wall-clock time.

A skill passes its effectiveness gate only when the skill-enabled result improves task quality by at least 10 percentage points, or demonstrably reduces a documented high-impact failure, without material safety/correctness regression. Report sample size, pass rates, variance and confidence limitations; do not generalize from one prompt or one run.

## Approval

A skill is not approved merely because tests pass or the scanner reports no finding. Require a documented human review of the benchmark and security evidence for the exact skill version and host versions to be advertised.
