# Contributing to SkillForge AI

Thanks for contributing! Issues, documentation fixes, tests, and small pull requests are welcome.

## Development setup

```bash
git clone https://github.com/djama77/skillforge-ai.git
cd skillforge-ai
python -m pip install -e ".[ui,dev]"
pytest -q
```

## Before opening a pull request

1. Explain the problem and the proposed change.
2. Add or update tests when behavior changes.
3. Run `pytest -q` and include the outcome.
4. Never commit sensitive documents, access tokens, generated private data, or copyrighted manuals without permission.
5. Keep the offline, no-Ollama workflow operational.
6. Document any model limitations and avoid claiming unverified accuracy.

## Good first contributions

- Improve Markdown extraction and text chunking.
- Add tests for PDF edge cases and Unicode.
- Improve accessibility and UI translations.
- Add verified installation adapters for agent-specific conventions.
- Add a reproducible benchmark with documented evaluation datasets.

Please be respectful and constructive in issues and reviews.
