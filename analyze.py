#!/usr/bin/env python3
from collections import Counter
from time import gmtime
import os
import numpy as np
import collections

ZSH_HISTORY = "~/.zsh_history"


def concatx(*args):
    return "\n".join(
        map(lambda t: "".join(t), zip(*map(lambda s: s.split("\n"), args)))
    )


def termhist(a, title, xsize=10, ysize=10, xleg=None):
    values, _ = np.histogram(a, bins=xsize)
    normv = 1 / np.max(values) * ysize
    mat = np.zeros((xsize, ysize))
    for i_v, v in enumerate(values):
        for k in range(int((v * normv))):
            mat[i_v][k] = v
    d = 6
    hist = "-" * d + "+" + "-" * xsize + "+" + "\n"
    hist += " " * d + "|" + title.center(xsize) + "|\n"
    hist += "-" * d + "+" + "-" * xsize + "+" + "\n"
    for y in range(ysize):
        hist += f"{int(((ysize-y-1)/normv)):>5} |"
        for x in range(xsize):
            hist += "\u2588" if mat[x][ysize - y - 1] else " "
        hist += "|\n"
    hist += "-" * d + "+" + "-" * xsize + "+" + "\n"
    if not xleg is None:
        assert len(xleg) == xsize
        hist += " " * d + "|" + xleg.center(xsize) + "|\n"
        hist += "-" * d + "+" + "-" * xsize + "+" + "\n"

    return hist


def termhistcol(ysize=10):
    return "+\n|\n+\n" + "|\n" * ysize + "+\n|\n+\n"


def analyse_zshrc():
    zsh_history_real_path = os.path.expanduser(ZSH_HISTORY)
    print(f"Analyse {zsh_history_real_path}")
    ts = []
    commands = []
    with open(zsh_history_real_path, "rb") as f:
        for line in f:
            try:  # Skip wrong lines
                raw = line.decode().rstrip("\n\r")
                tup = raw.split(";", 1)
                timestamp = gmtime(int(tup[0][2:-2]))
                command = tup[1]
                # Ensure all values are already computed
                ts.append(timestamp)
                commands.append(command)
            except:
                pass
    return ts, commands


def grouper(iterable, n):
    iterable = iter(iterable)
    while True:
        yield itertools.chain((next(iterable),), itertools.islice(iterable, n - 1))


if __name__ == "__main__":

    ts, cmds = analyse_zshrc()

    print("Frequencies:")
    hnames = "012345678901012345678901"
    dnames = "MTWTFSS"
    mnames = "JFMAMJJASOND"
    hists = concatx(
        termhistcol(),
        termhist([t.tm_hour for t in ts], "hour", xsize=24, xleg=hnames),
        termhist([t.tm_mday for t in ts], "day", xsize=7, xleg=dnames),
        termhist([t.tm_mon for t in ts], "month", xsize=12, xleg=mnames),
    )
    print(hists)

    # Top commands
    D = 10
    N = 3
    print("Top commands:")
    stats = Counter(map(lambda x: x.split(" ", 1)[0], cmds)).most_common(N * D)
    format_stats = lambda stats: "\n".join(
        (f"{n[:8]:>8} {c:5} ({(100*c/len(cmds)):4.1f}%) |" for n, c in stats)
    )
    res = concatx(*(format_stats(stats[s * D : s * D + D]) for s in range(N)))
    print(res)
