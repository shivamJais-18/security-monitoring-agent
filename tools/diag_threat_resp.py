import importlib, traceback, inspect, sys
from pathlib import Path

print('THREAT DETECTOR')
try:
    m = importlib.import_module('agents.threat_detector')
    print('MODULE FILE:', getattr(m,'__file__',None))
    print('HAS detect_threats:', hasattr(m,'detect_threats'))
    print('PUBLIC:', [n for n in dir(m) if not n.startswith('_')])
except Exception:
    traceback.print_exc()

print('\nRESPONSE COORDINATOR (file import)')
try:
    p = Path('agents/playbooks/agents/response_coordinator.py').resolve()
    spec = importlib.util.spec_from_file_location('response_coordinator', str(p))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    print('FILE:', p)
    print('HAS coordinate_response:', hasattr(mod,'coordinate_response'))
    print('PUBLIC:', [n for n in dir(mod) if not n.startswith('_')])
except Exception:
    traceback.print_exc()
