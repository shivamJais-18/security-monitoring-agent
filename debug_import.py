import importlib
m = importlib.import_module('utils.scaledown')
print('module', m)
print('file', m.__file__)
print('attrs', [a for a in dir(m) if not a.startswith('__')])
print('\n--- source start ---\n')
print(open(m.__file__, encoding='utf-8').read())
print('\n--- source end ---\n')
