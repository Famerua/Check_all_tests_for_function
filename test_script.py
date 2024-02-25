class Xrange:
    def __init__(self, start, end, step=1):
        self.start = float(start) if isinstance(step, float) else start
        self.end = float(end) if isinstance(step, float) else end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start >= self.end:
                raise StopIteration
        else: 
            if self.start <= self.end:
                raise StopIteration
        val = self.start
        self.start += self.step
        return val
xrange = Xrange(5, 1, -1)

next(xrange)
next(xrange)
next(xrange)
next(xrange)

try:
    next(xrange)
except StopIteration:
    print('Error')