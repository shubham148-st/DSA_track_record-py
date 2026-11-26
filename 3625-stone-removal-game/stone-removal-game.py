class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        alice_turn = True

        while n >= remove and remove > 0:
            n -= remove
            remove -= 1
            alice_turn = not alice_turn

        return not alice_turn