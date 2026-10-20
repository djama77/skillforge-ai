import re

def inspect_skill(content: str) -> dict:
    checks = {
        'frontmatter': content.startswith('---\n') and content.count('---') >= 2,
        'name': bool(re.search(r'(?m)^name: [a-z0-9-]+$', content)),
        'description': bool(re.search(r'(?m)^description: .+', content)),
        'source_traceability': '## Provenance' in content and 'Source:' in content,
        'source_hash': 'SHA256' in content,
        'source_limit_disclosed': 'Coverage:' in content,
        'untrusted_source_warning': 'untrusted' in content.lower(),
        'human_review': 'Human review' in content,
    }
    return {'passed': sum(checks.values()), 'total': len(checks), 'checks': checks, 'warning': 'Structural checks only; factual reliability and prompt-injection resistance are NOT certified.'}
