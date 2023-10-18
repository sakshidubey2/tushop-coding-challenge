def jobScheduling():
    n = int(input("Enter the number of Jobs: "))
    jobs = []
    start_time_arr = []
    end_time_arr = []
    profit_arr = []
    for _ in range(n):
        start_time = int(input("Enter job start time (HHMM): "))
        end_time = int(input("Enter job end time (HHMM): "))
        profit = int(input("Enter earnings: "))
        start_time_arr.append(start_time)
        end_time_arr.append(end_time)
        profit_arr.append(profit)

    jobs = sorted(zip(end_time_arr, start_time_arr, profit_arr))  
    n = len(jobs)
    dp = [0] * n
    prev = [-1] * n

    for i in range(n):
        dp[i] = jobs[i][2]  

    for i in range(1, n):
        for j in range(i):
            if jobs[i][1] >= jobs[j][0]:  
                if dp[j] + jobs[i][2] > dp[i]:
                    dp[i] = dp[j] + jobs[i][2]
                    prev[i] = j
                    print("dp", dp)

    max_profit = max(dp)
    max_profit_index = dp.index(max_profit)
    
    selected_intervals = []

    while max_profit_index >= 0:
        selected_intervals.append((jobs[max_profit_index][1], jobs[max_profit_index][0]))
        max_profit_index = prev[max_profit_index]

    selected_intervals.reverse()

    sum_profit = sum(profit_arr)
    jobs_length = len(jobs)

    return jobs_length - len(selected_intervals), sum_profit - max_profit,

print(jobScheduling())
