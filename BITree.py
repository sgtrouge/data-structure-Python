class BITree:
    def __init__(self, max_bound = 1000000, init_list = []):
        self._count = {}
        self._max_bound = max_bound
        self._counter = {}
        self._sum = {}
        for element in init_list:
            self.add(element)

    def clear(self):
        self._count.clear()
        self._sum.clear()


#--------------------------FENWICK-OPERATION------------------------------#
    def _upTree(self, num, value, ori_num):
        if (num > self._max_bound):
            return;
        if (num not in self._count):
            self._count[num] = value
            self._sum[num] = ori_num
        else:
            self._count[num] += value
            self._sum[num] += ori_num
        self._upTree(num + (num & - num), value, ori_num)

    def _downTree(self, num, command_type):
        if (command_type == 'sum'):
            tmp_ds = self._sum
        else:
            tmp_ds = self._count

        if (num in tmp_ds):
            tmp = tmp_ds[num]
        else:
            tmp = 0

        if (num <= 0):
            return tmp
        else:
            return tmp + self._downTree(num - (num & - num), command_type)

#--------------------------BASIC-OPERATION---------------------------------#

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

#--------------------------AGGREGATION------------------------------------#
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

#--------------------------ORDER-STATISTIC---------------------------------#
    def meanRange(self, x_range, y_range):
        tmp_sum = self.sumRange(x_range, y_range);
        tmp_count = self.countRange(x_range, y_range);
        if (tmp_count == 0):
            print ("Error: No elements in this range to compute mean")
        else:
            return tmp_sum*1.0/tmp_count

    def maxRange(self, x_range, y_range):
        tmp_count = self.countRange(x_range, y_range);
        return self.orderStat(x_range, y_range, tmp_count)

    def minRange(self, x_range, y_range):
        return self.orderStat(x_range, y_range, 1)

    def medianRange(self, x_range, y_range):
        tmp_count = (self.countRange(x_range, y_range) + 1)/2
        return self.orderStat(x_range, y_range, tmp_count)

    def orderStat(self, x_range, y_range, order):
        lower_range = min([x_range, y_range])
        upper_range = max([x_range, y_range])
        base_range = lower_range
        if (self.countRange(lower_range, upper_range) < order):
            print ("Error: Not enough elements in this range to find order")
            return
        res = 0
        while (lower_range <= upper_range):
            mid = (lower_range + upper_range)/2
            if (self.countRange(base_range, mid) >= order):
                res = mid
                upper_range = mid-1
            else:
                lower_range = mid+1
        return res
