class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        
        z = []
        a = []
        
        i = 0
        n = len(t)
        
        while i < n and t[i] == '1':
            i += 1
            
        initial_ones = t.count('1') - 2
        
        while i < n:
            z_len = 0
            while i < n and t[i] == '0':
                z_len += 1
                i += 1
            z.append(z_len)
            
            a_len = 0
            while i < n and t[i] == '1':
                a_len += 1
                i += 1
            if i < n:
                a.append(a_len)

        k = len(a)
        if k == 0:
            return initial_ones
        
        m = len(z)
        pref_max = [0] * m
        suff_max = [0] * m
        
        curr_max = 0
        for idx in range(m):
            curr_max = max(curr_max, z[idx])
            pref_max[idx] = curr_max
            
        curr_max = 0
        for idx in range(m - 1, -1, -1):
            curr_max = max(curr_max, z[idx])
            suff_max[idx] = curr_max
            
        max_gain = 0
        
        for idx in range(k):
            a_i = a[idx]
            z_left = z[idx]
            z_right = z[idx + 1]
            
            gain = z_left + z_right
            
            other_max = 0
            if idx > 0:
                other_max = max(other_max, pref_max[idx - 1])
            if idx + 2 < m:
                other_max = max(other_max, suff_max[idx + 2])
                
            gain = max(gain, other_max - a_i)
            max_gain = max(max_gain, gain)
            
        return initial_ones + max_gain