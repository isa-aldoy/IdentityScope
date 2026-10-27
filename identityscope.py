import argparse,fnmatch,json
from pathlib import Path

def matches(pattern,value):
    return any(fnmatch.fnmatchcase(value.lower(),str(p).lower()) for p in (pattern if isinstance(pattern,list) else [pattern]))
def evaluate(policy,action,resource):
    effects=[];unknown=[]
    statements=policy.get("Statement",[])
    for s in (statements if isinstance(statements,list) else [statements]):
        if any(k in s for k in ("Condition","NotAction","NotResource","Principal","NotPrincipal")):
            unknown.append(s.get("Sid","unnamed"));continue
        if matches(s.get("Action",[]),action) and matches(s.get("Resource",[]),resource):effects.append(s.get("Effect"))
    return {"decision":"explicitDeny" if "Deny" in effects else "allowed" if "Allow" in effects else "implicitDeny","complete":not bool(unknown),"unsupported":unknown}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("policy");p.add_argument("action");p.add_argument("resource");a=p.parse_args()
    print(json.dumps(evaluate(json.loads(Path(a.policy).read_text()),a.action,a.resource),indent=2))
