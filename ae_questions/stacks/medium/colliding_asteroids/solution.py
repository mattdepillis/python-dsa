"""

"""
def colliding_asteroids(asteroids):
    stack = []

    for i in range(len(asteroids)):
        stack.append(asteroids[i])
        
        if asteroids[i] < 0:
            j = len(stack) - 2
            while j >= 0:
                if stack[j] < 0: break
                elif abs(asteroids[i]) < abs(stack[j]):
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