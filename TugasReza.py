class Node:
    def __init__(self,data,priority) -> None:
        self._data = data
        self._priority = priority
        self._next = None
        self._prev = None
class PQSTugas:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0
    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False
    def printAll(self):
        if self.isEmpty() == True:
            print("Sorted Queue kosong")
        else:
            a = self._head
            while a != None:
                print('(', a._data, ',', a._priority, ')', end=' ')
                a = a._next
        print()
    def _addHead(self, newNode) -> None:
        newNode._next = self._head
        self._head._prev = newNode
        self._head = newNode
    def _addTail(self, newNode) -> None:
        self._head._next = newNode
        newNode._prev = self._head
        self._tail = newNode
    def _addMiddle(self, newNode) -> None:
        newNode = newNode._next
    def add(self, data, priority) -> None:
         #isi kode anda
        b = Node(data,priority)
        if self.isEmpty():
            self._head = b
            self._tail = b
        elif self._size == 1:
            if self._head._priority > priority:
                b._next = self._head
                self._head._prev = b
                self._head = b
            else:
                self._head._next = b
                b._prev = self._head
                self._tail = b
        else:
            if self._head._priority > priority:
                b._next = self._head
                self._head._prev = b
                self._head = b
            elif self._head._priority <= priority:
                self._head._next = b
                b._prev = self._head
                self._tail = b
                self._tail._next = None
            else:
                a = self._head
                while a._priority < priority:
                    a = a._next
                c = a._prev
                b._next = a
                a._prev = b
                c._next = b
                b._prev = c
        self._size = self._size + 1
    def remove(self) -> None:
        if self.isEmpty() == False:
            d = self._head
            if self._size == 1:
                self._head = None
            else:
                self._head = self._head._next
                self._head._prev = None
            del d
            self._size = self._size - 1
    def removePriority(self, priority) -> None:
        #isi kode anda
        pass
if __name__ == "__main__":
    tugasKu = PQSTugas()
    tugasKu.add("StrukDat",1)
    tugasKu.add("Menyapu", 5)
    tugasKu.add("Cuci Baju", 4)
    tugasKu.add("Beli Alat Tulis", 3)
    tugasKu.add("Cuci Sepatu", 4)
    tugasKu.printAll()
    # tugasKu.remove()
    # tugasKu.printAll()
    # tugasKu.removePriority(2)
    # tugasKu.removePriority(4)
    # tugasKu.printtAll()