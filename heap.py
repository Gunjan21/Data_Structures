class minHeap:

    def __init__(self):
        self.list = [0]
        self.size = 0

    def insert(self,data):

        self.list.append(data)
        self.size += 1

        self.perc_up(self.size)

    def perc_up(self,i):
        parent = i//2
        while parent > 0:
            if self.list[i]<self.list[parent]:
                print("perc up: swapping: ", self.list[i],"and",
                      self.list[parent])
                temp = self.list[i]
                self.list[i] = self.list[parent]
                self.list[parent]=temp
            else:
                break

            i = parent
            parent = i//2

    def perc_down(self,i):
        done = 0
        while not done:
            if 2*i > self.size: #this means only 1 node in the heap. no child
                break
            #we come here, only if a child exists.
            minChildindex = i*2

            if 2*i+1>self.size:
                break

            if 2*i+1 < self.size:
                if self.list[2*i+1]<self.list[minChildindex]:
                    minChildindex = 2*i + 1
                    
            if self.list[minChildindex] < self.list[i]:
                print("perc down: swapping",self.list[i],"and",
                      self.list[minChildindex])
                temp = self.list[i]
                self.list[i]=self.list[minChildindex]
                self.list[minChildindex] = temp
            else:
                break

            i = minChildindex

        print("perc_down done")

    def remove(self):
        if self.size == 0:
            raise RuntimeError("Removing from empty heap")

        result = self.list[1]
        self.list[1] = self.list[self.size]
        self.size = self.size - 1
        self.list.pop()
        self.perc_down(1)

        return result

    def buildHeap(self,alist):
        i = len(alist)//2
        self.size = len(alist)
        self.list = [0] + alist[:]

        while(i>0):
            self.perc_down(i)
            i = i-1

    def search_second_elem(self):
        pass

class maxHeap:

    def __init__(self):
        self.size = 0
        self.list = []

    def insert(self,data):

        self.list.append(data)
        self.size += 1

        self.perc_up(self.size)

    def perc_up(self,i):

        parent = i//2
        while parent > 0:
            if self.list[parent]>self.list[i]:
                break
            else:
                print("perc up: swapping," , self.list[parent],"and",
                      self.list[i])
                temp = self.list[i]
                self.list[i]=self.list[parent]
                self.list[parent] = temp

            i = parent
            parent = i//2

    def remove(self):

        result = self.list[1]

        self.list[1] = self.list[self.size]
        self.size -= 1
        self.list.pop()
        self.perc_down(1)

        return result

    def perc_down(self,i):
        done = 0
        self.size = len(self.list)
        while not done:
            if i*2 > self.size:
                break

            maxChild = i*2
            
            if 2*i+1 <= self.size:
                if self.list[maxChild]<self.list[i*2+1]:
                    maxChild = i*2 + 1

            if self.list[i]<self.list[maxChild]:

                print("prec down: swapping", self.list[i], "and",
                      self.list[maxChild])
                temp = self.list[i]
                self.list[i] = self.list[maxChild]
                self.list[maxChild] = temp
            else:
                break

            i = maxChild

        print("perc down : done")
        print(self.list)

    def buildHeap(self,alist):
        i = len(alist)//2
        self.size = len(alist)
        self.list = [0] + alist[:]
        while (i>0):
            self.perc_down(i)
            i = i-1
        
    def heapSort(self,alist):
        
        a = []
        self.buildHeap(alist)
        end = len(self.list)
        print(end)
        print(self.list[1])
        print(self.list[end-1])
        while end > 1:
            a.append(self.list[1])
            print('swapping',self.list[end-1],'and',self.list[1])
            temp = self.list[end-1]
            self.list[end-1]=self.list[1]
            self.list[1]=temp
            self.perc_down(1)
            end -= 1
            
        print(a)
