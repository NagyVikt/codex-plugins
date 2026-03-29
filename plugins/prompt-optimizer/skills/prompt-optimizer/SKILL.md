---
name: prompt-optimizer
description: Use when the user wants to reduce token usage in prompts, conversation context, or Codex request patterns while preserving intent and output quality.
---

# Prompt Optimizer

Use this skill when the user asks to save tokens, reduce token costs, or compress prompts/context.

## Goals

- Keep user intent unchanged.
- Reduce input tokens first, then output tokens.
- Keep instructions explicit and testable.

## Workflow

1. Identify token-heavy sections:
   - repeated context
   - long background paragraphs
   - vague open-ended asks
   - oversized example blocks
2. Rewrite as compact, structured prompt:
   - task in one sentence
   - constraints in bullets
   - strict output limit (`max words`, `N bullets`, or `JSON schema`)
3. Split static vs dynamic context:
   - static: reusable summary block
   - dynamic: per-request delta only
4. Provide two variants:
   - `safe`: high fidelity, moderate savings
   - `aggressive`: stronger compression, higher risk
5. Add measurable controls:
   - `max_output_tokens`
   - response format constraints
   - explicit “do not repeat context” instruction

## Rewrite Template

```text
Task: <one sentence>
Context: <3-6 bullet summary, no prose>
Constraints:
- Output format: <bullets/json/table>
- Length: <hard cap>
- Scope: <what to include/exclude>
- Tone: <optional>
Deliverable: <single concrete output>
```

## Codex-Specific Pattern

When optimizing prompts for Codex sessions:

- Avoid sending full file contents unless required.
- Reference file paths and line ranges instead of pasting large blocks.
- Ask for concise responses by default.
- Reuse compact project summaries between turns.
- Prefer incremental deltas over restating full instructions.

## Guardrails

- Do not remove critical constraints (security, compliance, correctness).
- Do not compress away required edge cases.
- If compression risks ambiguity, keep the longer phrasing for that part.
