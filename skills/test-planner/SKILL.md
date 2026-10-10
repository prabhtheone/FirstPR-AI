---
name: test-planner
description: Create a practical test plan for an open-source issue, including expected behavior, normal cases, edge cases, regression checks, and verification steps. Use when a contributor needs to plan testing before or after a code change.
---

# Test Planner

## Purpose

Help beginner contributors determine how to verify a bug fix or feature safely.

## Instructions

1. Summarize what needs to be tested using only the issue details provided.
2. Identify the expected behavior and observable results.
3. Create test cases for normal use, edge cases, invalid inputs, and regression risks where relevant.
4. For each test, describe the setup, action, and expected result.
5. Recommend relevant automated tests only when appropriate for the available information.
6. Do not invent a test framework, command, filename, or test result.
7. Clearly distinguish proposed tests from tests that have actually been run.
8. If details are missing, state what information is needed instead of guessing.

## Output format

### Testing objective
Explain what behavior must be verified.

### Test checklist
List practical test cases and their expected results.

### Edge cases
Describe additional cases worth checking.

### Regression checks
Explain what existing behavior should continue working.

### How to verify
Give safe verification steps and label any suggested commands as examples when the project is unknown.

### Missing information
List any details needed to create a more specific test plan.
