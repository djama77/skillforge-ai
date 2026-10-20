from pathlib import Path
from .core import extract,make_skill
from .intelligence import ollama_suggest
from .quality import inspect_skill
from .export import export_skill
import json

def build(input_path: str,output_dir: str,title: str,use_ollama: bool=False,model: str='qwen2.5:1.5b',target: str='codex')->dict:
    text,source=extract(input_path)
    content=make_skill(text,source,title)
    if use_ollama:
        suggestion=ollama_suggest(text,model=model).replace('```','[fence]')
        content+='\n## Local AI suggestions (unverified; review against source)\n\n'+suggestion+'\n'
    output=export_skill(content,output_dir,target)
    report=inspect_skill(content)
    (output/'quality-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    return {'directory':str(output),'report':report,'content':content}
