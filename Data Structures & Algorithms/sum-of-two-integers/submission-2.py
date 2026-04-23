class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 32) - 1
        max_int = 1 << 31
        while b != 0:
            carry = (a & b) << 1 
            a = (a ^ b) & mask 
            b = carry & mask 
        
        return a if a < max_int else a - (1 << 32)

        