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
        slot = self.hash_fun(key)
        if slot is not None:
            if self.is_key(key):

                self.values[slot] = value
            else:
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


if __name__ == "__main__":
    map1 = NativeDictionary(17)

    TEST_STRINGS_keys = ["Open", "afile", "on23thedisk", "please", "change1"]
    TEST_STRINGS_values = ["Irina", "Zheka", "Kate", "Gorgoza", "Baragoz"]
    for pos in range(len(TEST_STRINGS_keys)):
        print(f"hash_fun of {TEST_STRINGS_keys[pos]} is {map1.hash_fun(TEST_STRINGS_keys[pos])}")
        print(f"{pos} string of keys {TEST_STRINGS_keys[pos]} and values {TEST_STRINGS_values[pos]}")
        print(map1.put(TEST_STRINGS_keys[pos], TEST_STRINGS_values[pos]))
    print("#######")
    for pos in range(len(TEST_STRINGS_keys)):
        pass

