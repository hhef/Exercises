"""
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks
(5 inches each). Return True if it is possible to make the goal by choosing from the given bricks.
"""


def make_bricks(small, big, goal):
    final_goal = 0

    for i in range(big + 1):
        if final_goal == goal:
            break
        elif goal - final_goal < 5 or i == big:
            for j in range(small):
                if final_goal == goal:
                    break
                else:
                    final_goal += 1
            break
        else:
            final_goal += 5

    return final_goal == goal
