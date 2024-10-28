#!/usr/bin/env python3
from abc import ABC, abstractmethod

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        length = len(item)
        print("Extended the list with [{}] items.".format(length))

    def remove(self, item):
        if item not in self:
            print("item not in list")
        else:
            print("Removed [{}] from the list.".format(item))
            super().remove(item)

    def pop(self, position=-1):
        print("Popped [{}] from the list.".format(self[position]))
        super().pop(position)
