class BITree:
    def __init__(self, max_bound = 1000000, init_list = []):
        self._ds = {}
        self._max_bound = max_bound
        self._counter = {}
        for element in init_list:
            self.add(element)

    def _upTree(self, num, value):
        if (num > self._max_bound):
            return;
        if (num not in self._ds):
            self._ds[num] = value
        else:
            self._ds[num] += value
        self._upTree(num + (num & - num), value)

    def _downTree(self, num):
        if (num in self._ds):
            tmp = self._ds[num]
        else:
            tmp = 0
        if (num <= 0):
            return tmp
        else:
            return tmp + self._downTree(num - (num & - num))

    def count(self, x_range, y_range):
        lower_range = min([x_range, y_range])
        upper_range = max([x_range, y_range])
        lowsum = self._downTree(lower_range-1)
        upsum = self._downTree(upper_range)
        return upsum - lowsum

    def add(self, num, value = 1):
        # O(log(max_bound))
        if (num not in self._counter):
            self._counter[num] = value
        else:
            self._counter[num] += value
        self._upTree(num, value)

    def delete(self, num, value = 1):
        # O(log(max_bound))
        if (num not in self._counter) or (self._counter[num] < value):
            print ("Error: Not enough elements to delete.")
        self._counter[num] -= value
        self._upTree(num, value * -1)

    def clear(self):
        self._ds.clear()
