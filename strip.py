#!/usr/bin/env python3
import os

FOLDER = os.path.dirname(os.path.realpath(__file__)) + "/hugo/content/docs/"
for root, _, files in os.walk(FOLDER):
    for file in [
        os.path.join(root, fn) for fn in files if str(fn).split(".")[-1] == "md"
    ]:
        file = os.path.join(FOLDER, file)
        with open(file, "r") as f:
            lines = f.readlines()

        lines = [line.strip() for line in lines]
        print(lines)
        # with open(file, "w") as f:
        #     f.writelines(lines)
