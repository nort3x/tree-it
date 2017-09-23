#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-

import argparse
import os
from termcolor import colored

all_dir_count = 0
all_file_count = 0


def list_me_dir_file(ls, path):
    dirs = []
    files = []
    for x in ls:
        if os.path.isdir(path + "/" + x):
            dirs.append(x)
        if os.path.isfile(path + "/" + x):
            files.append(x)
    return sorted(dirs, key=str.lower) + sorted(files, key=str.lower)


def better_size(size_in_byte, dont_rount=False):
    if dont_rount:
        if len(str(size_in_byte)) >= 3:  # kilo
            if len(str(size_in_byte)) >= 6:  # mega
                s = str(size_in_byte)[:len(str(size_in_byte)) - 6]
                s = s + "." + str(size_in_byte)[len(s):] + " Mb"
                return s
            else:
                s = str(size_in_byte)[:len(str(size_in_byte)) - 3]
                s = s + "." + str(size_in_byte)[len(s):] + " Kb"
                return s
        else:
            return str(size_in_byte)
    # do round
    else:
        if len(str(size_in_byte)) >= 3:  # kilo
            if len(str(size_in_byte)) >= 6:  # mega
                s = str(size_in_byte)[:len(str(size_in_byte)) - 6]
                s = s + "." + str(size_in_byte)[len(s):]
                s = round(float(s))
                return str(s) + " Mb"
            else:
                s = str(size_in_byte)[:len(str(size_in_byte)) - 3]
                s = s + "." + str(size_in_byte)[len(s):]
                s = round(float(s))
                return str(s) +" Kb"
        else:
            return str(size_in_byte)


# lets tree

def tree(path, number, size=False,dontround=False):

    global all_dir_count, all_file_count

    if os.path.isdir(path):
        try:
            if "//" in path:
                path = path.replace("//", "/")
            print("   │" * number + "---⚈" + colored(path, color="yellow"))
            all_dir_count += 1
            for x in list_me_dir_file(sorted(os.listdir(path)), path):
                if os.path.isdir(path + "/" + x):
                    print("   │" * (number + 1))
                    tree(path + "/" + x, number + 1, size, dontround)
                if os.path.isfile(path + "/" + x):
                    all_file_count += 1
                    if size:
                        s = "   │" * (number + 1) + x
                        total_number = 70 - len(s)
                        if total_number <= 2:
                            total_number = 8
                        print(s + " " * total_number + better_size(os.path.getsize(path + "/" + x),dontround))
                    else:
                        print("   │" * (number + 1) + x)
            print("   │" * (number) + "   ╰")
            print("   │" * number)
        except:
            exit()
    else:
        print(colored("[Err]", color="red") + " " + path + " is Not a directory")

parser = argparse.ArgumentParser(description="Dir{file Tree scheming tool")
parser.add_argument("Directory", nargs='?', help="Point to start scheming", default=os.getcwd())
parser.add_argument("-s", "--size", help="also print file size", action="store_true")
parser.add_argument("-v", "--verbose", help="Don't round size", action="store_true")

args = parser.parse_args()
tree(args.Directory, 0, args.size, args.verbose)
s = "Directoris: " + str(all_dir_count)+" , Files: " + str(all_file_count)
print(colored("┌"+"─"*(len(s)+2)+"┐"+"\n│ ",color="green")+ s +colored(" │\n└"+"─"*(len(s)+2)+"┘",color="green"))
