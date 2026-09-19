import argparse,json,logging
from .ai import generate_ideas,generate_package
def main():
    p=argparse.ArgumentParser(description="YouTube automation engine"); s=p.add_subparsers(dest="cmd",required=True)
    r=s.add_parser("research"); r.add_argument("--count",type=int,default=10)
    n=s.add_parser("package"); n.add_argument("--topic",required=True)
    d=s.add_parser("dry-run"); d.add_argument("--topic",required=True)
    a=p.parse_args(); logging.basicConfig(level=logging.INFO,format="%(levelname)s %(message)s")
    if a.cmd=="research": print(json.dumps(generate_ideas(a.count),indent=2))
    else:
        print(json.dumps(generate_package(a.topic).__dict__,indent=2))
        if a.cmd=="dry-run": print("\nDRY RUN: no network publishing performed.")
if __name__=="__main__": main()
