class Solution:
    def largestCombination(candidates):
        binary = []
        length = len(bin(max(candidates))[2:])
        res = 0
        for candidate in candidates:
            s = bin(candidate)[2:]
            binary.append("0" * (length - len(s)) + s)
        for i in range(length):
            cnt = 0
            for b in binary:
                if b[i] == "1":
                    cnt += 1
                res = max(res, cnt)
        return res
        