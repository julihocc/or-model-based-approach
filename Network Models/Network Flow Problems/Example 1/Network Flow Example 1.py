"""
Eiselt, H. A., & Sandblom, C. L. (2012).
Operations research: A model-based approach.
Springer Science & Business Media.
Section 5.2 Network Flow Problems.
See Fig. 5.4 Arc capacities for evacuation.
"""

from ortools.graph import pywrapgraph
import graphviz as gv
import matplotlib.pyplot as plt
import matplotlib.image as img

capacities = {
    (0, 1): 60, (0, 5): 60,
    (1, 2): 60, (1, 4): 40,
    (2, 3): 30,
    (3, 4): 40, (3, 6):30,
    (4, 5): 40,
    (5, 8): 30,
    (6, 7): 40, (6, 11): 60,
    (7, 8): 40, (7, 9): 40,
    (8, 10): 60,
    (9, 10): 30, (9, 11): 60
}

f = gv.Graph(name= "example_1", format = "png")
for k, v in capacities.items():
    f.edge(str(k[0]), str(k[1]), label=str(v))
f.view()

im = img.imread("example_1.gv.png", )
plt.imshow(im)
plt.axis('off')
plt.show()

extra_capacities = {}

for index, capacity in capacities.items():
    a, b = index
    extra_capacities[(b,a)] = capacity
    
capacities.update(extra_capacities)

# Instantiate a SimpleMaxFlow solver.
max_flow = pywrapgraph.SimpleMaxFlow()
# Add each arc.
for index, capacity in capacities.items():
    a, b = index
    max_flow.AddArcWithCapacity(a, b, capacity)

# Find the maximum flow between node 0 and node 4.

solution = {}

if max_flow.Solve(0, 11) == max_flow.OPTIMAL:
    print('Max flow:', max_flow.OptimalFlow())
    for i in range(max_flow.NumArcs()):
        tail = max_flow.Tail(i)
        head = max_flow.Head(i)
        flow = max_flow.Flow(i)
        capacity = max_flow.Capacity(i)
        solution[(tail, head)] = (flow, capacity)
    print('Source side min-cut:', max_flow.GetSourceSideMinCut())
    print('Sink side min-cut:', max_flow.GetSinkSideMinCut())
else:
    print('There was an issue with the max flow input.')

print(solution)

f = gv.Graph(name= "solution_1", format = "png")
for k, v in solution.items():
    tail, head = k
    if tail < head :
        flow, capacity = v
        f.edge(str(tail), str(head), label="{}/{}".format(flow, capacity))
f.view()

im = img.imread("solution_1.gv.png", )
plt.imshow(im)
plt.axis('off')
plt.show()