class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        rem = t
        c7, c5, c3, c2 = 0, 0, 0, 0
        
        while rem % 7 == 0:
            c7 += 1
            rem //= 7
        while rem % 5 == 0:
            c5 += 1
            rem //= 5
        while rem % 3 == 0:
            c3 += 1
            rem //= 3
        while rem % 2 == 0:
            c2 += 1
            rem //= 2
            
        if rem > 1:
            return "-1"
            
        n = len(num)
        
        def get_min_digits(r2, r3, r5, r7):
            s = []
            while r7 > 0:
                s.append('7')
                r7 -= 1
            while r3 >= 2:
                s.append('9')
                r3 -= 2
            while r2 >= 3:
                s.append('8')
                r2 -= 3
            while r2 >= 1 and r3 >= 1:
                s.append('6')
                r2 -= 1
                r3 -= 1
            while r5 > 0:
                s.append('5')
                r5 -= 1
            while r2 >= 2:
                s.append('4')
                r2 -= 2
            while r3 > 0:
                s.append('3')
                r3 -= 1
            while r2 > 0:
                s.append('2')
                r2 -= 1
            s.sort()
            return "".join(s)

        min_req_str = get_min_digits(c2, c3, c5, c7)
        if len(min_req_str) > n:
            return min_req_str

        # Find the first zero if any
        zero_idx = -1
        for i in range(n):
            if num[i] == '0':
                zero_idx = i
                break

        if zero_idx != -1:
            prefix = num[:zero_idx]
            p2, p3, p5, p7 = 0, 0, 0, 0
            for c in prefix:
                d = int(c)
                while d % 7 == 0:
                    p7 += 1
                    d //= 7
                while d % 5 == 0:
                    p5 += 1
                    d //= 5
                while d % 3 == 0:
                    p3 += 1
                    d //= 3
                while d % 2 == 0:
                    p2 += 1
                    d //= 2
            rem2 = max(0, c2 - p2)
            rem3 = max(0, c3 - p3)
            rem5 = max(0, c5 - p5)
            rem7 = max(0, c7 - p7)
            
            suffix = get_min_digits(rem2, rem3, rem5, rem7)
            if len(prefix) + len(suffix) <= n:
                res = prefix
                while len(res) + len(suffix) < n:
                    res += '1'
                return res + suffix

        # Check if current num is already valid
        p2, p3, p5, p7 = 0, 0, 0, 0
        has_zero = False
        for c in num:
            if c == '0':
                has_zero = True
            d = int(c)
            if d > 0:
                while d % 7 == 0:
                    p7 += 1
                    d //= 7
                while d % 5 == 0:
                    p5 += 1
                    d //= 5
                while d % 3 == 0:
                    p3 += 1
                    d //= 3
                while d % 2 == 0:
                    p2 += 1
                    d //= 2
        if not has_zero and p2 >= c2 and p3 >= c3 and p5 >= c5 and p7 >= c7:
            return num

        # Backtrack from right to left to find the smallest valid greater number
        cur2, cur3, cur5, cur7 = 0, 0, 0, 0
        for c in num:
            d = int(c)
            if d == 0:
                continue
            while d % 7 == 0:
                cur7 += 1
                d //= 7
            while d % 5 == 0:
                cur5 += 1
                d //= 5
            while d % 3 == 0:
                cur3 += 1
                d //= 3
            while d % 2 == 0:
                cur2 += 1
                d //= 2

        for i in range(n - 1, -1, -1):
            d_curr = int(num[i])
            if d_curr > 0:
                d2, d3, d5, d7 = 0, 0, 0, 0
                tmp = d_curr
                while tmp % 7 == 0:
                    d7 += 1
                    tmp //= 7
                while tmp % 5 == 0:
                    d5 += 1
                    tmp //= 5
                while tmp % 3 == 0:
                    d3 += 1
                    tmp //= 3
                while tmp % 2 == 0:
                    d2 += 1
                    tmp //= 2
                cur2 -= d2
                cur3 -= d3
                cur5 -= d5
                cur7 -= d7

            for d_val in range(max(1, d_curr + 1), 10):
                d_char = str(d_val)
                nd2, nd3, nd5, nd7 = 0, 0, 0, 0
                ntmp = d_val
                while ntmp % 7 == 0:
                    nd7 += 1
                    ntmp //= 7
                while ntmp % 5 == 0:
                    nd5 += 1
                    ntmp //= 5
                while ntmp % 3 == 0:
                    nd3 += 1
                    ntmp //= 3
                while ntmp % 2 == 0:
                    nd2 += 1
                    ntmp //= 2

                rem2 = max(0, c2 - (cur2 + nd2))
                rem3 = max(0, c3 - (cur3 + nd3))
                rem5 = max(0, c5 - (cur5 + nd5))
                rem7 = max(0, c7 - (cur7 + nd7))

                suffix = get_min_digits(rem2, rem3, rem5, rem7)
                candidate = num[:i] + d_char
                if len(candidate) + len(suffix) <= n:
                    while len(candidate) + len(suffix) < n:
                        candidate += '1'
                    return candidate + suffix

        # Fallback: If no valid number of length n exists, construct one of length n + 1
        target_len = max(n + 1, len(min_req_str))
        res = ""
        while len(res) + len(min_req_str) < target_len:
            res += '1'
        return res + min_req_str