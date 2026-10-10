# FirstPR AI

**A local-first AI mentor that helps beginners understand open-source contributions.**

FirstPR AI uses [Ollama](https://ollama.com/) for local language-model inference and [Gradio](https://www.gradio.app/) for its web interface. It is designed to help contributors get oriented before changing code.

## What it includes

FirstPR AI ships with five focused skill guides:

| Skill | Purpose |
|---|---|
| **Issue Analyzer** | Break down an issue and identify what needs investigation. |
| **Codebase Explorer** | Guide a contributor through understanding an unfamiliar codebase. |
| **Test Planner** | Help plan useful tests before and after a change. |
| **PR Mentor** | Help prepare and review a contribution workflow. |
| **Contribution Safety Checker** | Encourage safety checks before making or submitting a change. |

The app sends prompts to the Ollama endpoint configured in `app.py`. With Ollama running locally, you do not need a cloud AI API key.

## Quick start

### 1. Install prerequisites

- Python 3.10 or newer
- [Ollama](https://ollama.com/download)
- Git (recommended)

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

If PowerShell blocks activation, use `.venv\Scripts\python.exe` directly instead.

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Download and start the local model

The app is currently configured to use `llama3.2:3b`.

```powershell
ollama pull llama3.2:3b
ollama serve
```

If Ollama is already running in the background, you do not need to start `ollama serve` again. Keep Ollama running while using the app.

### 6. Launch the app

In a second terminal, from the project folder with the virtual environment activated:

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
├── tests/
│   └── test_app.py
├── .github/workflows/ci.yml
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Tests and development checks

Run these commands from the repository root:

```powershell
python -m compileall -q app.py tests
python -m unittest discover -s tests -v
```

GitHub Actions runs the syntax check and regression tests on pushes and pull requests to `main`. The tests mock the Ollama connection, so they do not download a model or require a running Ollama server. The workflow does not evaluate model answer quality.

## Privacy and limitations

- The app is designed to use the Ollama endpoint configured in `app.py`; review that configuration before using sensitive information.
- Model output can be incorrect or incomplete. Review suggestions and verify commands before running them.
- Never paste access tokens, passwords, private keys, or confidential project data into prompts.
- The repository does not include local model files or your Python virtual environment.

## Roadmap

- Add a configurable model and Ollama endpoint.
- Add screenshots and a short demo.
- Expand beginner-friendly contribution examples.
- Improve skill guidance using real beginner feedback.

## Contributing

Contributions and suggestions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE).
