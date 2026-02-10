from engine.governance.enforcement_engine import evaluate_compliance

def check_governance(snapshot, mandate):
    return evaluate_compliance(snapshot, mandate)
