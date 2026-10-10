# 🤖 FirstPR AI

> **Your local AI mentor for open-source contributions.** Understand issues, explore unfamiliar codebases, plan tests, prepare pull requests, and review contribution safety — with a local Ollama model.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange?logo=gradio&logoColor=white)
![Ollama](https://img.shields.io/badge/AI-Ollama-black)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/Tests-unittest-blue)

FirstPR AI is a beginner-friendly, local-first assistant for people making their first open-source contributions. It combines a simple Gradio interface with focused skill guides and a model served by [Ollama](https://ollama.com/). No cloud AI API key is required when using the configured local Ollama endpoint.

## ✨ What can it do?

Choose a skill from the interface and provide the relevant issue or project context.

| Skill | What it helps with |
| --- | --- |
| 🧩 **Issue Analyzer** | Break an issue into a clear problem, requirements, and investigation steps. |
| 🧭 **Codebase Explorer** | Plan how to navigate an unfamiliar repository and find relevant files. |
| 🧪 **Test Planner** | Identify test cases and plan verification before and after a change. |
| 🔀 **PR Mentor** | Organize the steps for preparing a clear, reviewable pull request. |
| 🛡️ **Contribution Safety Checker** | Think through safety checks before changing code or submitting a contribution. |

> **Important:** The skills guide the model; they do not guarantee correct answers or automatically make safe code changes. Review the output and verify commands before using them.

## 🖼️ Screenshots

### Main interface
![FirstPR AI main interface](screenshots/main-interface.png)

### Available agent skills
![FirstPR AI skill selector](screenshots/agent-skills.png)

### App settings
![FirstPR AI settings](screenshots/settings.png)

## 🚀 Run it on your computer

### 1. Install prerequisites

- **Python 3.10+**
- **Ollama** — [Download Ollama](https://ollama.com/download)
- **Git** — [Download Git](https://git-scm.com/downloads)

### 2. Download the project

Open PowerShell or a terminal and run:

```powershell
git clone https://github.com/prabhtheone/FirstPR-AI.git
cd FirstPR-AI
```

### 3. Create a virtual environment

A virtual environment keeps this project's Python packages separate from other projects.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use the environment's Python directly in the following commands: `.venv\Scripts\python.exe -m pip install -r requirements.txt`.

### 4. Install Python dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Download the AI model

FirstPR AI is currently configured to use `llama3.2:3b`. Make sure Ollama is installed, then run:

```powershell
ollama pull llama3.2:3b
```

Keep Ollama running while you use the app. If Ollama is not already running in the background, open a separate terminal and start it with `ollama serve`.

### 6. Start FirstPR AI

From the project folder, run:

```powershell
python app.py
```

Open **http://127.0.0.1:7860** in your browser.

## 🧑‍💻 How to use it

1. **Start Ollama** and confirm the configured model is available.
2. **Launch the app** with `python app.py`.
3. **Open the local URL** shown by Gradio (normally `http://127.0.0.1:7860`).
4. **Choose a skill** from the dropdown, such as *Issue Analyzer*.
5. **Paste useful context** into the GitHub Issue box. Include the issue title, description, expected behavior, and reproduction steps when relevant. For other skills, provide context that matches the selected skill.
6. **Click the action button** and wait for the local model to generate a response.
7. **Review the result critically.** Confirm advice against the repository, documentation, and project contribution guidelines before acting on it.

### Example prompt

```text
Title: Login form accepts an empty password

Expected behavior:
The form should reject an empty password and show a useful validation message.

Actual behavior:
Submitting the form with an empty password continues to the next screen.

Please help me understand the issue, suggest where I should investigate, and list questions to clarify before changing code.
```

Use a real issue from your target repository for the most useful result. Do not paste passwords, access tokens, private keys, or confidential data.

## 🧪 Run the checks

From the repository root:

```powershell
python -m compileall -q app.py tests
python -m unittest discover -s tests -v
```

The unit tests mock the Ollama request, so they do not require a downloaded model or a running Ollama server. GitHub Actions is configured to run the syntax check and regression tests on pushes and pull requests to `main`. These checks verify application behavior at a basic level; they do **not** measure the quality of model-generated advice.

## 🗂️ Project structure

```text
FirstPR-AI/
├── app.py
├── requirements.txt
├── skills/
│   ├── issue-analyzer/SKILL.md
│   ├── codebase-explorer/SKILL.md
│   ├── test-planner/SKILL.md
│   ├── pr-mentor/SKILL.md
│   └── contribution-safety-checker/SKILL.md
├── tests/
│   └── test_app.py
├── screenshots/
│   ├── main-interface.png
│   ├── agent-skills.png
│   └── settings.png
├── .github/workflows/ci.yml
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## 🔐 Privacy and limitations

- The app sends prompts to the Ollama endpoint configured in `app.py`; check that configuration before using sensitive information.
- A local model can still produce inaccurate, incomplete, or misleading output. Verify important claims and commands.
- Never submit secrets, credentials, private keys, or confidential project information.
- The repository does not contain the model weights or your local Python virtual environment.
- This project is a guidance tool, not a replacement for maintainers, project-specific contribution rules, code review, or tests.

## 🛣️ Roadmap

- [ ] Add a configurable model and Ollama endpoint.
- [ ] Add a short recorded walkthrough.
- [ ] Expand beginner-friendly contribution examples.
- [ ] Improve the skill guides using feedback from new contributors.

## 🤝 Contributing

Bug reports, ideas, documentation improvements, and code contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and use the repository's issue templates when opening a report or feature request.

## 📄 License

Released under the [MIT License](LICENSE).
