class Solution:

    def combination_sum_3(self, k: int, n: int) -> list[list[int]]:

        min_sum = {
            1: 1,
            2: 3,
            3: 6,
            4: 10,
            5: 15,
            6: 21,
            7: 28,
            8: 36,
            9: 45
        }

        max_sum = {
            1: 9,
            2: 17,
            3: 24,
            4: 30,
            5: 35,
            6: 39,
            7: 42,
            8: 44,
            9: 45
        }

        eight_results = {
            37: [1, 2, 3, 4, 5, 6, 7, 9],
            38: [1, 2, 3, 4, 5, 6, 8, 9],
            39: [1, 2, 3, 4, 5, 7, 8, 9],
            40: [1, 2, 3, 4, 6, 7, 8, 9],
            41: [1, 2, 3, 5, 6, 7, 8, 9],
            42: [1, 2, 4, 5, 6, 7, 8, 9],
            43: [1, 3, 4, 5, 6, 7, 8, 9]
        }

        min_arr = [num for num in range(1, k + 1)]
        max_arr = [num for num in range(10 - k, 10)]

        if n < min_sum[k] or n > max_sum[k]:
            return []
        if n == min_sum[k]:
            return [min_arr]
        if n == max_sum[k]:
            return [max_arr]
        if k == 8:
            return [eight_results[n]]
        else:
            result = []
            start_number = int(''.join([str(num) for num in min_arr]))
            end_number = int(''.join([str(num) for num in max_arr]))

            for number in range(start_number, end_number + 1):
                num_list = [int(digit) for digit in str(number)]
                if sum(num_list) == n and len(num_list) == len(set(num_list)):
                    if sorted(num_list) not in result and 0 not in num_list:
                        result.append(sorted(num_list))
                if k == 7 and len(result) == 4:
                    break

        return result


check1 = Solution().combination_sum_3(7, 33)
print(check1)
