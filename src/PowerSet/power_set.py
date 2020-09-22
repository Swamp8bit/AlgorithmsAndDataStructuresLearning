
class PowerSet:

    def __init__(self, sz):
        # ваша реализация хранилищe
        self.count=0
        self.sz=sz
        self.elements = [None] * self.sz  # array initialization

    def hash_fun(self, value):
        # в качестве value поступают строки!
        sum=0
        for pos in range(len(value)):
            sym=value[pos]
            sum+=ord(sym)*pos
        # всегда возвращает корректный индекс слота
        return sum%self.sz

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
        slot=self.hash_fun(value)
        #print(f"The first slot is {slot}")
        for i in range(self.sz):
            #print(f"The slot in the loop is {slot} the iteration {iteration}")
            if self.elements[slot] is None:
                return slot
            else:
                slot=(slot+3)%self.sz
        #print(f"Cannot find slot in  {iteration} iterations for the size of array {self.size}")
        return None

    def get(self, value):

        slot=self.hash_fun(value)
        #print(f"The slot is {slot}")

        for i in range(self.sz):
            if self.elements[slot] == value:
                return True
            else:
                slot=(slot+3)%self.sz
        #print(f"Cannot find value {value} in  {iteration} iterations for the size of array {self.size}")
        return False

    def put(self, value):
        # записываем значение по хэш-функции

        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить
        if not self.get(value):
            slot=self.seek_slot(value)
            if slot is not None:
                self.elements[slot]=value
                self.count+=1
                return slot
            else:
                return None

    def size(self):
        return self.count
        # количество элементов в множестве

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        slot = self.hash_fun(value)
        for i in range(self.sz):
            if self.elements[slot] == value:
                self.elements[slot] = None
                self.count-=1
                return True
            else:
                slot = (slot + 3) % self.sz
        # print(f"Cannot find value {value} in  {iteration} iterations for the size of array {self.size}")
        return False

    def only_values(self):
        return [x for x in self.elements if x is not None]

    def intersection(self, set2):
        # пересечение текущего множества и set2
        if self.sz < set2.sz:
            new_sz=self.sz
        else:
            new_sz=set2.sz
        result=PowerSet(new_sz)
        if self.size() < set2.size():
            only_values=self.only_values()
        else:
            only_values = set2.only_values()
        for value in only_values:
            if self.get(value) and set2.get(value):
                result.put(value)
        return result

    def union(self, set2):
        # объединенbе текущего множества и set2
        new_sz=set2.sz+self.sz
        set1_only_values = self.only_values()
        set2_only_values=set2.only_values()
        result=PowerSet(new_sz)
        for value in set1_only_values:
            result.put(value)
        for value in set2_only_values:
            result.put(value)
        return result

    def difference(self, set2):
        # разница текущего множества и set2
        result=PowerSet(self.sz)
        set1_only_values = self.only_values()
        for value in set1_only_values:
            if set2.get(value):
                continue
            else:
                result.put(value)
        return result

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        set2_only_values = set2.only_values()
        for value in set2_only_values:
            if not self.get(value):
                return False
        return True

# from time import perf_counter
#
#
# if __name__ == '__main__':
#     S1=PowerSet(23)
#     assert S1.size() == 0
#     S1.put('AhalayMahalay')
#     assert S1.get('AhalayMahalay') == True
#     S1.put('AhalayMahalay')
#     assert S1.size() == 1
#     assert S1.size() == 1
#     S1.put('SimSalavim')
#     assert S1.get('SimSalavim') == True
#     assert S1.size() == 2
#     assert S1.remove('SimSalavim') == True
#     assert S1.size() == 1
#     print(S1.elements)
#     print([x for x in S1.elements if x is not None])
#
#     string1='ABCDEF'
#     string2='YQWRTUEF'
#     S2 = PowerSet(23)
#     S3 = PowerSet(23)
#     for s in string1:
#         S2.put(s)
#     for s in string2:
#         S3.put(s)
#     # start = perf_counter()
#     # S4=S2.intersection(S3)
#     # print(S4.only_values())
#     # end = perf_counter()
#     # print(end-start)
#
#     # start = perf_counter()
#     # S4 = S2.union(S3)
#     # print(S3.only_values())
#     # print(S2.only_values())
#     # print(S4.only_values())
#     # end = perf_counter()
#     # print(end - start)
#
#     start = perf_counter()
#     S4 = S2.difference(S3)
#     print(S3.only_values())
#     print(S2.only_values())
#     print(S4.only_values())
#     end = perf_counter()
#     print(end - start)
