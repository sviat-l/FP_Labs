def superDigit(n, k):
    return int(n) if k==0 else superDigit(  str(sum(int(x) for x in n)) ,k-1)

print(superDigit('9875', 3))