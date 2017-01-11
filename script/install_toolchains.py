#!/usr/bin/env python
import sys
import os
from subprocess import call

host = "n/a"
target = "n/a"

def print_help():
    message = "usage: install_toolchain <HOST> <TARGET> \
    \nex. install_toolchain darwin local \
    \nex. install_toolchain darwin android-ndk-r10e"
    print(message)

# very ugly, refactor in the future
def install_toolchain():
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    proj_root = os.path.realpath(curr_dir + "/..")
    download_dir = proj_root + '/download'
    toolchain_dir = proj_root + '/toolchain'
    if host == "darwin-x86_64" and target == "android-ndk-r10e":
        file_name = "android-ndk-r10e-darwin-x86_64.zip"
        if (os.path.isfile(download_dir + '/' + file_name)):
            print("file already exist")
        else:
            # should use system() instead of call()..., or how to change working directory?
            call(["curl", "-o", download_dir + "/" + file_name, "https://dl.google.com/android/repository/android-ndk-r10e-darwin-x86_64.zip"])
        call(["unzip", download_dir + "/" + file_name, "-d", toolchain_dir])
    else:
        print("currently only support HOST:darwin-x86_64, TARGET:android-ndk-r10e")

def main(argv):
    # argv format: <host> <abi>
    # TODO: detect host
    if not len(argv) == 2:
        print_help()
        return
    global host
    global target
    host = argv[0]
    target = argv[1]
    install_toolchain()

if __name__ == '__main__':
    main(sys.argv[1:])
