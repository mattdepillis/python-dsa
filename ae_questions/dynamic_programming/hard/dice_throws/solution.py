"""

"""
def recursive_determine_dice_throws(total_dice, remaining_dice, sides, target, prev, valid_combos):
    
    for value in range(1, sides + 1):
        adjusted_target = target - value
        if adjusted_target == 0 and remaining_dice > 0:
            prev.append(value)

            return prev
        elif adjusted_target < 0 or remaining_dice <= 0:
            break
        else:
            vc = recursive_determine_dice_throws(
                total_dice, remaining_dice - 1, sides, adjusted_target, prev + [value], valid_combos
            )
            if len(vc) > 0 and isinstance(vc[0], int) and len(vc) == total_dice: valid_combos.append(vc)
        print(valid_combos, prev, value, remaining_dice)
    
    return valid_combos

def dice_throws(num_dice, num_sides, target):
    valid_combos = recursive_determine_dice_throws(num_dice, num_dice, num_sides, target, [], [])
    print(valid_combos)
    return len(valid_combos)

if __name__ == "__main__":
    # print(dice_throws(
    #     num_dice=2, num_sides=6, target=7
    # ))

    print(dice_throws(
        num_dice=3, num_sides=10, target=12
    ))