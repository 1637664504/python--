import time
import debugpy

#debugpy.listen(("localhost", 6688))
#debugpy.wait_for_client()
#debugpy.breakpoint()
print('break on this line')

idx = 0
while True:
    print("welcome debbug, idx: ",idx)
    idx=idx+1
    time.sleep(2)

#python -m debugpy --listen 5678 ./myscript.py
#debugpy.connect(('xxx.xxx.xxx.xxx', 5678))