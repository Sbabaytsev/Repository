import os
import os.path
import zipfile
with open("ans.txt", "w") as o:
    if zipfile.is_zipfile("main.zip"):
        z = zipfile.ZipFile("main.zip", "r")
        z.extractall()
        os.chdir("main")

        for current_dir, dirs, files in os.walk("."):

            for element in files:
                if element[-3:] == ".py":
                    print(element)
                    print("Current dir = ", "main" + current_dir[1:])
                    print(current_dir, dirs, files)
                    o.write("main" + current_dir[1:] + "\n")
                    break


        z.close()


    else:
        print("File is not a zip-file!")
