import pytest
from skillforge.core import extract,make_skill,save_skill

def test_provenance():
    output=make_skill('Population census methodology','manual.txt','Statistics Expert')
    assert 'statistics-expert' in output and 'manual.txt' in output and 'untrusted' in output

def test_empty_rejected():
    with pytest.raises(ValueError):make_skill('  ','empty.txt')

def test_round_trip(tmp_path):
    source=tmp_path/'example.txt';source.write_text('Data quality checks',encoding='utf-8')
    result=save_skill(str(source),str(tmp_path/'output'),'QA')
    assert result.exists() and 'Data quality checks' in result.read_text(encoding='utf-8')

def test_unsupported(tmp_path):
    path=tmp_path/'bad.docx';path.write_text('x')
    with pytest.raises(ValueError):extract(str(path))
