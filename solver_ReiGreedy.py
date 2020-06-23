
import sys
import math

from common import print_solution, read_input

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

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

def solve(cities) :
    citiesGone = [cities[0]]
    citiesLeft = cities[1:]
    while len(citiesLeft) > 0 :
        list = goNear(citiesGone, citiesLeft)
        citiesGone = list[0]
        citiesLeft = list[1]
    solution = []
    for x in citiesGone :
        solution.append(cities.index(x))
    return solution

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
