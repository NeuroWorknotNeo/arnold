"""build_readme.py -- собрать README.md из README_template.md и сгенерированных таблиц (table_short.md, rates.md)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(HERE, 'README_template.md')).read()
t = t.replace('{{TABLE_SHORT}}', open(os.path.join(HERE, 'table_short.md')).read())
t = t.replace('{{RATES}}', open(os.path.join(HERE, 'rates.md')).read())
open(os.path.join(HERE, 'README.md'), 'w').write(t)
print('README.md written')
