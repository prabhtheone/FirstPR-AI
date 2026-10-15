# Security Policy

## Supported versions

Security fixes are currently considered for the latest version on the `main` branch.

## Reporting a vulnerability

Please **do not** report exploitable vulnerabilities, exposed credentials, or private user data in a public issue.

Instead, use GitHub's private vulnerability reporting feature for this repository if it is enabled. If it is unavailable, contact the repository maintainer privately through the contact options on their GitHub profile.

Include, when safe to do so:

- A clear description of the potential impact.
- Steps to reproduce the issue in a test environment.
- A minimal proof of concept that does not access other people's data.
- Any suggested mitigation.

Please allow the maintainer reasonable time to investigate before publicly disclosing an unpatched vulnerability.

## Safe use of FirstPR AI

- Never paste API keys, passwords, access tokens, private keys, or confidential source code into prompts.
- FirstPR AI sends prompts to the Ollama endpoint configured in `app.py`. Verify the endpoint and your local environment before using sensitive project material.
- Treat model-generated commands and code suggestions as untrusted until reviewed and tested.
