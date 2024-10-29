#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, item, counter=0):
        self.item = iter(item)
        self.counter = counter

    def get_count(self):
        return self.counter

    def __next__(self):
        self.counter += 1
        return next(self.item)
