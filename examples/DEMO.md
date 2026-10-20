# SkillForge AI: 2-minute demo

## Input
Use [sample.md](sample.md), a small statistics methodology example.

## Install

```bash
python -m pip install -e ".[ui,dev]"
```

## Generate a skill (no model required)

```bash
skillforge examples/sample.md --title "Statistical Data Quality" --target codex --output demo-output
```

## Inspect results

Open `demo-output/codex/SKILL.md`, `quality-report.json`, and `manifest.json`.

The output contains source provenance, a 12,000-character excerpt limit, and a human-review checklist. Structural checks do **not** certify factual correctness or resistance to malicious content.

## Optional local Ollama

First install Ollama and pull a supported local model:

```bash
ollama pull qwen2.5:1.5b
skillforge examples/sample.md --title "Statistical Data Quality" --ollama --model qwen2.5:1.5b
```

The app only contacts Ollama on localhost port 11434. This is optional.

## Web UI

```bash
python -m streamlit run app.py
```

Upload the example Markdown or a permitted PDF, generate a draft, review the checks, and download `SKILL.md`.
