# Given a set of jobs to be executed, each with a value and a deadline, and the value
# is obtained if the job is completed before the deadline, find the optimal executing order

# Only one job can be executes per time unit, a set of jobs is said to be feasible if there is
# an execution order such that all of them are executed and all meet their deadlines

# The algorithm chooses, in each step, the job with the maximum value, provided that, by adding it
# to the other selected jobs, the set remains feasible.
# To know whether a set of jobs is feasible, we just need to check if, executing them in order of
# increasing deadline, all meet their deadlines

#A job contains: (value, deadline)
job_list = [(20, 3), (50, 3), (50, 3), (50, 2), (40, 1), (30, 1), (10, 1)]
#Sort the jobs in order of decreasing profit
job_list = list(reversed(sorted(job_list, key = lambda a: a[0])))
selected_jobs = []

for job in job_list:
    selected_jobs.append(job_list.pop(0))
    #sort the result in order of ascending deadline
    sorted_selected_jobs = sorted(selected_jobs, key = lambda a: a[1])
    #Check whether the set of jobs is still feasible
    for i in range(len(sorted_selected_jobs)):
        if selected_jobs[i][1] < (i + 1):
            #If a job is scheduled after its deadline, remove the last
            #introduced job and never consider it again
            selected_jobs.pop(-1)
            continue

print(selected_jobs)