import importlib, traceback, inspect

try:
    m = importlib.import_module('agents.log_analyzer')
    print('LOADED', getattr(m, '__file__', None))
    print('has_analyze:', hasattr(m, 'analyze_logs'))
    if hasattr(m, 'analyze_logs'):
        f = m.analyze_logs
        print('analyze_logs type:', type(f))
        try:
            print('signature:', inspect.signature(f))
        except Exception:
            print('signature: <uninspectable>')
    print('\nPUBLIC NAMES:')
    for name in sorted(n for n in dir(m) if not n.startswith('_')):
        print(name)
except Exception:
    traceback.print_exc()

# Also try executing analyze_logs if present to see runtime failures (dry run)
try:
    if hasattr(m, 'analyze_logs'):
        print('\nTrying to call analyze_logs with dummy files...')
        try:
            m.analyze_logs('data/scaled_logs/scaled_logs.json', 'data/scaled_logs/analyzed_logs.json')
            print('analyze_logs executed (no exceptions)')
        except Exception:
            traceback.print_exc()
except Exception:
    pass
