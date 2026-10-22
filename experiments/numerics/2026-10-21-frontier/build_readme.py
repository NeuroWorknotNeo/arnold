"""build_readme.py -- собрать README.md из README_template.md, подставив {{CATALOG}}, {{ISO}}, {{TABLE}}, {{PROFILES}}."""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
import fcat
subprocess.run([sys.executable, os.path.join(HERE, 'make_iso_table.py')], capture_output=True, cwd=HERE)
subprocess.run([sys.executable, os.path.join(HERE, 'make_table.py')], capture_output=True, cwd=HERE)
subprocess.run([sys.executable, os.path.join(HERE, 'profile_table.py'), 'A1', 'A3', 'B1', 'B2', 'B3', 'B3b', 'E1', 'D1'], capture_output=True, cwd=HERE)
L = ['| № | гр. | U | зачем / почему не покрыт |', '|---|---|---|---|']
for e in fcat.CAT:
    u = e['U'].replace('**', '^').replace('*', '·')
    if len(u) > 150:
        u = u[:147] + '… (полностью в `fcat.py`)'
    L.append(f"| {e['id']} | {e['group']} | `{u}` | {e['name']}. {e['why']} |")
t = open(os.path.join(HERE, 'README_template.md')).read()
t = t.replace('{{CATALOG}}', '\n'.join(L))
t = t.replace('{{ISO}}', open(os.path.join(HERE, 'iso_table.md')).read())
t = t.replace('{{TABLE}}', open(os.path.join(HERE, 'table.md')).read())
t = t.replace('{{PROFILES}}', open(os.path.join(HERE, 'profiles.md')).read())
open(os.path.join(HERE, 'README.md'), 'w').write(t)
print('README.md:', len(t), 'символов')
