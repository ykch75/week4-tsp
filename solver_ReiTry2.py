
import sys
import math

from common import print_solution, read_input

def distance(city1, city2) :
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def areaBreakpoint33(cities) :
    #Cauculate the breakpoint of each area,
    #Return [XBPlist,YBPlist]
    citiesX = []
    citiesY = []
    areaBPX = []
    areaBPY = []
    for spot in cities :
        citiesX.append(spot[0])
        citiesY.append(spot[1])
    maxX = max(citiesX)
    maxY = max(citiesY)
    spaceX = maxX /3
    spaceY = maxY /3

    for i in range(1,4) :
        areaBPX.append(0+i*spaceX)
        areaBPY.append(0+i*spaceY)
    return [areaBPX , areaBPY]

def areaApart(cities, bpList33) :
    area = {"a":[], "b":[], "c":[], "d":[], "e":[], "f":[], "g":[], "h":[], "i":[]}
    areaBPX = bpList33[0]
    areaBPY = bpList33[1]
    for city in cities :
        cityX = city[0]
        cityY = city[1]
        areaC = None
        if cityX <= areaBPX[0] :
            if cityY <= areaBPY[0] :
                areaC = "a"
            elif cityY <= areaBPY[1] :
                areaC = "b"
            else :
                areaC = "c"

        elif cityX <= areaBPX[1] :
            if cityY <= areaBPY[0] :
                areaC = "d"
            elif cityY <= areaBPY[1] :
                areaC = "e"
            else :
                areaC = "f"
        else :
            if cityY <= areaBPY[0] :
                areaC = "g"
            elif cityY <= areaBPY[1] :
                areaC = "h"
            else :
                areaC = "i"

        area[areaC].append(city)
    return area

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

def distShorten(city1_1, city1_2, city2_1, city2_2): #To calculate the distance shorten.
    originDist = distance(city1_1, city1_2) + distance(city1_2, city2_2)
    newDist = distance(city1_1, city2_2) + distance(city1_2,city2_1)
    return originDist - newDist


def mergeArea(area1, area2): #area should be a list. Return a list.
    nA1 = len(area1)
    nA2 = len(area2)
    if nA1 == 0 :
        return area2
    if nA2 == 0 :
        return area1
    start = -1
    connect = -1
    distS = distShorten(area1[-1], area1[0], area2[-1], area2[0])
    result = []
    for i in range(0,nA1-1) :
        for j in range(0,nA2-1) :
            if  distShorten(area1[i], area1[i+1], area2[j], area2[j+1]) > distS :
                connect = j
                start = i
                distS = distShorten(area1[i], area1[i+1], area2[j], area2[j+1])
    result.extend(area1[:start +1])
    result.extend(area2[connect +1:])
    result.extend(area2[:connect +1])
    result.extend(area1[start +1:])
    return result


def solve(cities):
    solutionCity = []
    solution = []
    bpList = areaBreakpoint33(cities)
    area = areaApart(cities, bpList)
    areaGreedy = {"a":[], "b":[], "c":[], "d":[], "e":[], "f":[], "g":[], "h":[], "i":[]}
    order =["a", "b", "c", "f", "e", "d", "g", "h", "i"]
    for key in area :
        areaGreedy[key].extend(goGreedy(area[key]))
    for area in order :
        solutionCity = mergeArea(solutionCity, areaGreedy[area])
    for i in solutionCity :
        solution.append(cities.index(i))
    return solution

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
