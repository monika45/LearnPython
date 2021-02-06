class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # chs = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        # numbers = [1, 5, 10, 50, 100, 500, 1000]
        # ch_map = [('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]
        ch_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        special = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        result = 0
        i = 0
        j = 1
        special_keys = special.keys()
        slen = len(s)
        while j <= slen:
            if j < slen and (s[i] + s[j]) in special_keys:
                result += special[s[i] + s[j]]
                i += 2
                j = i + 1
            else:
                result += ch_map[s[i]]
                i += 1
                j += 1
        return result
