import time
import debugpy

debugpy.connect(("localhost", 6688))

#python -m debugpy --listen 5678 ./myscript.py
#debugpy.connect(('xxx.xxx.xxx.xxx', 5678))