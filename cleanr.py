#!/usr/bin/env python3
import os
import re
import sys
import shutil

"""
todo what this does
"""


DIR = os.path.dirname(os.path.realpath(__file__)) + "/"

STYLES = dict([(k, []) for k in {"C100", "16A", "E29"}])
STYLES["C100"] = [
    (r"$", r""),  # https://stackoverflow.com/a/10913081/7833617
    # Bullet points
    (r"^(\d)+\) ", r"\1. "),
    (r"^[✧#]\s*", r"- "),  # this line needs to preface header operations
    (r"^−\s*", r"\t\t- "),
    (r"^!\s*([^\[])", r"* \1"),
    (r"^(?:[•☞➜]|o ([A-Z]))\s*", r"\t- \1"),
    (r"\)\(", r")\n\t- ("),  # Parenthesis Unjoin (i.e sources)
    (r"\n\(", r" ("),  # Parenthesis 2
    (r"([^\n]{0,55} ?)\n( ?[a-z])", r"\1 \2"),  # word-wrap
    (r"^[A-Z]([\w]* |o[rf]|and|&{1,}\w+)\n+(\t*[A-Z-])", r"# \1\n\n"),  # Header
    # (r"(#.*?)\n+([0-9a-zA-Z])", r"\1\n\n- \2"),  # spacing after header
    # (r" {2,}", r" "),
]

# todo figure out how to find tabs 'dynamically'


def main(fname, flags):
    styling = flags[0] if (flags and flags[0] in STYLES.keys()) else "C100"
    copy = fname.split(".")[0] + "-clean.md"
    if (
        "-d" not in flags
        and os.path.isfile(copy)
        and "Y"
        != input(
            "clean copy exists, do you want to overwrite and continue? [y/n]\n"
        ).upper()[0]
    ):
        exit()

    with open(fname, "r") as fin:
        data = fin.read().strip()
        with open(copy, "w") as fout:
            for old, new in STYLES[styling]:
                data = re.sub(
                    old,
                    new,
                    data,
                    flags=re.M,
                )
            fout.write(data)


if __name__ == "__main__":
    if len(sys.argv) < 1:
        exit("filename needs to be passed in")
    if not os.path.isfile(DIR + sys.argv[1]):
        exit("file passed in DNE")
    if str(sys.argv[1]).count(".") > 1:
        exit("filename cannot have periods")
    main(DIR + sys.argv[1], sys.argv[2:])
