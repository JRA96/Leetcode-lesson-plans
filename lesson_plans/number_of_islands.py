# https://leetcode.com/problems/number-of-islands/submissions/907975956/

def numIslands(self, grid: List[List[str]]) -> int:
    # Do you need to look at or touch EVERY point in the MxN grid or can you skip some?
    # What is the length and width of the grid?
    # Do we need to store our visited locations?  How can we do it? (Is there a better way for memory?)
    # step 1)
            # lets print the indexes of our 1's and see if it matches
    # step 2)
            # let's add the indexes to a data structure and see if that matches
            # This isn't enough yet, even though we know we can find all the land
            # need to count the islands
    # step 3)
            # let's start trying to count islands
            # How can we do it?  
            # check horizontally and vertically until there's no adjacent land left
            # Print indexes as we go and see if it matches what we saw before 
    # step 4)
            # add logic to increment island count once helper function has found all 1's (an island)

    number_of_islands = 0
    visited = {}
    width, length= len(grid[0]), len(grid)

    #Step 3) TODO
    def all_indexes(i, j):
        if (i, j) not in visited:

            if grid[i][j] == '1':
                # Print(visited) does it match what we saw in the last step? TODO
                visited[(i,j)] = 0
                if i - 1 >= 0:
                    all_indexes(i - 1, j)
                if i + 1 < length:
                    all_indexes(i + 1, j)
                if j - 1 >= 0:
                    all_indexes(i, j - 1)
                if j + 1 < width:
                    all_indexes(i, j + 1)
    
    # Step 1) TODO
    # for i, item in enumerate(grid):
    #         for j, point in enumerate(item):
    #             if point == '1':
    #                 print((i,j))

    # Step 2) TODO
    # for i, item in enumerate(grid):
    #         for j, point in enumerate(item):
    #             if point == '1':
    #                 visited[(i,j)] = 0

    # Step 4) TODO
    for i, item in enumerate(grid):
        for j, point in enumerate(item):
            if (i, j) not in visited and point == '1':
                all_indexes(i, j)
                number_of_islands += 1
    
    return number_of_islands