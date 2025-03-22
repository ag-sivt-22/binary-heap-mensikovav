from dataclasses import dataclass
from typing import Any

@dataclass
class Element:
    value: Any
    priority: int
 

class BinaryHeap:

    def __init__(self):
        self.heap = []
    
    def push(self, element):
        # naivni implementace binarni haldy
        self.heap.append(element)
        pozice = len(self.heap)-1
        self.bublani_nahoru(pozice)

    def bublani_nahoru(self,pozice):
        rodic = (pozice-1)//2
        if pozice >0 and self.heap[pozice].priority < self.heap[rodic].priority:
            self.heap[pozice], self.heap[rodic] =  self.heap[rodic], self.heap[pozice]
            self.bublani_nahoru(rodic)

    def pop(self):
        # naivni implementace binarni haldy
        # najdi nejmensi prvek a vrat ho
        if not self.heap:
            raise Exception("Heap is empty")
        min = self.heap[0]
        novy = self.heap[len(self.heap)-1]
        self.heap[0]= novy
        self.heap.pop()
        pozice = 0
        self.bublani_dolu(pozice)
        return min

    def bublani_dolu(self, pozice):
        syn1 = 2*pozice + 1
        syn2= 2*pozice + 2
        nejmensi = pozice
        if syn1 < len(self.heap) and self.heap[syn1].priority < self.heap[nejmensi].priority:
            nejmensi = syn1
        if syn2 < len(self.heap) and self.heap[syn2].priority < self.heap[nejmensi].priority:
            nejmensi = syn2
        if nejmensi != pozice:
            self.heap[pozice], self.heap[nejmensi] = self.heap[nejmensi], self.heap[pozice]
            self.bublani_dolu(nejmensi)


    def head(self):
        if not self.heap:
            raise Exception("Heap is empty")
        # vrati nejmensi element ve fronte (element na cele fronty)
        # protoze mame naivni implementaci, musime projit cely seznam
        return self.heap[0]
