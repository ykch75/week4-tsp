
import sys
import math

from common import print_solution, read_input

def distance(city1, city2) :
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

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

def goNear(citiesGone, citiesLeft) :
    dist = distance(citiesGone[-1],citiesLeft[0])
    next = citiesLeft[0]
    for city in citiesLeft[1:] :
        if distance(citiesGone[-1], city) < dist :
            next = city
            dist = distance(citiesGone[-1], city)
    citiesLeft.remove(next)
    citiesGone.append(next)
    return [citiesGone, citiesLeft]

def goGreedy(cities) :
    if not cities :
        return []
    citiesGone = [cities[0]]
    citiesLeft = cities[1:]
    while len(citiesLeft) > 0 :
        list = goNear(citiesGone, citiesLeft)
        citiesGone = list[0]
        citiesLeft = list[1]
    return citiesGone

def mergeArea(area1, area2): #area should be a list. Return a list.
    if len(area1) == 0 :
        return area2
    if len(area2) == 0 :
        return area1
    start = area1[0]
    connect = area2[0]
    dist = distance(start, connect)
    result = []
    for a in area1 :
        for b in area2 :
            if distance(a,b) < dist :
                connect = b
                start = a
                dist = distance(a,b)
    startIndex = area1.index(start) + 1
    connectIndex = area2.index(connect) + 1
    result.extend(area1[:startIndex])
    result.extend(area2[connectIndex:])
    result.extend(area2[:connectIndex])
    result.extend(area1[startIndex:])
    return result

def solve(cities) :
    G = g(cities)
    area = {"a":[], "b":[], "c":[], "d":[], "e":[], "f":[], "g":[], "h":[], "O":[]}
    goOut = ["a", "c", "e", "g"]
    goIn = ["b", "d", "f", "h"]
    order = ["a", "b", "c", "d", "e", "f", "g", "h", "O"]
    areaGreedy = {"a":[], "b":[], "c":[], "d":[], "e":[], "f":[], "g":[], "h":[], "O":[]}
    solutionCity = []
    solution = []
    for city in cities :
        tan = gTan(G, city)
        dist = distance(G, city)
        area[getArea(G, city, tan, dist)].append(city)

    for x in goOut :
        areaGreedy[x].extend(goGreedy(area[x]))

    for x in goIn :
        areaGreedy[x].extend(goGreedy(area[x]))

    for i in order :
        solutionCity = mergeArea(solutionCity, areaGreedy[i])

    for city in solutionCity :
        solution.append(cities.index(city))
    # for n in order :
    #     for j in areaGreedy[n] :
    #         solution.append(cities.index(j))

    return solution

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
