import random
from paesslerNoise import generateNoisemap, writeNoisemap, readNoisemap

def generateMap(worldname, width, height):
    ground = generateNoisemap(width, height, (width*height) // 4)
    objects = generateNoisemap(width, height, (width*height) // 4)
    writeNoisemap(ground, worldname + "_ground.txt")
    writeNoisemap(objects, worldname + "_objects.txt")

def loadMap(worldname):
    ground = readNoisemap(worldname + "_ground.txt")
    objects = readNoisemap(worldname + "_objects.txt")
    return ground, objects
    
    

def generateTerrainGround(width, height):
    terrain = []

    for i in range(height):
        row = []
        
        for j in range(width):
            row.append("+")
        terrain.append(row)

    return terrain

def generateTerrainObjects(width, height):
    terrain = []

    for i in range(height):
        row = []
        
        for j in range(width):
            rng = random.randint(0, 10)
            if (rng == 0):
                row.append("#")
            
            else:
                row.append(" ")
                
        terrain.append(row)

    return terrain

def write_2d_list_to_file(data, filename):
    """
    Write a 2D Python list to a text file.

    Parameters:
        data (list): The 2D Python list to be written.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w") as file:
        for row in data:
            file.write(" ".join(map(str, row)) + "\n")


def read_2d_list_from_file(filename):
    """
    Read the contents of a text file into a 2D Python list.

    Parameters:
        filename (str): The name of the file to read from.

    Returns:
        list: The 2D Python list read from the file.
    """
    result = []
    with open(filename, "r") as file:
        for line in file:
            result.append(list(map(str, line.strip().split())))
    return result

def printTerrain(terrain):

    for i in range(len(terrain)):
        
        print(terrain[i])
        
            
                       
    

