# FirstPR AI

**A local-first AI mentor that helps beginners understand open-source contributions.**

FirstPR AI uses [Ollama](https://ollama.com/) for local language-model inference and [Gradio](https://www.gradio.app/) for its web interface. It is designed to help contributors get oriented before changing code.

## What it includes

FirstPR AI ships with five focused skill guides:

| 5 Skills | Purpose |
|---|---|
| **Issue Analyzer** | Break down an issue and help identify what needs investigation. |
| **Codebase Explorer** | Guide a contributor through understanding an unfamiliar codebase. |
| **Test Planner** | Help think through useful tests before and after a change. |
| **PR Mentor** | Help prepare and review a contribution workflow. |
| **Contribution Safety Checker** | Encourage safety checks before making or submitting changes. |

The app sends prompts to the Ollama server configured in `app.py`. With Ollama running locally, you do not need a cloud AI API key.

## Quick start

### 1. Install prerequisites

- Python 3.10 or newer
- [Ollama](https://ollama.com/download)
- Git (optional, but useful for contributing)

### 2. Clone the repository

```powershell
git clone https://github.com/prabhtheone/FirstPR-AI.git
cd FirstPR-AI
```

### 3. Create and activate a virtual environment (recommended)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run the commands below using `.venv\Scripts\python.exe` directly instead.

### 4. Install Python dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Download and start a local model

The current setup is configured to use `llama3.2:3b`.

```powershell
ollama pull llama3.2:3b
ollama serve
```

If Ollama is already running in the background, you do not need to start `ollama serve` again. Keep Ollama running while you use the app.

### 6. Launch FirstPR AI

In a second PowerShell terminal, from the project folder with the virtual environment activated:

```powershell
python app.py
```

Open [http://127.0.0.1:7860](http://127.0.0.1:7860) in your browser.

## Project structure

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
├── .github/
│   └── workflows/
│       └── ci.yml
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Privacy and limitations

- The app is designed to use the Ollama endpoint configured in `app.py`; check that configuration before using it with sensitive information.
- Model output can be incorrect or incomplete. Review suggestions and verify commands before running them.
- Do not paste access tokens, passwords, private keys, or confidential project data into prompts.
- The GitHub repository contains the application and skill guides; it does not include your local model files or Python virtual environment.

## Development checks

Run a Python syntax check locally:

```powershell
python -m compileall -q app.py
```

A GitHub Actions workflow runs dependency installation and a syntax check on pushes and pull requests to `main`. It does not test model quality or require an Ollama server.

## Roadmap

- Add automated tests for issue-analysis behavior.
- Add screenshots and a short demo once the UI capture is available.
- Improve error handling for an unavailable local model.
- Expand beginner-friendly contribution examples.

## Contributing

Contributions and suggestions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE).
