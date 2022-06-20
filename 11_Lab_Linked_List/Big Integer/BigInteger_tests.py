from big_integer import BigInteger


for i in [12, -76, 234, -2493939]:
    for j in [59, 2, -15, -144051]:
        x = BigInteger(str(i))
        y = BigInteger(str(j))
        assert(i+j == int(str(x+y))), (i,j, i+j, x+y)

for i in [-31, 12, -100001, 9099090]:
    for j in [-1, 0, 2, -10090, 9]:
        x = BigInteger(str(i))
        y = BigInteger(str(j))
        assert(i-j == int(str(x-y))), (i,j, i-j, x-y)


for i in[-31, 1, 234, 623634]:
    for j in [-1,1, 0, 2, 15, 515215]:
        x = BigInteger(str(i))
        y = BigInteger(str(j))
        assert(i*j == int(str(x*y))), (i,j, i*j, x*y)


for i in[ 3,-3, -5, 5, 1345, -1345, 16, -16]:
    for j in [-2,2, 12,-4,4 -12, 1, -1]:
        x = BigInteger(str(i))
        y = BigInteger(str(j))
        assert(i//j == int(str(x//y))), (i,j, i//j, x//y)

for i in[ 3,-3, -5, 5, 1345, -1345, 16, -16]:
    for j in [-3,3, 12, -12]:
        x = BigInteger(str(i))
        y = BigInteger(str(j))
        assert(i%j == int(str(x%y))), (i,j, i%j, x%y)


for i in[ 0, 1, -3, 11, 25]:
    for j in [0,1, 2, 5, 12, 31]:
        x = BigInteger(str(i))
        y = BigInteger(str(j))
        assert(i**j == int(str(x**y))), (i,j, i**j, x**y)


for i in[ 3,-3, -5, 5, 1345, -1345, 16, -16]:
    for j in [-4,4]:
        x = BigInteger(str(i))
        y = BigInteger(str(j))
        assert(list(divmod(i,j)) == [int(str(n)) for n in x.big_divmod(y)]),\
                          (i,j, divmod(i,j), x.big_divmod(y))



for i in [1, 2, 6, 11, 17, 63, 98]:
    x = BigInteger(str(i))
    assert(x.bit_big_integer() == BigInteger(str(bin(i)[2:]))), x
    assert(x.bit_big_integer().bin_into_integer()==x), x


for i in [1, 2, 6, 11, 17, 63, 98]:
    x = BigInteger(str(i))
    assert((x << BigInteger('1')) << BigInteger('1') == x << BigInteger('2')), x
    assert((x << BigInteger('2')) << BigInteger('3') == x << BigInteger('5')), x

for i in [6, 11, 17, 63, 98]:
    x = BigInteger(str(i))
    assert((x>>BigInteger('1')) >> BigInteger('1') == x>>BigInteger('2')), x
    assert((x<<BigInteger('11')) >> BigInteger('11') == x), x


for i in [2,5, 15, 63]:
    x = BigInteger(str(i))
    for j in [1, 2, 12, 17, 56]:
        y = BigInteger(str(j))
        assert (int(str(x&y)) == i&j), ((i, j), [x&y], i&j)

for i in [2,5, 15, 63]:
    x = BigInteger(str(i))
    for j in [1, 2, 12, 17, 56]:
        y = BigInteger(str(j))
        assert (int(str(x|y)) == i|j), ((i, j), [x|y], i|j)


for i in [2,5, 15, 63]:
    x = BigInteger(str(i))
    for j in [1, 2, 12, 17, 56]:
        y = BigInteger(str(j))
        assert (int(str(x^y)) == i^j), ((i, j), [x^y], i^j)

