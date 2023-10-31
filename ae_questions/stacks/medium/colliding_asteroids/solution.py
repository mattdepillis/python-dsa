"""
Given an array of integers representing asteroids (- moving left, + moving right), determine which asteroids collide with each other and which survive collisions.
Asteroids must be traveling in opposite directions to potentially crash into each other. If two asteroids collide, the smaller one (by absolute value) explodes. If they're the same size, they both explode.

TC: O(n) - must iterate through all asteroids
SC: O(n) - must store stack of max size = n
"""
def colliding_asteroids(asteroids):
    stack = []

    for i in range(len(asteroids)):
        stack.append(asteroids[i])

        if asteroids[i] < 0:
            j = len(stack) - 2
            while j >= 0 and stack[j] > 0:
                if abs(asteroids[i]) < abs(stack[j]):
                    stack.pop(len(stack) - 1)
                    break
                elif abs(asteroids[i]) == abs(stack[j]):
                    stack.pop(len(stack) - 1)
                    stack.pop(j)
                    break
                else:
                    stack.pop(j)
                    j -= 1

    return stack


if __name__ == "__main__":
    # print(colliding_asteroids(
    #     # [ -3, 5, -8, 6, 7, -4, -7 ] # [ -3, -8, 6 ]
    # ))

    # print(colliding_asteroids([5]))

    print(colliding_asteroids(
        [1, 2, 3, -4] # [-4]
    ))