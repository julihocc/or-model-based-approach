"""
Eiselt, H. A., & Sandblom, C. L. (2012).
Operations research: A model-based approach.
Springer Science & Business Media.
Section 5.2 Network Flow Problems.
See Fig. 5.4 Arc capacities for evacuation.
"""

from ortools.graph import pywrapgraph

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
if max_flow.Solve(0, 11) == max_flow.OPTIMAL:
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