# Contributing to FirstPR AI

Thanks for your interest in improving FirstPR AI!

## Before you start

- Read the README and understand the local Ollama setup.
- For larger changes, open an issue first to discuss the proposed direction.
- Keep changes focused and explain the problem they solve.
- Never commit API keys, passwords, access tokens, private prompts, model downloads, or your virtual environment.

## Local development

1. Create and activate a Python virtual environment.
2. Install dependencies with `python -m pip install -r requirements.txt`.
3. Make sure Ollama is running and the configured model is available if you need to test the full app.
4. Run `python app.py`.
5. Run `python -m compileall -q app.py` before submitting.

## Pull requests

Please include:
- A clear description of the problem and the change.
- Steps to reproduce or test the change.
- Screenshots for meaningful UI changes, when practical.
- Notes about any limitations or behavior that still needs work.

Keep pull requests small and reviewable. Do not claim a test passed unless you ran it. AI-generated suggestions should be reviewed and verified by the contributor.

## Reporting a bug

When opening an issue, include the expected behavior, actual behavior, steps to reproduce, Python version, operating system, and relevant error messages. Remove secrets and personal information from logs before sharing them.
