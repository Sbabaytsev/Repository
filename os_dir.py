import os
import os.path

import shutil

print(os.getcwd())
print(os.listdir())

print(os.path.exists("files.py"))
print(os.path.exists("random.py"))

print(os.path.isfile("random.py"))
print(os.path.isdir(".idea"))

print(os.path.abspath("files.py"))

os.chdir(".idea")
print(os.getcwd())

for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)

shutil.copy("test1.iml", "test2.iml")
for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)

shutil.copytree("tests", "tests/tests")