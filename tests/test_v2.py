import json
import pytest
from skillforge.export import export_skill
from skillforge.pipeline import build
from skillforge.intelligence import ollama_suggest

def test_pipeline(tmp_path):
    source=tmp_path/'source.md';source.write_text('# Survey sampling\nA sample is a subset of a population.',encoding='utf8')
    result=build(str(source),str(tmp_path/'out'),'Survey Expert',target='codex')
    assert result['report']['passed']==result['report']['total']
    assert (tmp_path/'out'/'codex'/'SKILL.md').exists()
    assert json.loads((tmp_path/'out'/'codex'/'quality-report.json').read_text())['passed']==8

def test_targets(tmp_path):
    for target in ['codex','claude','copilot','opencode']:
        assert (export_skill('example',str(tmp_path),target)/'SKILL.md').exists()
    with pytest.raises(ValueError):export_skill('x',str(tmp_path),'invalid')

def test_ollama_rejects_remote():
    with pytest.raises(ValueError):ollama_suggest('text',endpoint='https://remote.example')
