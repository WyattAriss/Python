########################################
### MAZE SOLVER (CMPT 120 Assignment #2)
### Date: April 10th 2014
### Team (name and SFU ID):
###   - Wyatt Ariss (wariss)
########################################
file = open("maze1.txt", "r") #Filename to read
wfile = open("answer-maze.txt", "w") #Filename to write
maze = []
WALL = -1
CORRIDOR = 0
MINOTAUR = 2
START_ROW = 1
START_COLUMN = 0

#Convert the maze from #'s and spaces to -1's and 0's
def maze_converter(file):
    for line in file:
        maze_line = []
        for char in line:
            if char == "#":
                maze_line.append(WALL)
            elif char ==  " ":
                maze_line.append(CORRIDOR)
            elif char == "M":
                maze_line.append(MINOTAUR)
        maze.append(maze_line)
    return maze
def flood_fill(maze, start_row, start_column, source_color, dest_color, flag=False): #Flag = whether or not we see a minotaur

    #check if we have exited the maze, but not through the entrance!
    if (start_row < 0 or start_column < 0) and (start_row != START_ROW and start_column != START_COLUMN-1):
        if flag == True:
            return "DEAD"
        else:
            return "ALIVE"

    if start_row > len(maze)-1  or start_column > len(maze[0])-1:
        if flag == True:
            return "DEAD"
        else:
            return "ALIVE"

    #Flag only remains True for the recursions that come after (ex. if the minotaur is on the path to the exit).
    #When the recursions go backwards to the coordinates right before the minotaur, flag is still false.
    if maze[start_row][start_column] == MINOTAUR:
        flag = True

    if maze[start_row][start_column] == source_color or maze[start_row][start_column] == MINOTAUR:
        maze[start_row][start_column] = dest_color
        var = flood_fill(maze, start_row, start_column+1, source_color, dest_color, flag)
        if var != "DEAD" and var != "ALIVE":
            var = flood_fill(maze, start_row, start_column-1, source_color, dest_color, flag)
        if var != "DEAD" and var != "ALIVE":
            var = flood_fill(maze, start_row+1, start_column, source_color, dest_color, flag)
        if var != "DEAD" and var != "ALIVE":
            var = flood_fill(maze, start_row-1, start_column, source_color, dest_color, flag)
        return var
    else:
        return "STUCK"

result = flood_fill(maze_converter(file), START_ROW, START_COLUMN, 0, 1)
print result
wfile.writelines(result)
file.close()
wfile.close()
