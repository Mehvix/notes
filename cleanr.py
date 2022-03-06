#!/usr/bin/env python3
import os
import re
import sys


def decode(c):
    return hex(ord(c))


DIR = os.path.dirname(os.path.realpath(__file__)) + "/"

STYLES = dict([(k, []) for k in {"C100", "16A", "E29"}])
STYLES["C100"] = [
    (r"$", r""),  # https://stackoverflow.com/a/10913081/7833617
    (r" [–-]{1,2} ", r" -- "),
    (r"[“”]", r'"'),
    # ======= #
    # Bullets #
    # ======= #
    (r"^(\d)+\) ", r"\1. "),  # digits formatting
    (r"^[✧#]\s*", r"- "),  # needs to preface header operations
    (r"^[!$\"]\s*([^\[])", r"* \1"),
    (r"^−\s*", r"\t\t- "),
    (r"^[★☞➜➔]\s*", r"\t* "),
    (r"^[–•]\s*|^o ([A-Z])", r"\t- \1"),
    (r'^\s*((?:.|\d+\.)? ?)(♫|(?:[“"].*[”"].*)$)', r"\t\1> \2"),  # quotes
    (r"^\s*((?:.|\d+\.)? ?Results:)\n\t(. )", r"- \1\n\t\2"),  # results
    (r"\)\(", r")\n\t- ("),  # Parenthesis Unjoin (i.e sources)
    (r"\n\(", r" ("),  # Parenthesis 2
    (r"([^\n]{0,55} ?)\n( ?[a-z&(])", r"\1 \2"),  # word-wrap
    # ======= #
    # Headers #
    # ======= #
    (r"^[☛]", r"## "),  # H2 unique
    (r"(^[A-Z][^ .].{2,42}\n)", r"\n## \1\n"),  # Headers
    (r"#+\s*(.*\n+)#+\s*(.*\n+)#+\s*(.*\n+)", r"# \1## \2### \3"),  # H3s
    (r"#{1,2}\s*(.*\n+)#{2,3}\s*(.*\n+)", r"# \1## \2"),  # H2s
    (r"(#.*?)\n+\s*. ([A-Z0-9\"])", r"\1\n\n- \2"),  # spacing after headers
    (r"$\n+#", r"\n\n#"),  # spacing before headers
    (r"(#.*$\n*)\t+(.)", r"\1\2"),  # normalize below header
    # (r"(#.*$\n+[*-].*$)(?:\n\s(. .*))+", r"\1\n\t\2"),  # normalize two down
    (r"^([\s]*). (\d+\.)", r"\1\2"),  # point before numbers
    (r"^([A-Z].{20,})", r"- \1"),  # long lines
    # whitespace
    (r"^((?:.|\d+\.) .*\n)\t{2,}((?:.|\d+\.) .*\n)", r"\1\t\2"),  # removes 2+ tab gaps
    (
        r"^(\t(?:.|\d+\.) .*\n)\t{3,}((?:.|\d+\.) .*\n)",
        r"\1\t\2",
    ),  # removes 2+ tab gaps (ident)
    (r"^(\d+\. .*\n)- ", r"\1\t- "),  # indent fater num lists
    (r" {2,}", r" "),
    (r"\n\n\t(.\s*)\b", r"\n\t\1"),
]
STYLES["16A"] = [
    (r"$", r""),  # https://stackoverflow.com/a/10913081/7833617
    (r" [–-]{1,2} ", r" -- "),
    (r"[“”]", r'"'),
    (r"~([\\a-Z])", r"\vec \1")
    # (r"", r"")
]
STYLES["E29"] = [
    (r"$", r""),  # https://stackoverflow.com/a/10913081/7833617
    (r" [–-]{1,2} ", r" -- "),
    (r"[“”]", r'"'),
    (r"", r"-"),
    (r"•", r"\t-"),
    (r"^[☛]", r"## "),  # H2 unique
    (r"(^[A-Z][^ .].{2,42}\n)", r"\n## \1\n"),  # Headers
    (r"#+\s*(.*\n+)#+\s*(.*\n+)#+\s*(.*\n+)", r"# \1## \2### \3"),  # H3s
    (r"#{1,2}\s*(.*\n+)#{2,3}\s*(.*\n+)", r"# \1## \2"),  # H2s
    (r"(#.*?)\n+\s*. ([A-Z0-9\"])", r"\1\n\n- \2"),  # spacing after headers
    (r"$\n+#", r"\n\n#"),  # spacing before headers
    (r"(#.*$\n*)\t+(.)", r"\1\2"),  # normalize below header
    # (r"(#.*$\n+[*-].*$)(?:\n\s(. .*))+", r"\1\n\t\2"),  # normalize two down
    (r"^([\s]*). (\d+\.)", r"\1\2"),  # point before numbers
    (r"^([A-Z].{20,})", r"- \1"),  # long lines
    # whitespace
    (r"^((?:.|\d+\.) .*\n)\t{2,}((?:.|\d+\.) .*\n)", r"\1\t\2"),  # removes 2+ tab gaps
    (
        r"^(\t(?:.|\d+\.) .*\n)\t{3,}((?:.|\d+\.) .*\n)",
        r"\1\t\2",
    ),  # removes 2+ tab gaps (ident)
    (r"^(\d+\. .*\n)- ", r"\1\t- "),  # indent fater num lists
    (r" {2,}", r" "),
    (r"\n\n\t(.\s*)\b", r"\n\t\1"),
    # (r"", r"")
]


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
                print(old)
                data = re.sub(old, new, data, flags=re.M | re.U)
            fout.write(data)


if __name__ == "__main__":
    if len(sys.argv) < 1:
        exit("filename needs to be passed in")
    if not os.path.isfile(DIR + sys.argv[1]):
        exit("file passed in DNE")
    if str(sys.argv[1]).count(".") > 1:
        exit("filename cannot have periods")
    main(DIR + sys.argv[1], sys.argv[2:])
