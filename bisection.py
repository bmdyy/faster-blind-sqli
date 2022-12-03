C = 77 # 'M' = 77

low = 0
high = 127

while low <= high:
    mid = (low + high) // 2
    print("Low = %d, High = %d, Mid = %d" % (low, high, mid))
    print("Is C between %d and %d?" % (low, mid))
    if C in range(low, mid+1): # SQL BETWEEN is inclusive
        high = mid - 1
        print("Yes => High = %d" % high)
    else:
        low = mid + 1
        print("No => Low = %d" % low)
    print()

print("Answer = Low = %d" % low)