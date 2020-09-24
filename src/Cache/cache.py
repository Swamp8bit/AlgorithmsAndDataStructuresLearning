class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота
        def hashing(value):
            result = 0
            for pos in range(len(value)):
                sym = value[pos]
                result += ord(sym) * pos
            return result % self.size

        slot = hashing(key)

        iteration = 0
        step = 3
        while iteration < self.size:
            iteration += 1
            if self.slots[slot] is None:
                return slot
            else:
                slot = (slot + step) % self.size
        return None

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        if key in self.slots:
            return True
        else:
            return False

    def put(self, key, value):
        if self.is_key(key):
            slot=self.slots.index(key)
            self.values[slot] = value
        else:
            slot = self.hash_fun(key)
            if slot is not None:
                self.slots[slot] = key
                self.values[slot] = value
            else:
                return None
        # гарантированно записываем
        # значение value по ключу key

    def get(self, key):

        def find_key(value, size, step):
            slot = self.hash_fun(value)
            iteration = 0
            while iteration < size:
                iteration += 1
                if self.slots[slot] == value:
                    return slot
                else:
                    slot = (slot + step) % size
            return None

        if self.is_key(key):
            slot = find_key(key, self.size, 3)
            return self.values[slot]
        else:
            # возвращает value для key,
            # или None если ключ не найден
            return None


class NativeCache(NativeDictionary):
    def __init__(self, sz):
        super().__init__(sz)

        self.hits = [0] * self.size

    def get(self, key):

        def find_key(value, size, step):
            slot = self.hash_fun(value)
            iteration = 0
            while iteration < size:
                iteration += 1
                if self.slots[slot] == value:
                    self.hits[slot]+=1
                    return slot
                else:
                    slot = (slot + step) % size
            return None

        if self.is_key(key):
            slot = find_key(key, self.size, 3)
            return self.values[slot]
        else:
            # возвращает value для key,
            # или None если ключ не найден
            return None

    def hash_fun(self, key):
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота
        def hashing(value):
            result = 0
            for pos in range(len(value)):
                sym = value[pos]
                result += ord(sym) * pos
            return result % self.size

        slot = hashing(key)

        iteration = 0
        step = 3
        while iteration < self.size:
            iteration += 1
            if self.slots[slot] is None:
                return slot
            else:
                slot = (slot + step) % self.size
        return None

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        if key in self.slots:
            return True
        else:
            return False

    def put(self, key, value):
        if self.is_key(key):
            slot = self.slots.index(key)
            self.values[slot] = value
        else:
            slot = self.hash_fun(key)
            if slot is not None:
                self.slots[slot] = key
                self.values[slot] = value
            else:
                slot_to_clean = self.hits.index(min(self.hits))
                self.slots[slot_to_clean] = key
                self.values[slot_to_clean] = value
        # гарантированно записываем
        # значение value по ключу key

    def illustration(self):
        for s, v, h in zip(self.slots, self.values, self.hits):
            print(f"Key {s} value {v} hit {h}")

from random import choice
import requests
import os
if __name__ == '__main__':
    if not os.path.exists('words.txt') and not os.path.getsize('words.txt') > 0:
        http = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
        with open('words.txt', 'w+') as file:
            file.write(http.text)
    words=[]
    with open('words.txt', 'r') as f:
        for i in range(1000):
            line = f.readline()
            words.append(line.rstrip())

    print(words)
    cache=NativeCache(23)

    for i in range(23):
        cache.put(choice(words), choice(words))

    for i in range(100):
        cache.get(choice(words))
    #     r = http.request('GET', 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
    #     list_of_words=r.data.decode('utf-8').split('\n')

    cache.illustration()