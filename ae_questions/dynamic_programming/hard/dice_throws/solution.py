"""

"""
def recursive_determine_dice_throws(remaining_dice, sides, target, prev):
    valid_combos = []

    # print(f"remaining_dice: {remaining_dice}, target: {target}, prev: {prev}")

    for val in range(1, sides + 1):
        if target - val > 0 and remaining_dice > 0:
            valid_combos += recursive_determine_dice_throws(
                remaining_dice - 1, sides, target - val, prev + [val]
            )
        else:
            if target - val == 0 and remaining_dice == 1: valid_combos.append(prev + [val])
            break
    
    return valid_combos


def dice_throws(num_dice, num_sides, target):
    valid_combos = recursive_determine_dice_throws(num_dice, num_sides, target, [])
    print(valid_combos)
    return len(valid_combos)

if __name__ == "__main__":
    # print(dice_throws(
    #     num_dice=2, num_sides=6, target=7
    # ))

    # print(dice_throws(
    #     num_dice=3, num_sides=10, target=12
    # ))

    print(dice_throws(
        num_dice=11, num_sides=9, target=32
    ))