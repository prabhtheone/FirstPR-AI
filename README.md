# 🤖 FirstPR AI

**A beginner-friendly AI mentor for open-source contributors.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/UI-Gradio-orange?logo=gradio)](https://www.gradio.app/)
[![Ollama](https://img.shields.io/badge/Local%20AI-Ollama-black)](https://ollama.com/)
[![CI](https://github.com/prabhtheone/FirstPR-AI/actions/workflows/ci.yml/badge.svg)](https://github.com/prabhtheone/FirstPR-AI/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

FirstPR AI helps new contributors understand GitHub issues, explore unfamiliar codebases, plan tests, prepare pull requests, and review potentially risky contribution steps.

**Try the hosted app:** [firstpr-ai.vercel.app](https://firstpr-ai.vercel.app)

## ✨ Two ways to use FirstPR AI

- **Local mode:** a Gradio interface powered by Ollama. Prompts are sent to the Ollama server configured on your computer; no cloud AI key is needed.
- **Hosted mode:** a browser interface served by Vercel with a serverless API that calls Groq. Prompts are sent to the configured cloud provider.

## 🧰 Agent skills

| Skill | What it helps you do |
| --- | --- |
| **Issue Analyzer** | Break an issue into a problem statement, requirements, unknowns, and investigation steps. |
| **Codebase Explorer** | Plan how to navigate an unfamiliar repository and verify where relevant code lives. |
| **Test Planner** | Identify positive, negative, edge-case, and regression tests. |
| **PR Mentor** | Prepare a small, reviewable contribution and a clear pull request description. |
| **Contribution Safety Checker** | Review commands and contribution steps for risk and reversibility. |

The five Markdown files in `skills/` are the single source of truth. Both the local app and hosted API load them through `skill_registry.py`, so skill instructions are not duplicated across backends.

## 🖼️ Screenshots

![FirstPR AI main interface](screenshots/main-interface.png.png)

![FirstPR AI skill selector](screenshots/agent-skills.png.png)

![FirstPR AI settings](screenshots/settings.png.png)

## 🚀 Run locally

### Prerequisites

- Python 3.10 or newer
- [Ollama](https://ollama.com/download)
- [Git](https://git-scm.com/downloads)

### 1. Clone the repository

```bash
git clone https://github.com/prabhtheone/FirstPR-AI.git
cd FirstPR-AI
```

### 2. Create and activate a virtual environment

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use `.venv\Scripts\python.exe` instead of `python` in the following commands.

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Download the configured model

FirstPR AI's local app currently uses `llama3.2:3b`.

```bash
ollama pull llama3.2:3b
```

Make sure Ollama is running. If it is not already running as a background service, start it in a separate terminal:

```bash
ollama serve
```

### 5. Start the app

```bash
python app.py
```

Open [http://127.0.0.1:7860](http://127.0.0.1:7860).

## 💡 How to use it

1. Start Ollama and make sure the configured model is available.
2. Run `python app.py` and open the local Gradio URL.
3. Select one of the five agent skills.
4. Paste the relevant GitHub issue or project context.
5. Ask FirstPR AI for guidance and review its response critically.
6. Verify suggested files, commands, and technical claims against the real repository before acting.

For best results, include an issue title, expected behavior, actual behavior, reproduction steps, and relevant error messages when available.

## ☁️ Hosted deployment configuration

The hosted frontend is `web/index.html`; its API handler is `web/api/chat.py`.

Configure these environment variables in the Vercel project:

| Variable | Required? | Description |
| --- | --- | --- |
| `GROQ_API_KEY` | Yes | Secret API key used by the hosted backend. |
| `GROQ_MODEL` | No | Groq model name; defaults to `llama-3.3-70b-versatile`. |

Add secrets through Vercel Project Settings → Environment Variables. **Never commit API keys to Git.** Hosted mode sends prompts to Groq; local mode uses Ollama independently.

## 🧪 Run checks

From the repository root:

```bash
python -m compileall -q app.py skill_registry.py web/api tests
python -m unittest discover -s tests -v
```

The regression tests mock the Ollama request and do not require a running model or network access. GitHub Actions runs the syntax check and test suite on pull requests and pushes to `main`.

These automated checks validate syntax and selected application behavior. They do not verify the quality of model-generated advice or replace a live end-to-end check of the Ollama and Groq integrations.

## 🗂️ Project structure

```text
FirstPR-AI/
├── app.py                    # Local Gradio application
├── skill_registry.py         # Shared skill registry and Markdown loader
├── skills/                   # Source-of-truth skill instructions
│   ├── issue-analyzer/
│   ├── codebase-explorer/
│   ├── test-planner/
│   ├── pr-mentor/
│   └── contribution-safety-checker/
├── screenshots/              # README screenshots
├── web/
│   ├── index.html             # Hosted browser interface
│   └── api/
│       └── chat.py            # Vercel / Groq API handler
├── tests/
│   └── test_app.py            # Network-free regression tests
├── .github/workflows/ci.yml   # GitHub Actions checks
├── requirements.txt
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
└── README.md
```

## 🔐 Privacy and limitations

- Local mode sends prompts to the Ollama endpoint configured in `app.py`.
- Hosted mode sends prompts to Groq through the Vercel API.
- Do not submit passwords, access tokens, private keys, or confidential project data.
- AI output can be inaccurate or incomplete. Verify commands, repository paths, and technical claims before acting.
- FirstPR AI provides guidance; it does not automatically modify repositories, guarantee a safe contribution, or replace project maintainers and code review.

## 🤝 Contributing

Bug reports, documentation improvements, and focused code contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md) before contributing or reporting a security concern.

## 📄 License

Released under the [MIT License](LICENSE).
