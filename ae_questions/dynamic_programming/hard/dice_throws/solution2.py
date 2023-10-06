"""

"""
def recursive_determine_dice_throws(remaining_dice, sides, target, results):
    if remaining_dice == 0:
        return 1 if target == 0 else 0
    
    if results[remaining_dice][target] > -1:
        return results[remaining_dice][target]
    
    ways_to_reach_target = 0
    for t in range(max(0, target - sides), target):
        ways_to_reach_target += recursive_determine_dice_throws(
            remaining_dice - 1, sides, t, results
        )

    results[remaining_dice][target] = ways_to_reach_target
    print(remaining_dice, target)
    print(results)
    print("\n")

    return ways_to_reach_target

def dice_throws(num_dice, num_sides, target):
    results = [[-1] * (target + 1) for _ in range(num_dice + 1)]
    return recursive_determine_dice_throws(num_dice, num_sides, target, results)

if __name__ == "__main__":
    print(dice_throws(
        num_dice=2, num_sides=6, target=7
    ))

    # print(dice_throws(
    #     num_dice=3, num_sides=10, target=12
    # ))

    # print(dice_throws(
    #     num_dice=11, num_sides=9, target=32
    # ))