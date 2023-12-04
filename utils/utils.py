import sys

def input_as_list(separator=None):
    if not separator:
        return [l.strip() for l in sys.stdin if l.strip()]
    data = sys.stdin.read()
    return [l for l in data.split(separator) if l.strip()]


def input_as_list_ints(separator=None):
    if not separator:
        return [int(l.strip()) for l in sys.stdin if l.strip()]
    data = sys.stdin.read()
    return [int(l.strip()) for l in data.split() if l.strip()]

def example_as_list(example, separator=None):
    if not separator:
        return [l.strip() for l in example if l.strip()]
    data = sys.stdin.read()
    return [l for l in data.split(separator) if l.strip()]

