# QA

Personal learning repo for QA engineering — LLM evaluation, test automation, and tooling experiments.

## About

This repo documents hands-on learning across different QA topics. Each folder represents a tool or concept being explored, with working code and notes.

## Structure

```
QA/
├── CLAUDE.md       # Project context, git workflow, and setup notes
├── README.md       # This file
└── DeepEval/       # LLM evaluation using DeepEval + Ollama
    └── tests/
        ├── test_1.py   # GEval correctness metric
        └── test_2.py   # LLMTestCase shapes (RAG, chatbot, tool-use)
```

## Topics

### DeepEval
LLM evaluation framework for testing AI outputs. Tests run locally using [Ollama](https://ollama.com) with `llama3.2` — no API key required.

**Run tests:**
```bash
source venv/bin/activate
ollama serve          # in a separate terminal
cd DeepEval
deepeval test run tests/test_1.py
```

## Setup

```bash
git clone git@github-personal:markiansaberon-hash/QA.git
cd QA
python3 -m venv venv
source venv/bin/activate
pip install deepeval python-dotenv litellm
```

> See `CLAUDE.md` for full git workflow, SSH setup, and known gotchas.
