class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def convert_to_days(date: str) -> int:
            month, day = map(int, date.split('-'))
            return sum(days[:month - 1]) + day
            
        alice_start = convert_to_days(arriveAlice)
        alice_end = convert_to_days(leaveAlice)
        bob_start = convert_to_days(arriveBob)
        bob_end = convert_to_days(leaveBob)
        
        overlap_start = max(alice_start, bob_start)
        overlap_end = min(alice_end, bob_end)
        
        return max(0, overlap_end - overlap_start + 1)