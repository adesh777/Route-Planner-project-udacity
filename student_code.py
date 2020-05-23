import math
import heapq


def euclidean_distance(start, end):
    return math.hypot(start[0] - end[0], start[1] - end[1])

def heuristic_cost_estimate(start, end):
    return euclidean_distance(start, end)

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]     
        total_path.insert(0, current)
    return total_path


def shortest_path(M, start, goal):
    print('shortest path called')    

    assert (start in M.intersections), "Start is not defined in the map."  
    assert (goal in M.intersections), "Goal is not defined in the map."    

    closedSet = set()
    openSet = set()
    pq = []
    cameFrom = {}
    gScore = {start: 0.0}
    fScore = {start: heuristic_cost_estimate(M.intersections[start], M.intersections[goal])}
    shortest_path_found = False

    heapq.heappush(pq, (fScore[start], start))
    openSet.add(start)

    while openSet:
        current = heapq.heappop(pq)[1]     
        if current == goal:
            shortest_path_found = True
            break

        openSet.remove(current)           
        closedSet.add(current)

        for neighbor in M.roads[current]:
            if neighbor in closedSet:
                continue
          
            tentative_gScore = gScore[current] + euclidean_distance(M.intersections[current], M.intersections[neighbor])          
            if neighbor in gScore and tentative_gScore >= gScore[neighbor]:
                continue
  
            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(M.intersections[neighbor], M.intersections[goal])   
            
            if neighbor not in openSet:
                heapq.heappush(pq, (fScore[neighbor], neighbor))
                openSet.add(neighbor)
                

    if not shortest_path_found:
        raise ValueError('No path found.')

    return reconstruct_path(cameFrom, goal)