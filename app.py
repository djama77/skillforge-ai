import tempfile
from pathlib import Path
import streamlit as st
from skillforge.pipeline import build

st.set_page_config(page_title='SkillForge AI V2',page_icon='🛠️',layout='wide')
st.title('🛠️ SkillForge AI V2')
st.caption('Local-first • Source-grounded drafts • Optional Ollama • Structural quality checks')
with st.sidebar:
    st.header('Settings')
    title=st.text_input('Skill name','Document Expert')
    target=st.selectbox('Export target',['codex','claude','copilot','opencode'])
    use_ai=st.checkbox('Use local Ollama',value=False)
    model=st.text_input('Ollama model','qwen2.5:1.5b',disabled=not use_ai)
file=st.file_uploader('Upload PDF, Markdown or TXT',type=['pdf','md','txt'])
if file and st.button('Build skill',type='primary'):
    if len(file.getvalue())>20*1024*1024:st.error('20 MB file limit exceeded')
    else:
        with tempfile.TemporaryDirectory() as tmp:
            source=Path(tmp)/Path(file.name).name
            source.write_bytes(file.getvalue())
            try:
                result=build(str(source),str(Path(tmp)/'output'),title,use_ai,model,target)
                st.success('Draft generated. Human validation is required.')
                st.metric('Structural checks',f"{result['report']['passed']}/{result['report']['total']}")
                st.warning(result['report']['warning']);st.json(result['report']['checks'])
                st.download_button('Download SKILL.md',result['content'],'SKILL.md','text/markdown')
                st.code(result['content'][:6000],language='markdown')
            except Exception as exc:st.error(f'Generation failed: {exc}')
