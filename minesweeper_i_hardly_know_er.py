'''
Program that dynamically creates a Minesweeper grid and shows it cleared
'''

import random


def generate_map(rows, columns):
    """
    Create a 2D list with the bounds specified and populate it with a
    programmically selected dash (empty tile) or hash (mine) with a slightly
    higher probability of selecting a dash 

    Args:
        rows (int): the length of our y axis
        columns (int): the length of our x axis

    Returns:
        minefield (list): a 2D list
    """
    
    possible_tiles = ["-", "-", "#"]
    minefield = [
        [random.choice(possible_tiles) for i in range(columns)]
        for j in range(rows)
        ]
    
    return minefield


def check_bounds(axis, n):
    """
    Determines where the valid bounds of a tile adjacent to our target would 
    start and end (either one tile before/after the target or not at all) based
    off of the length of its axis and its position in it

    Args:
        axis (list): either the parent list or a list within the parent list,
            the formula is the same
        n (int): the index of our target tile in the list   

    Returns:
        range: a range that can start with -1 and end with 2, which we will later
            iterate over to automatically create valid co-ordinates to check
    """
    
    START = 0 if n == 0 else -1
    END = 1 if n == (len(axis) - 1) else 2
    
    return range(START, END)


def sweep_target(minefield, nth_row, nth_col):
    """Takes the target tile and its position in the parent list and the list.
    With the target tile as reference, the function refers to the bounds check
    function for a range of existing adjacent tiles, and then uses a nested for
    loop to create every possible combination of "co-ordinates" within those
    validated ranges. Then, it checks for a bomb at every co-ordinate and 
    returns a mine-count once it has finished.

    Args:
        minefield (list): our grid, given locally for efficiency
        nth_row (int): the target's index in the parent list
        nth_col (int): the target's index in the list

    Returns:
        string: The target tile's count of adjacent mines, cast to string for
        formatting's sake
    """
    
    mines = 0
    
    # With the bounds as -1 through 1, we can join our indices with
    # each individual number in these lists to find the adjacent indices
    y_bounds = check_bounds(minefield, nth_row)
    x_bounds = check_bounds(minefield[nth_row], nth_col)
    
    for y in y_bounds: 
        for x in x_bounds:
            if minefield[nth_row + y][nth_col + x] == "#":
                mines += 1
    
    return str(mines)


def solve(minefield):
    """Performs the sweep function on each individual empty tile, which passes
    it through the program until every tile has been replaced with the return
    value of the sweep function

    Args:
        minefield (list): our grid, given locally

    Returns:
        minefield (list): our grid, solved! 
    """
    
    for y in range(len(minefield)):
        for x in range(len(minefield[y])):
            if minefield[y][x] != "#":
                minefield[y][x] = sweep_target(minefield, y, x)
                
    return minefield


def main():
    minefield = generate_map(6, 6)
    [print(x) for x in minefield]
    print("\n")
    show_solution = solve(minefield)
    [print(x) for x in show_solution]


if __name__ == "__main__":
    main()