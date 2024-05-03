import random


def generateNoisemap(width, height, paessValue):
    '''

generates a noisemap with certain shape. paessValue is the number of ones that gets
renadomly placed before smoothing everthing out (aka how "full" it is)
'''
    grid = []
    for y in range(height):
        collumn = []
        for x in range(width):
            collumn.append(0.0)
        grid.append(collumn)

    for i in range(paessValue):
        x = random.randint(0, width)
        y = random.randint(0, height)
        grid[y - 1][x - 1] = 1.0

    
    
    for y in range(height):
        for x in range(width):
            try:
                value = grid[y][x]
                
                
                up = grid[y - 1][x]
                down = grid[y + 1][x]
                left = grid[y][x - 1]
                right = grid[y][x + 1]
                upleft = grid[y - 1][x - 1]
                upright = grid[y - 1][x + 1]
                downleft = grid[y + 1][x - 1]
                downright = grid[y + 1][x + 1]

                average = up + down + left + right + upleft + upright + downleft + downright
                average /= 8
                grid[y][x] = float(round(average, 1))
                
            except IndexError:
                pass
                   

    
                   
    
    return grid

def seedetNoise(x, y):
    n = x + y * 57
    n = (n << 13)**n
    return (1.0 - ( (n * (n * n * 15731 + 789221) + 1376312589)& 2147483647) / 1073741824.0)

def generateSeedetNoisemap(width, height):
    noisemap = []
    for y in range(height):
        collumn = []
        for x in range(width):
            collumn.append(seedetNoise(x, y))
        noisemap.append(collumn)
    return noisemap

def writeNoisemap(array, filename, delimiter=' '):
    with open(filename, 'w') as file:
        for row in array:
            line = delimiter.join(map(str, row)) + '\n'
            file.write(line)


def readNoisemap(filename, delimiter=' '):
    with open(filename, 'r') as file:
        lines = file.readlines()
        array = []
        for line in lines:
            row = list(map(float, line.strip().split(delimiter)))
            array.append(row)
    return array
            

def printNoisemap(noise):
    
    for y in range(len(noise)):
        print(noise[y])
    


