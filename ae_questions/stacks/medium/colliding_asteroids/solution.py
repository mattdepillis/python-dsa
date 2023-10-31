"""

"""
def colliding_asteroids(asteroids):
    stack = []

    for i in range(len(asteroids)):
        if len(stack) == 0 or stack[-1] < 0 or (stack[-1] > 0 and asteroids[i] > 0):
            stack.append(asteroids[i])
        else:
            if abs(stack[len(stack) - 1]) < abs(asteroids[i]):
                stack[len(stack) - 1] = asteroids[i]
            elif abs(stack[len(stack) - 1]) == abs(asteroids[i]):
                stack.pop(len(stack) - 1)

    return stack


if __name__ == "__main__":
    print(colliding_asteroids(
        [ -3, 5, -8, 6, 7, -4, -7 ] # [ -3, -8, 6 ]
    ))

    # print(colliding_asteroids([5]))

    print(colliding_asteroids(
        [1, 2, 3, -4] # [-4]
    ))