#!/usr/bin/env python3

import sys
import math

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def opt(tour,dist):
    # 最後は出発点に戻ってくるため、0も入れて最適化する
    tour.append(0)
    for i in range(len(tour)-1):
        for j in range(i+2, len(tour)-2):
            current_dis = dist[tour[i]][tour[i+1]] + dist[tour[i+1]][tour[i+2]] + dist[tour[j]][tour[j+1]] + dist[tour[j+1]][tour[j+2]]
            new_dis = dist[tour[i]][tour[j+1]] + dist[tour[j+1]][tour[i+1]] + dist[tour[i+1]][tour[i+2]] + dist[tour[j]][tour[j+2]]
            new_dis2 = dist[tour[i]][tour[i+2]] + dist[tour[j]][tour[j+1]] + dist[tour[j+1]][tour[i+1]] + dist[tour[i+1]][tour[j+2]]
            if new_dis < current_dis:
                #print(i,j)
                tmp = tour[j+1]
                del tour[j+1]
                tour.insert(i+1, tmp)
            
            elif new_dis2 < current_dis:
                #print(i,j)
                tmp = tour[i+1]
                del tour[i+1]
                tour.insert(j+1, tmp)
    del tour[-1]
    return tour

def opt2(tour, dist):
    tour.append(0)
    for i in range(1,len(tour)-2):
        for j in range(i+3,len(tour)-2):
            current_dis = dist[tour[i-1]][tour[i]] + dist[tour[i]][tour[i+1]] + dist[tour[i+1]][tour[i+2]] + dist[tour[j-1]][tour[j]] + dist[tour[j]][tour[j+1]] + dist[tour[j+1]][tour[j+2]] 
            new_dis = dist[tour[i-1]][tour[i]] + dist[tour[i]][tour[j]] + dist[tour[j]][tour[j+1]] + dist[tour[j+1]][tour[i+1]] + dist[tour[i+1]][tour[i+2]] + dist[tour[j-1]][tour[j+2]]
            new_dis2 = dist[tour[i-1]][tour[i+2]] + dist[tour[j-1]][tour[j]] + dist[tour[j]][tour[i]] + dist[tour[i]][tour[i+1]] + dist[tour[i+1]][tour[j+1]] + dist[tour[j+1]][tour[j+2]]
            if new_dis < current_dis:
                #print(i,j)
                tmp1 = tour[j]
                tmp2 = tour[j+1]
                del tour[j]
                del tour[j]
                tour.insert(i+1, tmp1)
                tour.insert(i+2, tmp2)
        
            elif new_dis2 < current_dis:
                #print("2",i,j)
                tmp1 = tour[i]
                tmp2 = tour[i+1]
                del tour[i]
                del tour[i]
                tour.insert(j+1, tmp1)
                tour.insert(j+2, tmp2)    
                #print(tour)
    del tour[-1]
    return tour          

def swap(tour,dist):
    tour.append(0)
    for i in range(len(tour)-1):
        for j in range(i+2,len(tour)-1):
            current_dis = dist[tour[i]][tour[i+1]] + dist[tour[j]][tour[j+1]]
            new_dis = dist[tour[i]][tour[j]] + dist[tour[i+1]][tour[j+1]]
            if new_dis < current_dis:
                #print(i,j)
                tour[i+1], tour[j] = tour[j], tour[i+1]
                tour[i+2:j] = reversed(tour[i+2:j])
    del tour[-1]
    return tour

def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    
    # 何回も最適化の操作を行った方がいいかも？
    # スライド参照
    for loop in range(5):
        new_tour = swap(tour, dist)
        new_tour = opt(new_tour,dist)
        tour = opt2(new_tour, dist)
        
    return tour


if __name__ == '__main__':
    # assert len(sys.argv) > 1
    tour = solve(read_input('input_4.csv'))
    print_tour(tour)
