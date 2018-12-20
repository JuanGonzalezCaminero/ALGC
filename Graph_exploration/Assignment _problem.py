import math

#N agents are to be assigned to N tasks, each one having to perform
#exactly one. A cost matrix is defined, which indicates the cost of having
#each agent perform each task

#We can solve this using a branch-and-bound algorithm. This algorithm keeps an upper
#bound for the solution, a lower bound, and the best value found. Among the children
#of each node, it chooses the one with the best lowest-bound value, and discards the
#ones with a lowest bound greater than the global upper bound. This selection is done
#and does not take into account the values of the children from previous nodes
#Once a solution is reached, the upper bound is updated to the value of that solution.
#The search continues until no new nodes can be generated

cost_matrix = [[11, 12, 18, 40],
               [14, 15, 13, 22],
               [11, 17, 19, 23],
               [17, 14, 20, 28]]
upper_bound = 0
#Of course, this upper and lower bounds are, respectively, greater than or equal to and
#smaller than or equal to the actual solution, since it may be that the best assignment
#for each agent is chosen this way, but chances are the value of the same task will be
#selected for multiple agents. In this upper bound case, the value chosen is the value for
#task 4 for each agent
for agent in range(len(cost_matrix)):
    upper_bound += max(cost_matrix[agent])

lower_bound = 0
for agent in range(len(cost_matrix)):
    lower_bound += min(cost_matrix[agent])

best_found = math.inf

def assignment(agent_to_assign, assigments):
    children = []
    for i in range(len(cost_matrix[0])):
        if i in assigments:
            continue





















