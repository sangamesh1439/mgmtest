import sys

for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        exit(0)
    spendings = []
    totalSpendingInTrip = 0
    for i in range(0, n):
        s = float(sys.stdin.readline().strip())
        totalSpendingInTrip = round(totalSpendingInTrip + s, 2)
        spendings.append(s)
    
    diffExchange = 0
    perHeadSpending = round(totalSpendingInTrip // len(spendings), 2)
    for s in spendings:
        exchange = perHeadSpending - s
        if exchange > 0:
            diffExchange =  round(diffExchange + exchange ,2)

    print("$%.2f"%diffExchange)
exit(0)
