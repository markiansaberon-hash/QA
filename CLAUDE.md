# QA — Project Notes for Claude

## What this repo is

Personal learning repo for QA engineering topics — currently focused on LLM evaluation using DeepEval.
Owned by **markian.saberon@gmail.com** on GitHub under the account `markiansaberon-hash`.

---

## Git setup

### Remote
```
git@github-personal:markiansaberon-hash/QA.git
```

The remote uses the `github-personal` SSH host alias (not `github.com`) because this machine has two GitHub accounts — work and personal. The alias routes to the correct SSH key.

### SSH config (`~/.ssh/config`)
```
Host github-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_personal
```

### Git identity for this repo
```
user.name  = Markian Saberon
user.email = markian.saberon@gmail.com
```
These are set at the repo level (not global) so work commits stay separate.

---

## How to commit and push

```bash
# Stage specific files (never use git add -A — venv/ will sneak in)
git add <file>

# Commit
git commit -m "your message"

# Push
git push origin main
```

### Important rules
- Never commit `venv/` — it's in `.gitignore`
- Never commit `.env` — API keys live there. It's gitignored.
- If GitHub push protection blocks a push (exposed secret), rotate the key first, then unblock via the GitHub link in the error output

---

## Project structure

```
QA/
├── CLAUDE.md          # this file
├── README.md
├── .gitignore
├── venv/              # Python virtualenv — NOT committed
└── DeepEval/
    └── tests/
        ├── test_1.py  # Day 1: GEval correctness metric with Ollama
        └── test_2.py  # Day 2: Three LLMTestCase shapes (RAG, chatbot, tool-use)
```

---

## Running DeepEval tests

### Prerequisites
1. Activate the venv: `source venv/bin/activate`
2. Start Ollama in a separate terminal: `ollama serve`
3. Make sure `llama3.2` is pulled: `ollama list`

### Run a test
```bash
cd DeepEval
deepeval test run tests/test_1.py   # with DeepEval results table
pytest tests/test_2.py -s           # with print() output visible
```

### Known gotcha — logprobs
Ollama and Groq do not support `logprobs`. GEval requires it for probability-weighted scoring.
Fix: `litellm.drop_params = True` in the test file — litellm drops unsupported params before
sending the request, and GEval falls back to direct scoring (model outputs a 0–1 score).

---

## Aliases (in ~/.zshrc)
```bash
cd-deepeval   # cd ~/Documents/projects/QA && claude
```
