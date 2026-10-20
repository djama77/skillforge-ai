# SkillForge AI 🛠️

**Turn PDFs and technical documentation into portable, source-grounded AI agent skills.**

[![Tests](https://github.com/djama77/skillforge-ai/actions/workflows/tests.yml/badge.svg)](https://github.com/djama77/skillforge-ai/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**Local-first · Open source · Optional Ollama · CLI + Streamlit**

SkillForge AI creates `SKILL.md` drafts from your own documents, preserving a source filename, a hash of extracted text, and a visible coverage limit. It is useful for research, statistical methodology, technical manuals and developer documentation.

> **Prototype V2:** Exports are portable drafts in target-labelled folders, **not** verified native installers. Structural quality checks are not factual or security certifications. Human review is essential.

## Quick start

Requirements: Python 3.10 or later.

```bash
git clone https://github.com/djama77/skillforge-ai.git
cd skillforge-ai
python -m pip install -e ".[ui,dev]"
python -m streamlit run app.py
```

Upload a PDF, TXT or Markdown file and select **Build skill**. Download the resulting `SKILL.md`.

## Command-line example

```bash
skillforge examples/sample.md --title "Statistical Data Quality" --target codex --output demo-output
```

Generated files include:

```text
demo-output/
  codex/
    SKILL.md
    manifest.json
    quality-report.json
    EXPORT_NOTES.md
```

See the [reproducible demo](examples/DEMO.md) for a step-by-step walkthrough.

## Optional offline AI with Ollama

Install Ollama and download the model **once** while online:

```bash
ollama pull qwen2.5:1.5b
skillforge examples/sample.md --ollama --model qwen2.5:1.5b
```

Without Ollama, document-to-skill draft generation still works locally. The local Ollama endpoint is restricted to localhost port 11434.

## What V2 does

| Feature | Status |
| --- | --- |
| PDF, TXT and Markdown text extraction | Implemented |
| Portable skill draft with provenance | Implemented |
| Eight structural checks | Implemented |
| Local Ollama suggestions | Implemented; real-model validation pending |
| Codex, Claude, Copilot, OpenCode target folders | Implemented; native compatibility unverified |
| Full-document understanding | Not yet; excerpt limited to 12,000 characters |
| Automated factual verification | Not implemented |

## Tests

```bash
python -m pip install -e ".[dev]"
pytest -q
```

GitHub Actions runs the tests on pushes and pull requests.

## Community

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes, and [SECURITY.md](SECURITY.md) for security considerations. Open an issue to report a bug or propose a feature.

## License

MIT — see [LICENSE](LICENSE). Only upload and redistribute documents you have permission to use.
