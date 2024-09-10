import os


os.system("/home/chinmay/miniconda3/envs/yolo2/bin/python detect.py --weights gelan-c.pt --source 0  --device 0 --classes 0 --nosave")

# pid= os.fork()

# if pid == 0:
#     os.system("/home/chinmay/miniconda3/envs/yolo2/bin/python detect.py --weights gelan-c.pt --source 0 --device 0 --classes 0")
# else:
#     os.system("/home/chinmay/miniconda3/envs/yolo2/bin/python detect.py --weights gelan-c.pt --source 2 --device 0 --classes 0")