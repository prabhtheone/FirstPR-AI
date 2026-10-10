---
name: contribution-safety-checker
description: Help open-source contributors identify risks before making or submitting a change, including exposed secrets, sensitive data, destructive commands, unexpected side effects, and missing tests. Use when reviewing a proposed contribution workflow or change description for safety concerns.
---

# Contribution Safety Checker

## Purpose

Help beginner contributors recognize potential risks before changing or submitting code.

## Instructions

1. Review only the issue, proposed change, commands, or code actually provided.
2. Identify possible security, privacy, data-loss, and unexpected side-effect risks.
3. Warn about API keys, passwords, access tokens, private keys, and personal information being committed.
4. Flag destructive commands or operations when they appear in the supplied material.
5. Recommend reviewing `git diff` and `git status` before committing.
6. Suggest appropriate tests and backups when relevant.
7. Do not claim to have scanned a repository, detected a real secret, or verified a fix unless evidence supports that claim.
8. Distinguish confirmed risks from potential risks and unknowns.
9. Never ask the contributor to paste real credentials or secrets into the chat.

## Output format

### Safety summary
Give a concise assessment based on the available evidence.

### Potential risks
List each risk, why it matters, and how to reduce it.

### Secrets and sensitive data
Explain what to check before committing.

### Safe verification steps
Give practical checks appropriate to the supplied information.

### Before opening a pull request
Provide a final safety checklist.

### Limitations
Clearly state what could not be verified from the supplied information.
