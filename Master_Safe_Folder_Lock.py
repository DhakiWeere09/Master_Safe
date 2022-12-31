import os
# assert os.path.exists("SAFE") or os.path.exists("MS_hidden-00978687##afd")


def folder_lock():
    # os.system("attrib {0} +h +s".format("SAFE\\.data"))
    os.system("rename {0} {1}".format("SAFE", "MS_hidden-00978687##afd"))
    os.system("attrib {0} +h +s".format("MS_hidden-00978687##afd"))
    os.system("icacls {0} /deny {1}:(F)".format("MS_hidden-00978687##afd", os.environ["username"]))


def folder_unlock():
    os.system("icacls {0} /grant {1}:(F)".format("MS_hidden-00978687##afd", os.environ["username"]))
    os.system("attrib {0} -h -s".format("MS_hidden-00978687##afd"))
    os.system("rename {0} {1}".format("MS_hidden-00978687##afd", "SAFE"))
    # os.system("attrib {0} -h -s".format("SAFE\\.data"))
