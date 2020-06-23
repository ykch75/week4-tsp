
import sys
import math

from common import print_solution, read_input

def gDistance(g, city) : #與重心的距離
    return math.sqrt((city[0] - g[0]) ** 2 + (city[1] - g[1]) ** 2)

def g(cities) : #算重心
    n = len(cities)
    xSum = 0
    ySum = 0
    for spot in cities :
        xSum += spot[0]
        ySum += spot[1]
    return (xSum/n , ySum/n)

def gTan(g, city) : #算tan
    if city[0] == g[0] :
        return None
    return (city[0] - g[0])/(city[1] - g[1])

def getArea(g ,city ,gTan, gDistance):
    if (gTan > 0) and (gTan <= 1) and (city[0] > g[0]) :
        return "a"
    if (gTan > 1) and (city[0] > g[0]) :
        return "b"
    if (gTan <= -1) and (city[0] < g[0]) :
        return "c"
    if (gTan <= 0) and (gTan > -1) and (city[0] < g[0]):
        return "d"
    if (gTan > 0) and (gTan <= 1) :
        return "e"
    if (gTan > 1) :
        return "f"
    if (gTan <= -1) :
        return "g"
    if (gTan > -1) and (gTan <= 0) :
        return "h"
    if not gTan :
        if city[1] > g[1] :
            return "h"
        if city[1] < g[1] :
            return "d"
        if city[1] == g[1] :
            return "O"


def solve(cities) :
    G = g(cities)

    area = {"a":[], "b":[], "c":[], "d":[], "e":[], "f":[], "g":[], "h":[], "O":[]}
    goOut = ["a", "c", "e", "g"]
    goIn = ["b", "d", "f", "h"]
    order = ["a", "b", "c", "d", "e", "f", "g", "h", "O"]
    solution = []
    for city in cities :
        tan = gTan(G, city)
        distance = gDistance(G, city)
        area[getArea(G, city, tan, distance)].append([distance, tan, city])
    def getDist(list):
        return list[0]

    for x in goOut :
        area[x].sort(key=getDist)
    for x in goIn :
        area[x].sort(reverse=True, key=getDist)
    for i in order :
        for j in area[i] :
            solution.append(cities.index(j[2]))
    return solution

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
