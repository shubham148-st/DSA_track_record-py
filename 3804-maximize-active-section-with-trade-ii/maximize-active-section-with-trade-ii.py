class SparseTable:
    def __init__(self, nums):
        self.n = len(nums)
        if self.n == 0:
            return

        max_log = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(max_log)]

        for j in range(self.n):
            self.st[0][j] = nums[j]

        for i in range(1, max_log):
            length = 1 << (i - 1)
            for j in range(self.n - (1 << i) + 1):
                self.st[i][j] = max(self.st[i - 1][j], self.st[i - 1][j + length])

    def query(self, l, r):
        if l > r or self.n == 0:
            return 0
        i = (r - l + 1).bit_length() - 1
        return max(self.st[i][l], self.st[i][r - (1 << i) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        totalOnes = s.count('1')

        zeroGroups = []
        zeroGroupIndex = []

        for i in range(n):
            if s[i] == '0':
                if i > 0 and s[i - 1] == '0':
                    zeroGroups[-1]['length'] += 1
                else:
                    zeroGroups.append({'start': i, 'length': 1})
            zeroGroupIndex.append(-1 if not zeroGroups else len(zeroGroups) - 1)

        if not zeroGroups:
            return [totalOnes] * len(queries)

        zeroMergeLengths = [
            zeroGroups[i]['length'] + zeroGroups[i + 1]['length']
            for i in range(len(zeroGroups) - 1)
        ]

        st = SparseTable(zeroMergeLengths)
        ans = []

        for l, r in queries:
            left = zeroGroups[zeroGroupIndex[l]]['length'] - (l - zeroGroups[zeroGroupIndex[l]]['start']) if s[l] == '0' else 0
            right = (r - zeroGroups[zeroGroupIndex[r]]['start'] + 1) if (s[r] == '0' and zeroGroupIndex[r] != -1) else 0

            startAdjacentGroupIndex = zeroGroupIndex[l] + 1
            endAdjacentGroupIndex = (zeroGroupIndex[r] if s[r] == '1' else zeroGroupIndex[r] - 1) - 1

            activeSections = totalOnes

            if s[l] == '0' and s[r] == '0' and zeroGroupIndex[l] + 1 == zeroGroupIndex[r]:
                activeSections = max(activeSections, totalOnes + left + right)
            elif startAdjacentGroupIndex <= endAdjacentGroupIndex:
                activeSections = max(activeSections, totalOnes + st.query(startAdjacentGroupIndex, endAdjacentGroupIndex))

            if s[l] == '0' and zeroGroupIndex[l] + 1 <= (zeroGroupIndex[r] if s[r] == '1' else zeroGroupIndex[r] - 1):
                activeSections = max(activeSections, totalOnes + left + zeroGroups[zeroGroupIndex[l] + 1]['length'])

            if s[r] == '0' and zeroGroupIndex[l] < zeroGroupIndex[r] - 1:
                activeSections = max(activeSections, totalOnes + right + zeroGroups[zeroGroupIndex[r] - 1]['length'])

            ans.append(activeSections)

        return ans