from pathlib import Path
files = [
    Path('agents/log_analyzer.py'),
    Path('agents/threat_detector.py'),
    Path('agents/playbooks/agents/response_coordinator.py')
]
for p in files:
    print(p, 'exists:', p.exists(), 'size:', p.stat().st_size if p.exists() else 'N/A')
    if p.exists():
        with open(p,'r',encoding='utf-8') as fh:
            lines = fh.readlines()
        print('Preview (first 6 lines):')
        for i,l in enumerate(lines[:6],1):
            print(f'{i:03}: {l.rstrip()}')
    print()
