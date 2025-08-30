class Solution:
    def splitNum(self, num: int) -> int:       
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        
        digits.sort()
        num1 = num2 = ""
        for i in range(0, len(digits), 2):
            num1 += str(digits[i])
            if i+1 < len(digits):
                num2 += str(digits[i+1])
                
        return int(num1) + int(num2)
