class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        x = 0
        n = len(encoded)

        # XOR of all numbers from 1 to n+1 (since perm has n+1 elements)
        for i in range(1, n + 2):
            x ^= i

        # XOR every second encoded value to get the first element of perm
        for i in range(1, n, 2):
            x ^= encoded[i]
        
        perm = [0] * (n + 1)
        perm[0] = x

        # Reconstruct the permutation
        for i in range(n):
            perm[i + 1] = perm[i] ^ encoded[i]

        return perm
