#hashtables
#linked list approach - each item in array is a head of linked list


import LinkedList
from LinkedList import *

def hash_func(value, size):
    return value % size

class HashTable:
    def __init__(self,func,size=7):
        self.size=size
        self.func = func
        self.hash_tbl=[ ]

        for i in range(self.size):
            self.hash_tbl.append(LinkedList())

    def add_data(self,data):
        index = self.func(data,self.size)
        print("adding at index ", index)
        l = self.hash_tbl[index]
        l.add_at_begin(data)

    def search_data(self,data):
        index = self.func(data, self.size)
        print("searching at index",index)
        l = self.hash_tbl[index]
        result = l.search(data)
        return result

    def print(self):
        for i in range(self.size):
            l = self.hash_tbl[i]
            print("index",i,":",end="")
            l.print()
