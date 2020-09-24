"""
排序算法
"""


class SortAlgorithms:

    @staticmethod
    def find_smallest(list_):
        smallest_index, smallest = 0, list_[0]
        for i in range(1, len(list_)):
            if list_[i] < smallest:
                smallest_index, smallest = i, list_[i]
        return smallest_index

    @staticmethod
    def selection_sort(list_):
        """
        选择排序:每次找最小的
        时间复杂度：O(n*n)
        :param list_:
        :return:
        """
        new_arr = []
        for _ in range(0, len(list_)):
            smallest = SortAlgorithms.find_smallest(list_)
            new_arr.append(list_.pop(smallest))
        return new_arr

    @staticmethod
    def quik_sort(arr):
        """
        快速排序:分而治之
        时间复杂度：平均情况下，O(nlogn)。最遭情况为O(n*n)
        :param arr:
        :return:
        """
        if len(arr) < 2:
            return arr
        t = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] <= t:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return SortAlgorithms.quik_sort(left[:]) + [t] + SortAlgorithms.quik_sort(right[:])


def dv(w, h):
    """递归：将一块地均匀地分成方块，且方块要尽可能大"""
    x, y = (w, h) if w > h else (h, w)
    z = x % y
    if z == 0:
        return y
    x, y = y, z
    return dv(x, y)


if __name__ == '__main__':
    a = [43, 2, 87, 1, 82, 34, 98, 23]
    # sorted_a = SortAlgorithms.selection_sort(a)
    # print(sorted_a)

    print(SortAlgorithms.quik_sort(a))

    # print(dv(1680, 640))
