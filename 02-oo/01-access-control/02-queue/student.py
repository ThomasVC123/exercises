class queue:
    def __init__(self):
        self.__items = []
        
    def add(self, item):
        self.__items.append[item]

    def next(self):
        item = self.__items[0]
        del self.__items[0]
        return item
    
    def is_empty(self):
        return len(self.__items) == 0
