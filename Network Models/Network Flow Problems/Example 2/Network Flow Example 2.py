"""
Eiselt, H. A., & Sandblom, C. L. (2012).
Operations research: A model-based approach.
Springer Science & Business Media.
Section 5.2 Network Flow Problems.
See Fig. 5.5 Network for maximal flow example.
"""

from ortools.graph import pywrapgraph
import graphviz as gv
import matplotlib.pyplot as plt
import matplotlib.image as img

capacities = {
    (0,1): 5, (0,2): 8,
    (1,2): 2, (1,3): 2, (1,4): 4,
    (2,3): 3, (2,4): 3,
    (3,4): 5
}

f = gv.Digraph(name= "example_2", format = "png")
for k, v in capacities.items():
    f.edge(str(k[0]), str(k[1]), label=str(v))
f.render()
im = img.imread("example_2.gv.png", )
plt.imshow(im)
plt.axis('off')
plt.show()

# Instantiate a SimpleMaxFlow solver.
max_flow = pywrapgraph.SimpleMaxFlow()
# Add each arc.
for index, capacity in capacities.items():
    a, b = index
    max_flow.AddArcWithCapacity(a, b, capacity)

# Find the maximum flow between node 0 and node 4.
if max_flow.Solve(0, 4) == max_flow.OPTIMAL:
    print('Max flow:', max_flow.OptimalFlow())
    print('')
    print('  Arc    Flow / Capacity')
    for i in range(max_flow.NumArcs()):
      print('%1s -> %1s   %3s  / %3s' % (
          max_flow.Tail(i),
          max_flow.Head(i),
          max_flow.Flow(i),
          max_flow.Capacity(i)))
    print('Source side min-cut:', max_flow.GetSourceSideMinCut())
    print('Sink side min-cut:', max_flow.GetSinkSideMinCut())
else:
    print('There was an issue with the max flow input.')