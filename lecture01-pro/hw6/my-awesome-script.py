from cowpy import cow
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer
from datetime import datetime
import argparse
import pytz


def highligh(code):
    return highlight(code, PythonLexer(), TerminalFormatter())


def cowsay(text):
    buble = cow.Beavis()
    return buble.milk(text)


def time(zone):
    tz = pytz.timezone(zone)
    result = datetime.now(tz)
    fmt = '%Y-%m-%d %H:%M:%S'
    return result.strftime(fmt)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("arguments", nargs='+', type=str)
    args = parser.parse_args()
    if args.arguments[0] == "highligh":
        print(highligh(args.arguments[1]))
    elif args.arguments[0] == "time":
        print(time(args.arguments[1]))
    elif args.arguments[0] == "cowsay":
        print(cowsay(args.arguments[1]))
