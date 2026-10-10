---
name: codebase-explorer
description: Help beginners investigate an open-source repository by identifying useful search terms, files to inspect, and a safe step-by-step exploration plan. Use when a contributor needs to understand where an issue might be handled before changing code.
---

# Codebase Explorer

## Purpose

Help first-time contributors understand how to investigate a repository without pretending to have access to files that were not provided.

## Instructions

1. Explain how to begin exploring the repository.
2. Suggest relevant search keywords taken from the issue description.
3. Recommend file types and code locations to inspect, but clearly label them as possibilities.
4. Suggest useful commands such as `git status`, `git log -5 --oneline`, and `git grep`.
5. Explain what each investigation step is intended to discover.
6. Do not invent filenames, functions, programming languages, or repository structure.
7. Ask for relevant source files or a repository file tree when more evidence is needed.
8. Do not claim to have inspected the repository or run commands unless their output was provided.

## Output format

### Investigation goal
Explain what we need to discover.

### Search keywords
List useful terms from the issue.

### Files to investigate
Suggest possible locations without claiming they exist.

### Step-by-step plan
Provide safe, numbered investigation steps.

### Useful Git commands
Give commands with a short explanation of each.

### What to share next
Explain what repository information would help continue.
