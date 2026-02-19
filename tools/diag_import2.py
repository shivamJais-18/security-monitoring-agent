import importlib, traceback, inspect, sys
from pathlib import Path

p = Path('agents/log_analyzer.py').resolve()
print('FILE PATH:', p)
print('EXISTS:', p.exists())
print('SIZE:', p.stat().st_size)
print('\n--- FILE PREVIEW ---')
with open(p, 'r', encoding='utf-8') as fh:
    for i, line in enumerate(fh, 1):
        if i > 60:
            break
        print(f'{i:03}: {line.rstrip()}')

print('\n--- IMPORT MODULE ---')
try:
    m = importlib.import_module('agents.log_analyzer')
    print('MODULE FILE:', getattr(m, '__file__', None))
    keys = [k for k in m.__dict__.keys() if not k.startswith('_')]
    print('PUBLIC KEYS:', keys)
    print('HAS analyze_logs:', 'analyze_logs' in m.__dict__)
    # show source lines where analyze_logs is defined if present
    if 'analyze_logs' in m.__dict__:
        try:
            print('inspect.getsource(analyze_logs):')
            print(inspect.getsource(m.analyze_logs))
        except Exception as e:
            print('could not get source:', e)
except Exception:
    traceback.print_exc()

print('\n--- RAW GLOBALS DUMP (first 40 names) ---')
try:
    for i, k in enumerate(list(m.__dict__.keys())[:40], 1):
        print(f'{i:02}: {k} -> {type(m.__dict__[k])}')
except Exception:
    pass

print('\nDONE')
