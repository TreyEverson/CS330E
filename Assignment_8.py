# --------------------
# Assignment 8
# Robert Everson (rhe323)
# CS 330E
# --------------------

class my_islice_iterator ():
    def __init__ (self, letters, start = 0, stop = 0):
        self.letters = letters
        self.start = start
        self.stop = stop

    def __iter__ (self):
        return self

    def __next__ (self):
        l = list(self.letters)
        if len(l) == 0:
            raise StopIteration

        if self.start < self.stop:
            n = self.start
            self.start += 1
            return l[n]
        else:
            raise StopIteration
