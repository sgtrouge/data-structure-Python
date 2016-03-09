class BITree:
    def __init__(self, maxbound = 1000000):
        self._ds = {}
        self._maxbound = maxbound

    def upTree(self, num, value):
        if (int(num) > self._maxbound):
            return;
        if (num not in self._ds):
            self._ds[num] = 1
        else:
            self._ds[num] += value
        num = int(num)
        self.upTree(str(num + (num & - num)), value)

    def downTree(self, num):
        if (num in self._ds):
            tmp = self._ds[num]
        else:
            tmp = 0
        num = int(num)
        if (num <= 0):
            return tmp
        else:
            return tmp + self.downTree(str(num - (num & - num)))

    def count(self, x_range, y_range):
        lower_range = min([x_range, y_range])
        upper_range = max([x_range, y_range])
        lowsum = self.downTree(str(lower_range-1))
        upsum = self.downTree(str(upper_range))
        return upsum - lowsum

    def add(self, num, value = 1):
        self.upTree(str(num), value)

    def delete(self, num, value = 1):
        self.upTree(str(num), value * -1)

    def clear(self):
        self._ds.clear()
