class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        sol = ["1"] * n
        for i in range(1, n):
            if ((i+1) % 3 == 0) and ((i+1) % 5 == 0):
                sol[i] = "FizzBuzz"
            elif (i+1) % 3 == 0:
                sol[i] = "Fizz"
            elif (i+1) % 5 == 0:
                sol[i] = "Buzz"
            else:
                sol[i] = str(i+1)
        return sol

        