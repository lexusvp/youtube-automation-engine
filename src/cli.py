import argparse,json
from .ai import generate_ideas,generate_package
def main():
    p=argparse.ArgumentParser(); s=p.add_subparsers(dest="cmd",required=True); r=s.add_parser("research"); r.add_argument("--count",type=int,default=10); n=s.add_parser("package"); n.add_argument("--topic",required=True); a=p.parse_args(); print(json.dumps(generate_ideas(a.count) if a.cmd=="research" else generate_package(a.topic).__dict__,indent=2))
if __name__=="__main__": main()
