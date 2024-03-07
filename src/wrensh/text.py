import math
import re

def _is_neg_zero(x):
    return x == 0 and math.copysign(1, x) < 0

def cat(*files):
    return TextWrensh().cat(*files)

def echo(lines):
    out = TextWrensh()
    out.pipe += lines
    return out

class TextWrensh(object):

    def __init__(self, input=None):
        if input is None:
            self.pipe = list()
        else:
            self.pipe = input

    # Sinks

    def __str__(self):
        return "\n".join(self.pipe)

    def redirect(self, file):
        with open(file, "w") as f:
            f.write(str(self) + "\n")

    def append(self, file):
        with open(file, "a") as f:
            f.write(str(self) + "\n")

    # Higher-order functions

    def map(self, f):
        out = TextWrensh()
        for x in self.pipe:
            y = f(x)
            if isinstance(y, list):
                out.pipe += y
            elif isinstance(y, str):
                out.pipe.append(y)
        return out

    # POSIX commands

    def cat(self, *files):
        out = TextWrensh()
        for file in files:
            with open(file) as f:
                out.pipe += f.read().splitlines()
        return out

    def grep(self, pattern):
        out = TextWrensh()
        regex = re.compile(".*" + pattern + ".*")
        for line in self.pipe:
            if regex.match(line) is not None:
                out.pipe.append(line)
        return out

    def head(self, n=10):
        out = TextWrensh()
        if n > len(self.pipe) or _is_neg_zero(n):
            out.pipe = self.pipe
        else:
            out.pipe = self.pipe[:n]
        return out

    def sort(self):
        out = TextWrensh()
        self.pipe.sort()
        out.pipe = self.pipe
        return out

    def tail(self, n=10):
        out = TextWrensh()
        if n > len(self.pipe):
            out.pipe = self.pipe
        else:
            if n == 0:
                return out
            if n < 0:
                n += 1
            out.pipe = self.pipe[-n:]
        return out

    def uniq(self):
        out = TextWrensh()
        last = None
        for line in self.pipe:
            if line == last:
                continue
            last = line
            out.pipe.append(last)
        return out
