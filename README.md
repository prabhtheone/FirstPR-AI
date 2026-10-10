# FirstPR AI

A local AI mentor for beginners contributing to open source, powered by Ollama and Gradio.

## Features

- Issue Analyzer
- Codebase Explorer
- Test Planner
- PR Mentor
- Contribution Safety Checker

## Requirements

- Python 3.10+
- Ollama
- `llama3.2:3b`

## Setup

Install dependencies:

```powershell
pip install -r requirements.txt
```

Download the model:

```powershell
ollama pull llama3.2:3b
```

Run the application:

```powershell
python app.py
```

Open http://127.0.0.1:7860 in your browser.

## Privacy

The application sends prompts to the locally configured Ollama server. No cloud AI API key is required.

## License

See [LICENSE](LICENSE).
