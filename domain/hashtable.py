from collections import deque


class HashTable:

    # constructor, takes size as parameter
    def __init__(self, size):
        self.__items = [deque() for _ in range(size)]
        self.__size = size

    # hashing function
    def hash(self, key):
        sum = 0
        for chr in key:
            sum += ord(chr) - ord('0')
        return sum % self.__size

    # adds an element to the hashtable
    def add(self, key):
        if self.contains(key):
            return self.getPosition(key)
        self.__items[self.hash(key)].append(key)
        return self.getPosition(key)

    # checks if the table contains an element
    def contains(self, key):
        return key in self.__items[self.hash(key)]

    # removes an element from the table
    def remove(self, key):
        self.__items[self.hash(key)].remove(key)

    # returns the table as a string
    def __str__(self) -> str:
        result = "Symbol Table\n"
        for i in range(self.__size):
            result = result + str(i) + " === " + str(self.__items[i]) + "\n"
        return result

    # returns the position of an element in the table
    def getPosition(self, key):
        listPosition = self.hash(key)
        listIndex = 0
        for item in self.__items[listPosition]:
            if item != key:
                listIndex += 1
            else:
                break
        return (listPosition, listIndex)