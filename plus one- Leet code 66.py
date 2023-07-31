class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        int_con = 0
        out_arr =[]
        for x in range(0,len(digits)):
            num = digits.pop(0)
            num = int(num)
            power = len(digits)
            int_con = int_con + (num * (10 ** power ))
        int_con +=1
        int_con = str(int_con)
        for x in int_con:
            out_arr.append(int(x))
        return(out_arr)
