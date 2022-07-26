import os

from matplotlib.style import context

ROOT = __file__
js_file = os.path.join(os.path.dirname(ROOT), "sign.js")


with open(js_file, "r") as f:
    file = f.read()
    
import js2py

script = js2py.EvalJs()
script.execute(file)
print(script.e("hello"))