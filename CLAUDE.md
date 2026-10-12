# QA — Project Notes for Claude

## What this repo is

QA engineering portfolio and learning repo: API test automation (pytest), BDD (pytest-bdd / Gherkin), and LLM evaluation (DeepEval, Ragas).

---

## Project structure

```
QA/
├── CLAUDE.md                # this file
├── README.md                # portfolio overview
├── requirements.txt         # shared Python dependencies
├── .github/workflows/       # CI: runs pytest + BDD suites on every push
├── python-pytest/           # API tests: fixtures, parametrize, markers, schema validation
├── bdd-cucumber/            # BDD: .feature files + pytest-bdd step definitions
├── deepeval/                # LLM evaluation with DeepEval + Ollama
├── deepeval-chat-support/   # DeepEval for a chat-support style LLM
├── ragas-basics/            # RAG evaluation with Ragas
└── agentic-ai-jev/          # Agentic AI / LLM-as-a-judge notes
```

---

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Running tests

```bash
# API tests
cd python-pytest && pytest

# Only smoke tests
cd python-pytest && pytest -m smoke

# BDD tests
cd bdd-cucumber && pytest
```

### DeepEval (runs locally, no API key)
1. Start Ollama in a separate terminal: `ollama serve`
2. Make sure `llama3.2` is pulled: `ollama list`
3. Run:
```bash
cd deepeval
deepeval test run tests/test_1.py   # DeepEval results table
pytest tests/test_2.py -s           # with print() output
```

---

## Git workflow

```bash
git add <file>          # stage specific files, never `git add -A`
git commit -m "message"
git push origin main
```

### Rules
- Never commit `venv/` or `.env`; both are gitignored.
- API keys live only in `.env`.
- If GitHub push protection blocks a push (exposed secret), rotate the key first, then unblock via the link in the error.
- Intentional demo failures must be marked `xfail` / `expectedFailure` so CI stays green.

---

## Known gotchas

### DeepEval + Ollama: logprobs
Ollama and Groq don't support `logprobs`, which GEval uses for probability-weighted scoring.
Fix: set `litellm.drop_params = True` in the test file. litellm drops unsupported params and GEval falls back to direct 0–1 scoring.

### Folder names
Folders use hyphens, not spaces, so paths work in CI and the terminal.