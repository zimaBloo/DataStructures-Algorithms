class HashLinear:
    def __init__(self, M):
        self.M = M
        self.hashTable = M * [None]
        self.tombstone = "RIP"

    def hashValue(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        returnal = sum % self.M
        return returnal
    
    def insert(self, data):
        slot = self.hashValue(data)

        if self.hashTable[slot] == data:
            return
        
        if self.hashTable[slot] is None or self.hashTable[slot] == self.tombstone:
            self.hashTable[slot] = data
            return

        startingSlot = slot
        while True:
            slot += 1

            if slot == self.M:
                slot = 0

            if self.hashTable[slot] == data:
                return
        
            if slot == startingSlot:
                return
            
            if self.hashTable[slot] is None or self.hashTable[slot] == self.tombstone:
                self.hashTable[slot] = data
                return

    def delete(self, data):
        slot = self.hashValue(data)
        slotNumber = 0

        while self.hashTable[slot] != data:
            if slotNumber >= self.M:
                return
            if slot == self.M - 1:
                slot = 0
            else:
                slot += 1
            slotNumber += 1
        self.hashTable[slot] = self.tombstone
        return

    def print(self):
        string = ""
        for i in self.hashTable:
            if i is not None and i != self.tombstone:
                if len(string) == 0:
                    string = string + (str(i))
                else:
                    string = string + " " + str(i)
        print(string)


if __name__ == "__main__":
    table = HashLinear(8)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # 10aaaa1 BM40A1500 fOo 123 Bar1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # 10aaaa1 BM40A1500 Bar1