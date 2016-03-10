class BITree:
    def __init__(self, max_bound = 1000000, init_list = []):
        self._ds = {}
        self._max_bound = max_bound
        self._counter = {}
        self._sum = {}
        for element in init_list:
            self.add(element)

    def _upTree(self, num, value, ori_num):
        if (num > self._max_bound):
            return;
        if (num not in self._ds):
            self._ds[num] = value
            self._sum[num] = ori_num
        else:
            self._ds[num] += value
            self._sum[num] += ori_num
        self._upTree(num + (num & - num), value, ori_num)

    def _downTree(self, num, command_type):
        if (command_type == 'sum'):
            tmp_ds = self._sum
        else:
            tmp_ds = self._ds

        if (num in tmp_ds):
            tmp = tmp_ds[num]
        else:
            tmp = 0

        if (num <= 0):
            return tmp
        else:
            return tmp + self._downTree(num - (num & - num), command_type)

    def add(self, num, value = 1):
        # O(log(max_bound))
        if (num not in self._counter):
            self._counter[num] = value
        else:
            self._counter[num] += value
        self._upTree(num, value, num)

    def delete(self, num, value = 1):
        # O(log(max_bound))
        if (num not in self._counter) or (self._counter[num] < value):
            print ("Error: Not enough elements to delete.")
        self._counter[num] -= value
        self._upTree(num, -value, -num)

    def countRange(self, x_range, y_range):
        lower_range = min([x_range, y_range])
        upper_range = max([x_range, y_range])
        lowsum = self._downTree(lower_range-1, 'count')
        upsum = self._downTree(upper_range, 'count')
        return upsum - lowsum

    def sumRange(self, x_range, y_range):
        lower_range = min([x_range, y_range])
        upper_range = max([x_range, y_range])
        lowsum = self._downTree(lower_range-1, 'sum')
        upsum = self._downTree(upper_range, 'sum')
        return upsum - lowsum

    def meanRange(self, x_range, y_range):
        tmp_sum = self.sumRange(x_range, y_range);
        tmp_count = self.countRange(x_range, y_range);
        if (tmp_count == 0):
            print ("Error: No elements in this range to compute mean")
        else:
            return tmp_sum*1.0/tmp_count

    def maxRange(self, x_range, y_range):
        return

    def clear(self):
        self._ds.clear()
