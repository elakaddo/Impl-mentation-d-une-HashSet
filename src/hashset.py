class HashSet : 
    def __init__(self) -> None:
        self.elements = [None for i in range(0, 26)]
        self.count = 27

    def hashCode(self, value):
        if value != "" :
            hash = 0
            for char in value :
                hash += ord(char)
            hashCode = hash % self.count
            return hashCode
        else : return False
    
    def add(self, value):
        if value != "":
            i = self.hashCode(value)
            if self.elements[i] == None :
                self.elements[i] = value
                return i
            else : return False
        else : return False
    
    def get(self, i) : 
        if type(i) == int and i < 26 and i > 0:
            return self.elements[i]
        else : return False
