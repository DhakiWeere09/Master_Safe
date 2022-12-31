import os


def setup():
    os.mkdir("SAFE")
    os.mkdir("SAFE\\.data")
    os.mkdir("SAFE\\.data\\.clone_tree")
    os.system("attrib {0} +h +s".format("SAFE\\.data"))
    with open("SAFE\\.data\\.pass.MS", "w+") as f_pass:
        f_pass.write("ERROR401")
