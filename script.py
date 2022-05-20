commands = [
    "python setup.py sdist bdist_wheel",
    "git add .",
    'git commit -m "|^w^ >"',
    'git push',
    'pip install ./dist/*.tar.gz'
]

import os

for command in commands:
    os.system(command)