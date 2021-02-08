class Solution(object):
    def selectSort(self, a):
        """
        选择排序：
        输入一个无序数组，输出一个升序数组。
        第一次找数组中最小的值，放在第一位（即和第一位上的数交换）；
        第二次找剩余数组中最小的值（第2小的值），放在第二位（即和第二位上的数交换）；
        。。。
        第n-1次找剩余数组中最小的值(第n-1小的值)，放在第n-1位。
        :param a:
        :return:
        """
        n = len(a)

        for i in range(n - 2):
            cur_min = a[i]
            cur_min_index = i
            for j in range(i + 1, n):
                if a[j] < cur_min:
                    cur_min = a[j]
                    cur_min_index = j
            a[i], a[cur_min_index] = a[cur_min_index], a[i]
        return a


if __name__ == '__main__':
    print(Solution().selectSort([3, 1, 0, -2, 9, 5, 2, 0, 4, 8, 7]))
