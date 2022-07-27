import os
import sys

arg = sys.argv
assert len(arg) == 2

arg = sys.argv[1]
assert isinstance(arg, str)


if arg == "debug":
    commands = [
        'python setup.py sdist bdist_wheel',
        'git add .',
        'git commit -m "|^w^ >"',
        'git push',
    ]
elif arg == "build":
    commands = [
        'python setup.py sdist bdist_wheel',
        'git add .',
        'git commit -m "|^w^ >"',
        'git push',
        'twine upload dist/*'
    ]
else:
    commands = []

for command in commands:
    os.system(command)
