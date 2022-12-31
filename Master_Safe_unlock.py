import os
from os import system
from shutil import rmtree


def getrealpath(c_path, code):
    lst = c_path.split("\\")
    lst.pop()
    lst.append("{0}.ms".format(code))
    lst2 = [".data", ".clone_tree"]
    # lst = list(map(lambda x: lst.remove(x), lst2 )) -------------------[usage of LAMBDA]
    for each in lst2:
        lst.remove(each)
    return "\\".join(lst)


def recover(c_abspath, code):
    assert os.path.exists(c_abspath)
    f_base_name = os.path.basename(c_abspath)
    f_real_path = getrealpath(c_abspath, code)
    # print("file_real_path : " + f_real_path)
    # print("file_base_name : " + f_base_name)
    os.remove(c_abspath)
    system("ren {0} {1}".format(f_real_path, f_base_name))
    print("File Recovered : [{0}]\n".format(f_base_name))


def clone_locate(c_path, mode=0):
    os.chdir(c_path)
    for file in os.listdir(c_path):
        c_abspath = os.path.abspath(file)
        if os.path.isdir(c_abspath):
            # print("Found Clone DIR   : [{0}]".format(file))
            os.chdir(file)
            for f_re in clone_locate(c_abspath, 1):
                yield f_re
            os.chdir("..")
            if mode == 0:
                rmtree(file)
        else:
            # print("Found Clone FILE  : [{0}]".format(file))
            yield c_abspath


def unlock(c_root):
    os.chdir(c_root)
    for c_abspath in clone_locate(c_root):
        # print("clone_path : " + c_abspath)
        with open(c_abspath) as c:
            f_code = c.read()
        recover(c_abspath, f_code)


def unlock_single(c_basename):
    # print(os.getcwd())
    # c_basename = str(input("Path : "))
    c_abspath = os.path.abspath(c_basename)
    assert os.path.exists(c_abspath)
    with open(c_abspath) as file:
        code = file.read()
    recover(c_abspath, code)
