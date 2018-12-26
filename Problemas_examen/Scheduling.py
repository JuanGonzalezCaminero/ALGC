#We want to maximize the profit, jobs grant us profit if they are executed
#no later than their deadline (That is, the job can start, at most, in the
#moment the deadline ends). Jobs take 1 time unit to complete
tasks = [(20, 3), (50, 3), (50, 3), (50, 2), (40, 1), (30, 1), (10, 1)]

def scheduling(tasks):

