import importlib.util,os,sys
EP=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,EP)
from respell import respell
spec=importlib.util.spec_from_file_location("src",f"{EP}/episode_src.py"); E=importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
src=open(f"{EP}/episode_src.py").read()
head=src[:src.index("LINES = [")]; tail=src[src.index("\ndef _L("):]
body="LINES = [\n"+"".join(f" ({respell(t)!r},\n  {sh!r},\n  {o!r}),\n" for t,sh,o in E.LINES)+"]\n"
open(f"{EP}/episode.py","w").write(head+body+tail)
print("pre ok",len(E.LINES))
