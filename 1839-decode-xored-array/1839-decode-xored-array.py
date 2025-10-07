class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first] * (len(encoded) + 1)
        for i in range(len(encoded)):
            arr[i+1] = arr[i] ^ encoded[i]

        return arr