#!/usr/bin/env python3
import os
import re
import sys


def decode(c):
    return hex(ord(c))


DIR = os.path.dirname(os.path.realpath(__file__)) + "/"

BASE = [
    (r"$", r""),  # https://stackoverflow.com/a/10913081/7833617
    (r" [–-]{1,2} ", r" -- "),
    # ======= #
    # Bullets #
    # ======= #
    (r'^(\s)*"\s*([^"]*\n)(?:\s)*(. .)', r"\1- \2\1\t\3"),  # quotes
    (r"^(\d)+\) ", r"\1. "),  # digits formatting
    (r"^[✧#]\s*", r"- "),  # needs to preface header operations
    (r"^(?:[!²«$]|\"\s+)\s*([^\[])", r"* \1"),
    (r"^[−Ø]\s*", r"\t\t- "),
    (r"^\s*[★☞➜➔]\s*", r"\t* "),
    (r"^\s*[–•]\s*|^o ([A-Z])", r"\t- \1"),
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
    (r'^(\s*. )(.{3,45}?)(: *[^"])', r"\1**\2**\3"),  # term/definition
    (r"[““””]", r'"'),
    (r"\n([,.])", r" \1"),
    # ========== #
    # Whitespace #
    # ========== #
    (
        r"^(\s)*(. \*\*.+\*\*:.*\n)(?:\s)*(. .)",
        r"\1\2\1\t\3",
    ),
    (  # indent next bp after term/definition
        r"^((?:.|\d+\.) .*\n)\t{2,}((?:.|\d+\.) .*\n)",
        r"\1\t\2",
    ),  # removes 2+ tab gaps
    (
        r"^(\t(?:.|\d+\.) .*\n)\t{3,}((?:.|\d+\.) .*\n)",
        r"\1\t\2",
    ),  # removes 2+ tab gaps (ident)
    (r"^(\d+\. .*\n)- ", r"\1\t- "),  # indent fater num lists
    (r" {2,}", r" "),
    (r"\n\n\t(.\s*)\b", r"\n\t\1"),
    (r"^(.){1,3}$", r"<!--\1-->"),  # remove lines with three or less characters
    (r"^\s*\n(\t+. .)", r"\1"),  # gaps between bps
    (r" {1,3}\t",r"    "), # hidden tab
    (r"\t",r"    "), # tab to four spaces
]

STYLES = dict([(k, []) for k in {"C100", "16A", "E29"}])
STYLES["C100"] = [
    (r"\n[““””]", r' "'),
    (r'^\s*((?:.|\d+\.)? ?)(♫|(?:[“"].*[”"].*)$)', r"\t\1> \2"),  # quotes
    (r"^(\s)*.(> )", r"\1\2"),  # botch
    (r" v ", r"\n\t- "),
]
STYLES["16A"] = [(r"~([\\a-Z])", r"\vec \1")]
STYLES["E29"] = [
    ("[\uE000-\uF8FF]", r"-"),
    (r"[•]", r"-"),
    (r"[▪]", r"\t-"),
]


def main(fname, flags):
    styling = "DEFAULT ONLY"
    styling = next((flag for flag in flags if flag in STYLES.keys()), None)
    print("STYLING: " + styling)

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
            for old, new in STYLES[styling] + BASE:
                print(old)
                data = re.sub(old, new, data, flags=re.M)
            fout.write(data)


if __name__ == "__main__":
    if len(sys.argv) < 1:
        exit("filename needs to be passed in")
    if not os.path.isfile(DIR + sys.argv[1]):
        exit("file passed in DNE")
    if str(sys.argv[1]).count(".") > 1:
        exit("filename cannot have periods")
    main(DIR + sys.argv[1], sys.argv[2:])
