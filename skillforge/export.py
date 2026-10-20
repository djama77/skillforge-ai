from pathlib import Path
import json
TARGETS = {'codex','claude','copilot','opencode'}
def export_skill(content: str, directory: str, target: str) -> Path:
    if target not in TARGETS: raise ValueError(f'Unknown target: {target}')
    folder = Path(directory)/target
    folder.mkdir(parents=True,exist_ok=True)
    (folder/'SKILL.md').write_text(content,encoding='utf-8')
    (folder/'EXPORT_NOTES.md').write_text(f'# {target} export\n\nPortable SKILL.md draft. Review target-agent installation and discovery conventions before use.\n',encoding='utf-8')
    (folder/'manifest.json').write_text(json.dumps({'target':target,'format':'portable-skill-draft','review_required':True},indent=2),encoding='utf-8')
    return folder
