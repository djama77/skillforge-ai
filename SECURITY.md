# Security policy

SkillForge AI V2 is an early-stage prototype. Do not treat generated skills as trusted instructions without review.

## Reporting vulnerabilities

Please do not publish exploitable vulnerabilities or sensitive information in public issues. Contact the repository maintainer through a private GitHub channel if available, or request a private reporting channel without disclosing exploit details.

## Known limitations

- Imported documents are untrusted and may contain prompt-injection instructions.
- Local Ollama is optional; model-generated content may be inaccurate.
- Structural quality checks do not guarantee safety or factual correctness.
- Source excerpts may contain confidential material: review exports before sharing.
- The current extraction pipeline only uses the first 12,000 characters of extracted text in the generated skill.
- The application is intended for trusted local use; do not expose the Streamlit server publicly without additional safeguards.

Dependencies should be kept updated and reviewed before deployment.
