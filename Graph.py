import numpy as num
import networkx as net
import matplotlib.pyplot as plot
import queue as q

Graph = net.Graph()



Graph.add_edge(1, 3)
Graph.add_edge(1, 2)
Graph.add_edge(2, 4)
Graph.add_edge(2, 6)
Graph.add_edge(3, 4)
Graph.add_edge(4, 5)
Graph.add_edge(5, 6)
Graph.add_edge(1, 7)
Graph.add_edge(8, 6)
Graph.add_edge(4, 6)
Graph.add_edge(7, 9)
Graph.add_edge(3, 8)
Graph.add_edge(6, 9)
Graph.add_node(10)


pos = {1: (-0.5, 0.2), 2: (0, 0.1), 3: (-1, 0.7), 4: (2, 0.3), 5: (4, 0.4), 6: (5, 0.2), 7: (5.5, 0.55), 8: (7.6, 0.7),
       9: (8, 0.2), 10: (9, 0.3)}

options = {
    "font_size": 15,
    "node_size": 600,
    "node_color": "blue",
    "edgecolors": "black",
    "linewidths": 4,
    "width": 3,
}

net.draw_networkx(Graph, pos, **options)

ax = plot.gca()
ax.margins(0.20)
plot.axis("off")
plot.show()


startNode = 4
endNode = 7

queue = list()
queue.append(startNode)

Rqueue = list()
Rqueue.append(endNode)

visited = num.full(len(Graph.nodes),False,dtype = bool)
Rvisited = num.full(len(Graph.nodes),False,dtype = bool)


visited[startNode-1] = True
Rvisited[endNode-1] = True


previous = num.full(len(Graph.nodes),None)
Rprevious = num.full(len(Graph.nodes),None)

previous[startNode-1] = -1
Rprevious[endNode-1] = -1


def search():

    while queue and Rqueue:

        print(queue)
        print(Rqueue)
        print("-------------------")
        print(previous)
        print(Rprevious)
        print("**********************")
        print(visited)
        print(Rvisited)
        print("======================")

        current = queue.pop(0)
        neighbors = list(Graph.adj[current])
        print(neighbors)
        for x in range(len(neighbors)):
            print(x)
            node = neighbors[x]
            if not visited[x]:
                queue.append(node)
                visited[node-1] = True
                previous[node-1] = current

        Rcurrent = Rqueue.pop(0)
        Rneighbors = list(Graph.adj[Rcurrent])
        print(Rneighbors)
        for x in range(len(Rneighbors)):
            print(x)
            Rnode = Rneighbors[x]
            if not Rvisited[x]:
                Rqueue.append(Rnode)
                Rvisited[Rnode-1] = True
                Rprevious[Rnode-1] = Rcurrent

        inter = check()

        if inter != -1:
            print(f"Intersection between {startNode} and {endNode}")
            print("Intersected at " + str(inter))
            printFinal(inter)
            exit(0)


def printFinal(intersec):

    final = []
    final.append(intersec)
    print(intersec)
    q = intersec
    while q is not startNode:
        final.append(previous[q])
        q = previous[q]

    print(final)
    final.reverse()
    print(final)
    q = intersec

    while q is not endNode:
        final.append(Rprevious[q])
        q = Rprevious[q]

    final = list(map(str, final))
    print(final)


def check():
    for x in range(len(Graph.nodes)):
        if (visited[x] and Rvisited[x]):

            return x
    return -1


search()

print("Path not found in Graph")


#i = len()