import os
from random import randint as rand


def is_dir(f_abspath):
    return os.path.isdir(f_abspath)


def code_gen():
    return rand(10000000, 99999999)


def tree_cloner(f_abspath):
    # print (f_abspath)                                   # --------- [CHECK]
    assert (os.path.exists(f_abspath)), "NON-EXISTING FILE OCCURED"
    # f_b_name = os.path.basename(f_abspath)
    f_newabspath = get_clone_path(f_abspath)

    if os.path.exists(f_newabspath): return
    if is_dir(f_abspath):
        os.mkdir(f_newabspath)
    else:
        open(f_newabspath, "w+")
    # print("File [{0}] added to the log".format(f_b_name))


def get_clone_path(f_abspath):
    lst_temp = f_abspath.split("\\")
    index = lst_temp.index("SAFE")
    for word in [".clone_tree", ".data"]:
        lst_temp.insert(index + 1, word)

    return "\\".join(lst_temp)


def locate_files(path, mode=0):
    os.chdir(path)
    for file in os.listdir(path):
        if file.startswith(".") or file.endswith(".ms"):
            continue
        f_abspath = os.path.abspath(file)
        if mode == 0: tree_cloner(f_abspath)
        if is_dir(f_abspath):
            # print("Found DIR   : " + file)                                 [CHECK]------
            # print("\n")                                                    [CHECK]------
            os.chdir(f_abspath)
            yield from locate_files(f_abspath, mode)
            os.chdir("..")
        else:
            # print("Found FILE  : " + file)                                 [CHECK]------
            yield f_abspath


def lock(path):
    os.chdir(path)
    for file in locate_files(path):
        f_abspath = os.path.abspath(file)
        code = code_gen()
        os.rename(f_abspath, "{0}.ms".format(code))
        with open(get_clone_path(f_abspath), "w") as c_file:
            c_file.write(str(code))

        print("File [{0}] Locked\n".format(os.path.basename(f_abspath)))
        # input()                                                            [CHECK]------
    os.chdir("..")

