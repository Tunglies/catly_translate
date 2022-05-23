commands = [
    'python setup.py sdist bdist_wheel',
    'git add .',
    'git commit -m "|^w^ >"',
    'git push',
    'twine upload dist/*'
]

import os

for command in commands:
    os.system(command)