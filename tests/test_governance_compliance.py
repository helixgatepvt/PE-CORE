from importlib import import_module

evaluate_compliance = import_module(
    "engine.governance.enforcement_engine"
).evaluate_compliance
