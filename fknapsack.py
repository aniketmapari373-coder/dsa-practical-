def fractional_knapsack(weights, profits, capacity):
    n = len(weights)
    ratio = [(profits[i]/weights[i], weights[i], profits[i]) for i in range(n)]
    ratio.sort(reverse=True)
    max_profit = 0
    for r, w, p in ratio:
        if capacity == 0:
            break
        if w <= capacity:
            max_profit += p
            capacity -= w
        else:
            max_profit += p * (capacity / w)
            break
    return max_profit
# ---- Main Code ----
weights = []
profits = []
n = int(input("Enter number of parcels: "))
for i in range(n):
    wt = float(input(f"Enter weight of parcel {i+1}: "))
    pf = float(input(f"Enter profit of parcel {i+1}: "))
    weights.append(wt)
    profits.append(pf)
capacity = float(input("Enter capacity of truck: "))
max_profit = fractional_knapsack(weights, profits, capacity)
print("\nMaximum Profit:", max_profit)
