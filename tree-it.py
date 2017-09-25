#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-


import argparse
import os
from termcolor import colored

all_dir_count = 0
all_file_count = 0
end_hail = []


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
        if len(str(size_in_byte)) > 3:  # kilo
            if len(str(size_in_byte)) > 6:  # mega
                s = str(size_in_byte)[:len(str(size_in_byte)) - 6]
                s = s + "." + str(size_in_byte)[len(s):] + " Mb"
                return s
            else:
                s = str(size_in_byte)[:len(str(size_in_byte)) - 3]
                s = s + "." + str(size_in_byte)[len(s):] + " Kb"
                return s
        else:
            return str(size_in_byte) + " byte"
    # do round
    else:
        if len(str(size_in_byte)) > 3:  # kilo
            if len(str(size_in_byte)) > 6:  # mega
                s = str(size_in_byte)[:len(str(size_in_byte)) - 6]
                s = s + "." + str(size_in_byte)[len(s):]
                s = round(float(s))
                return str(s) + " Mb"
            else:
                s = str(size_in_byte)[:len(str(size_in_byte)) - 3]
                s = s + "." + str(size_in_byte)[len(s):]
                s = round(float(s))
                return str(s) + " Kb"
        else:
            return str(size_in_byte) + " byte"


# lets tree

def tree(path, number, size=False, dontround=False, jd=False, f=None, fd=None, depth=None):
    global all_dir_count, all_file_count, end_hail
    if depth is not None:
        if number-1 >= int(depth):
            return
    if os.path.isdir(path):  # check if dir

        if "//" in path:
            path = path.replace("//", "/")

        if jd:  # just directory ()

            try:
                if fd is not None:
                    if fd in path:
                        # print("   │" * number)
                        print("   │" * number + "    " + colored("┌" + "─" * (len(path) + 2) + "┐",
                                                                 color="green") + "\n" + "   │" * (
                                  number) + "---⚈" + colored("│ ", color="green")
                              + colored(path, color="red") + colored(" │", color="green") + "\n" + "   │" * number
                              + colored("    " + "└" + "─" * (len(path) + 2) + "┘", color="green"))

                        # end of this mad print
                        end_hail.append(path)
                        all_dir_count += 1
                        for x in list_me_dir_file(sorted(os.listdir(path)), path):
                            if os.path.isdir(path + "/" + x):
                                print("   │" * (number + 1))
                                tree(path + "/" + x, number + 1, size, dontround, jd, f, fd, depth)


                    else:
                        print("   │" * number + "---⚈" + colored(path, color="yellow"))
                        all_dir_count += 1
                        for x in list_me_dir_file(sorted(os.listdir(path)), path):
                            if os.path.isdir(path + "/" + x):
                                print("   │" * (number + 1))
                                tree(path + "/" + x, number + 1, size, dontround, jd, f, fd, depth)
                else:
                    print("   │" * number + "---⚈" + colored(path, color="yellow"))
                    all_dir_count += 1
                    for x in list_me_dir_file(sorted(os.listdir(path)), path):
                        if os.path.isdir(path + "/" + x):
                            print("   │" * (number + 1))
                            tree(path + "/" + x, number + 1, size, dontround, jd, f, fd, depth)
            except Exception as e:
                print(e)
                exit()

                # jd end




        else:
            try:
                if str(fd) in path:
                    pass
                else:
                    print("   │" * number + "---⚈" + colored(path, color="yellow"))
                all_dir_count += 1
                for x in list_me_dir_file(sorted(os.listdir(path)), path):
                    if os.path.isdir(path + "/" + x):
                        if fd is not None:
                            if fd in path + "/" + x:
                                path1 = path + "/" + x
                                print("   │" * number + "    " + colored("┌" + "─" * (len(path1) + 2) + "┐",
                                                                         color="green") + "\n" + "   │" * (
                                          number) + "---⚈" + colored("│ ", color="green")
                                      + colored(path1, color="red") + colored(" │",
                                                                              color="green") + "\n" + "   │" * number
                                      + colored("    " + "└" + "─" * (len(path1) + 2) + "┘", color="green"))
                                end_hail.append(path1)
                                tree(path1, number + 1, size, dontround, jd, f, fd, depth)

                            else:
                                print("   │" * (number + 1))
                                tree(path + "/" + x, number + 1, size, dontround, jd, f, fd, depth)
                        else:
                            print("   │" * (number + 1))
                            tree(path + "/" + x, number + 1, size, dontround, jd, f, fd, depth)

                    if os.path.isfile(path + "/" + x):
                        all_file_count += 1
                        if f is not None:
                            if f in x:
                                end_hail.append(path + x)
                                if size:
                                    total_number = 6
                                    s = "   │" * number + "   │" + colored("┌" + "─" * (len(x) + 2) + "┐",
                                                                           color="green") + "\n" + "   │" * (
                                        number) + "   │" + colored("│ ", color="green") + colored(x,
                                                                                                  color="red") + colored(
                                        " │", color="green") + " " * total_number + better_size(
                                        os.path.getsize(path + "/" + x),
                                        dontround) + "\n" + "   │" * number + "   │" + colored(
                                        "└" + "─" * (len(x) + 2) + "┘", color="green")
                                    print(s)
                                else:
                                    s = "   │" * number + "   │" + colored("┌" + "─" * (len(x) + 2) + "┐",
                                                                           color="green") + "\n" + "   │" * (
                                        number) + "   │" + colored("│ ", color="green") + colored(x,
                                                                                                  color="red") + colored(
                                        " │", color="green") + "\n" + "   │" * number + "   │" + colored(
                                        "└" + "─" * (len(x) + 2) + "┘", color="green")

                                    print(s)

                            else:
                                if size:
                                    s = "   │" * (number + 1) + x
                                    total_number = 70 - len(s)
                                    if total_number <= 2:
                                        total_number = 8
                                    print(s + " " * total_number + better_size(os.path.getsize(path + "/" + x),
                                                                               dontround))
                                else:
                                    print("   │" * (number + 1) + x)
                        else:
                            if size:
                                s = "   │" * (number + 1) + x
                                total_number = 70 - len(s)
                                if total_number <= 2:
                                    total_number = 8
                                print(s + " " * total_number + better_size(os.path.getsize(path + "/" + x), dontround))
                            else:
                                print("   │" * (number + 1) + x)

                print("   │" * (number) + "   ╰")
                print("   │" * number)
            except:
                exit()

    else:  # err of not a dir
        print(colored("[Err]", color="red") + " " + path + " is Not a directory")


parser = argparse.ArgumentParser(description="Dir{file Tree listing tool")
parser.add_argument("Directory", nargs='?', help="Point to start listing (default current directory)",
                    default=os.getcwd())
parser.add_argument("-f", "--findfile", metavar="", help="search and find specific file (provide part of file name)")
parser.add_argument("-fd", "--finddir", metavar="", help="find specific directory (provide part of directory name)")
parser.add_argument("-d", "--depth", metavar="", help="Depth of listing directories")
parser.add_argument("-s", "--size", help="also list files size", action="store_true")
parser.add_argument("-v", "--verbose", help="Don't round size", action="store_true")
parser.add_argument("-jd", "--justdir", help="Just show directories", action="store_true")
args = parser.parse_args()
if str(args.Directory) == str(os.getcwd()):
    d = os.getcwd()
else:
    d = os.getcwd() +"/"+ args.Directory

tree(d, 0, args.size, args.verbose, args.justdir, args.findfile, args.finddir, args.depth)
# end hail (search result)
try:

    if len(end_hail) > 1:
        answer = input("\n\n\n# found " + colored(str(len(end_hail)),
                                                  color="yellow") + " search result Do you want to list them all here? <y/N>: ")
        if ("y" == answer) or ("Y" == answer) or ("Yes" in answer) or ("yes" in answer):
            for x in list_me_dir_file(end_hail, ""):
                if os.path.isdir(x):
                    print("Directory:   " + colored(x, color="green"))
                if os.path.isfile(x):
                    print("File:        " + colored(x, color="green"))
        else:
            pass
    elif len(end_hail) == 1:
        for x in list_me_dir_file(end_hail, ""):
            print("\n\nyour only result:")
            if os.path.isdir(x):
                print("Directory:   " + colored(x, color="green"))
            if os.path.isfile(x):
                print("File:        " + colored(x, color="green"))

    if all_file_count > 0 or all_dir_count > 0:
        s = "Directoris: " + str(all_dir_count) + " , Files:     " + str(all_file_count)
        print("\n\nTotal number of dirs and files:\n" + colored("┌" + "─" * (len(s) + 2) + "┐" + "\n│ ",
                                                                color="green") + s + colored(
            " │\n└" + "─" * (len(s) + 2) + "┘", color="green"))
except:
    pass
