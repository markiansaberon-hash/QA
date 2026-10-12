# QA Engineering Portfolio

[![QA Tests](https://github.com/markiansaberon-hash/QA/actions/workflows/tests.yml/badge.svg)](https://github.com/markiansaberon-hash/QA/actions/workflows/tests.yml)

Hands-on QA engineering work by **Mark Ian Saberon** (Lead QA Engineer, 11+ years): API test automation with pytest, BDD with Gherkin, and LLM evaluation for AI features.

## What's inside

| Folder | What it shows |
| --- | --- |
| [`python-pytest`](python-pytest) | API test automation with pytest: session-scoped fixtures with setup/teardown, parametrized data-driven tests, markers, JSON schema validation, HTML reports |
| [`bdd-cucumber`](bdd-cucumber) | BDD with Gherkin and pytest-bdd: reusable Given/When/Then steps, Scenario Outlines, positive and negative API scenarios |
| [`deepeval`](deepeval) | LLM evaluation with DeepEval: GEval correctness metrics and test case shapes for RAG, chatbot and tool-use |
| [`deepeval-chat-support`](deepeval-chat-support) | Evaluating a chat-support style LLM with DeepEval (in progress) |
| [`ragas-basics`](ragas-basics) | RAG evaluation basics with Ragas (in progress) |
| [`agentic-ai-jev`](agentic-ai-jev) | Notes on agentic AI and LLM-as-a-judge tooling (in progress) |

## CI

Every push runs the pytest and BDD suites in GitHub Actions and uploads an HTML test report as a build artifact.

## Run locally

```bash
git clone https://github.com/markiansaberon-hash/QA.git
cd QA
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# API tests
cd python-pytest && pytest && cd ..

# BDD tests
cd bdd-cucumber && pytest && cd ..
```

DeepEval tests run locally with [Ollama](https://ollama.com) (`llama3.2`), so no API key is needed. See each folder's README for details.

## Tech

Python, pytest, pytest-bdd (Gherkin), requests, jsonschema, pytest-html, DeepEval, GitHub Actions