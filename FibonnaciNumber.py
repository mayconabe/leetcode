class Solution:
    def fib(self, n: int) -> int:
        t1 = 0
        t2 = 1
        soma = 1
        count = 3

        lst = [t1, t2]

        while count <= n:
            t3 = t1 + t2
            t1 = t2
            t2 = t3
            lst.append(t3)
            count += 1

        lst.reverse()
        if n == 0:
            return 0
        else:  
            return sum(lst[:2])
