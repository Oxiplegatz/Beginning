# seen = {}
#
#
# class Solution:
#     def climb_stairs(self, n: int) -> int:
#         if n in seen:
#             return seen[n]
#         elif n == 1:
#             return 1
#         elif n == 2:
#             return 2
#         seen[n] = self.climb_stairs(n - 2) + self.climb_stairs(n - 1)
#         return self.climb_stairs(n - 2) + self.climb_stairs(n - 1)


def climb_stairs(n):
    # f(n) = f(n-1) + f(n-2)
    array = [1, 2]
    if n == 1:
        return 1
    for i in range(2, n):
        array.append(array[-1] + array[-2])
        print(array)
    return array[-1]


print(climb_stairs(6))
