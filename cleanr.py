#!/usr/bin/env python3
import os
import sys
import re
import argparse

COURSE_PLACEHOLDER = "@COURSENAME"
DEFAULT_FIN = "unclean.md"
DEFAULT_FOUT = "clean.md"
COURSES = {"c100", "16a", "e-29", "c61"}

parser = argparse.ArgumentParser()
parser.add_argument("--course",
                    "-c",
                    help="Specifies course",
                    default=None,
                    required=False)
parser.add_argument("--fin",
                    "-i",
                    help="Specifies input file. Default: " + DEFAULT_FIN,
                    type=argparse.FileType('r'))
parser.add_argument("--fout",
                    "-o",
                    help="Specifies output file Default: " + DEFAULT_FOUT,
                    type=argparse.FileType('r'))
parser.add_argument("--force",
                    "-f",
                    help="Force overwrite output file, if it already exists",
                    action="store_true")
parser.add_argument("--base",
                    "-B",
                    help="Does not use base rules",
                    action="store_true")
parser.add_argument("--header",
                    "-H",
                    help="Does not use header rules",
                    action="store_true")
parser.add_argument("--verbose",
                    "-v",
                    action="store_true",
                    help="increase output verbosity")

args = parser.parse_args()

if not args.verbose:
    print = lambda **_: ()


print("Verbose on!")

FIN = args.fin.name if args.fin else DEFAULT_FIN
FOUT = args.fout.name if args.fout else DEFAULT_FOUT
COURSE = args.course or COURSE_PLACEHOLDER

DIR = os.path.dirname(os.path.realpath(__file__)) + "/"
DIN = DIR + FIN
DOUT = DIR + FOUT

# Rules
# todo make this pretty
BASE = [
    (r"$", r""),  # https://stackoverflow.com/a/10913081/7833617
    (r" ?[–-—]{1,2} ?", r" -- "),
    (r"([Ll]eft)", r"(L)"),
    (r"([Rr]ight)", r"(R)"),
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
    (r"^(.){1,3}$",
     r"<!--\1-->"),  # remove lines with three or less characters
    (r"^\s*\n(\t+. .)", r"\1"),  # gaps between bps
    (r" {1,3}\t", r"    "),  # hidden tab
    (r"\t", r"    "),  # tab to four spaces
]

if not args.header:
    BASE += [
        # ======= #
        # Headers #
        # ======= #
        (r"^[☛]", r"## "),  # H2 unique
        (r"(^[A-Z][^ .].{2,42}\n)", r"\n## \1\n"),  # Headers
        (r"#+\s*(.*\n+)#+\s*(.*\n+)#+\s*(.*\n+)", r"# \1## \2### \3"),  # H3s
        (r"#{1,2}\s*(.*\n+)#{2,3}\s*(.*\n+)", r"# \1## \2"),  # H2s
        (r"(#.*?)\n+\s*. ([A-Z0-9\"])",
         r"\1\n\n- \2"),  # spacing after headers
        (r"$\n+#", r"\n\n#"),  # spacing before headers
        (r"(#.*$\n*)\t+(.)", r"\1\2"),  # normalize below header
        # (r"(#.*$\n+[*-].*$)(?:\n\s(. .*))+", r"\1\n\t\2"),  # normalize two down
        (r"^([\s]*). (\d+\.)", r"\1\2"),  # point before numbers
        (r"^([A-Z].{20,})", r"- \1"),  # long lines
        (r'^(\s*. )(.{3,45}?)(: *[^"])', r"\1**\2**\3"),  # term/definition
        (r"[““””]", r'"'),
        (r"\n([,.])", r" \1")
    ]

STYLES = dict([(k, []) for k in COURSES])
STYLES["c100"] = [
    (r"\n[““””]", r' "'),
    (r'^\s*((?:.|\d+\.)? ?)(♫|(?:[“"].*[”"].*)$)', r"\t\1> \2"),  # quotes
    (r"^(\s)*.(> )", r"\1\2"),  # botch
    (r" v ", r"\n\t- "),
]
STYLES["16a"] = [(r"~([\\a-Z])", r"\vec \1")]
STYLES["e-29"] = [
    ("[\uE000-\uF8FF]", r"-"),
    (r"[•]", r"-"),
    (r"[▪]", r"\t-"),
]
STYLES["c61"] = [
    (r"^ ?Figure(?:\n*| )((\d+)\.(\d+)\..*?)$",
     r"\n{{< columns >}}<!-- mathjax fix -->\n" + r"\n" +
     r"<---><!-- mathjax fix -->\n" + f">![](/docs/mcb-c61/\\2\\3.png)\n" +
     r">Figure \1\n" + r"{{< /columns >}}\n"),
    (
        r"((?:[A-Z][a-z]{2,} ?){2}) (\([12]\d{3}-[12]\d{3}\))",
        r"[\1 \2](https://en.wikipedia.org/wiki/\1)",
    ),
    (r"^ ?([A-Z])", r"- \1"),
    (r'([a-zA-Z])[.?!]"? ', r"\1\n\t- "),
]


def decode(c):
    return hex(ord(c))


def main():
    if (not args.force and os.path.isfile(DOUT) and "Y" !=
        (input(f"> overwrite {FOUT}? [y/*]\n").upper() + "_")[0]):
        exit()

    rules = BASE if not args.base else []
    if COURSE and COURSE in STYLES.keys():
        rules += STYLES.get(COURSE)

    with open(DIN, "r") as fin:
        data = fin.read().strip()
        with open(DOUT, "w") as fout:
            for pat, repl in rules:
                data = re.sub(pat, repl, data, flags=re.M)
                print(f"{[pat]} => {[repl]}")

            fout.write(data)


if __name__ == "__main__":
    main()
