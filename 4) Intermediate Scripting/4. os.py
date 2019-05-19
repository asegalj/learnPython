import os
import shutil
os.system('dir')

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

shutil.move(".\\document.yaml" , ".\\document.2.yaml")
shutil.move(".\\document.2.yaml" , ".\\document.yaml")    