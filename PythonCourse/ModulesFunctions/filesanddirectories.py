import os


def list_directories(s):

    def dir_lists(d):
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print("directories listig of " + s)
        dir_lists(s)
    else:
        print(s + " does not exist")

list_directories('.')

#only thing to create scope in python are modules, functions, classes

