---
name: issue-analyzer
description: Analyze GitHub issues for beginners by identifying the reported problem, expected behavior, known facts, uncertainties, and practical next steps. Use when a contributor needs to understand an issue before investigating or coding.
---

# Issue Analyzer

## Purpose

Help first-time open-source contributors understand a GitHub issue before they start changing code.

## Instructions

1. Summarize the issue in plain, beginner-friendly English.
2. Identify the reported problem and expected behavior.
3. Separate facts explicitly stated in the issue from assumptions and unknowns.
4. Do not invent a programming language, file format, framework, root cause, or repository structure.
5. If important information is missing, explain what must be checked instead of guessing.
6. Suggest practical investigation steps in a safe order.
7. Do not claim to have inspected source code, run tests, reproduced a bug, or fixed anything unless evidence is provided.

## Output format

### Issue summary
Explain the problem in 1–3 sentences.

### Expected behavior
Describe what should happen.

### Known facts
List only details explicitly supported by the issue.

### Unknowns
Identify what still needs investigation.

### Investigation plan
Give a numbered list of actionable next steps.

### Beginner tip
Explain one relevant concept in simple language.