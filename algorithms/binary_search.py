import math
import itertools


class BinarySearch:

    def __init__(self):
        self._steps = 0

    @property
    def steps(self):
        return self._steps

    def binary_search(self, list_, item):
        """
        二分查找，找到元素返回下标，没找到返回None
        时间复杂度：O(logn)
        :param list_:
        :param item:
        :return:
        """
        low = 0
        high = len(list_) - 1
        while low <= high:
            self._steps += 1
            mid = (low + high) // 2
            if item == list_[mid]:
                return mid
            elif item < list_[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return None


if __name__ == '__main__':
    print(int(math.log(4000000000, 2)))
    l = [20, 25, 60, 202, 305, 908]
    bs = BinarySearch()
    print(bs.binary_search(l, 10))
    print('steps:%s' % bs.steps)
    # print(len(list(itertools.permutations('ABCDE'))))

