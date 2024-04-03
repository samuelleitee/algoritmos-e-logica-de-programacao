popA = 80000
popB = 200000
count = 0

while popA < popB:
    popA = popA + 0.03 * popA
    popB = popB + 0.015 * popB
    count += 1

print(count)
