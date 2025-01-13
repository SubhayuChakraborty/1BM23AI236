def twoStacks(maxSum, a, b):
    sum = 0
    count = 0
    i = 0
    j = 0

    
    while i < len(a) and sum + a[i] <= maxSum:
        sum += a[i]
        i += 1
    count = i

    
    while j < len(b) and i >= 0:
        sum += b[j]
        j += 1

        
        while sum > maxSum and i > 0:
            i -= 1
            sum -= a[i]

        
        if sum <= maxSum:
            count = max(count, i + j)

    return count


games = int(input())  
results = []

for _ in range(games):
    n, m, maxSum = map(int, input().split())  
    a = list(map(int, input().split()))  
    b = list(map(int, input().split()))  

    results.append(twoStacks(maxSum, a, b))


for result in results:
    print(result)
