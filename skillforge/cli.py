import argparse
from .pipeline import build

def main():
    parser=argparse.ArgumentParser(description='SkillForge AI V2')
    parser.add_argument('input')
    parser.add_argument('--output',default='generated-skill')
    parser.add_argument('--title',default='Document Expert')
    parser.add_argument('--target',choices=['codex','claude','copilot','opencode'],default='codex')
    parser.add_argument('--ollama',action='store_true')
    parser.add_argument('--model',default='qwen2.5:1.5b')
    args=parser.parse_args()
    result=build(args.input,args.output,args.title,args.ollama,args.model,args.target)
    print(result['directory']);print(f"Structural checks: {result['report']['passed']}/{result['report']['total']}")
if __name__=='__main__':main()
