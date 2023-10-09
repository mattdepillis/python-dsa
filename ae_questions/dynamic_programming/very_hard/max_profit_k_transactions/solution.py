"""

"""
def max_profit_k_transactions(prices, k):
    matrix = [[0] * len(prices) for _ in range(k + 1)]

    for num_k in range(1, len(matrix)):
        adjusted_min_index = num_k - 1

        for day in range(len(prices)):
            if day < num_k: matrix[num_k][day] = matrix[num_k - 1][day]
            elif prices[day] < prices[day - 1]:
                matrix[num_k][day] = matrix[num_k][day - 1]
                if prices[day] < prices[adjusted_min_index]: adjusted_min_index = day
            else:
                profit_option_one = prices[day] - prices[adjusted_min_index] + matrix[num_k - 1][adjusted_min_index]
                profit_option_two = prices[day] - prices[day - 1] + matrix[num_k - 1][day - 1]
                if profit_option_one > profit_option_two:
                    matrix[num_k][day] = profit_option_one
                else:
                    matrix[num_k][day] = profit_option_two
                    adjusted_min_index = day - 1

    return 0 if len(prices) == 0 else matrix[-1][-1]


if __name__ == "__main__":
    print(max_profit_k_transactions([5, 11, 3, 50, 60, 90], 2))

    print(max_profit_k_transactions(
        [1, 25, 24, 23, 12, 36, 14, 40, 31, 41, 5], 2
    ))

    print(max_profit_k_transactions([], 1))