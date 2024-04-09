def slice_list(a, b):
    args = sorted([a, b])
    primes = []
    for i in range(args[0], args[1]):
        for a in range(2, i):
            if i % a == 0:
                break
        else:
            primes.append(i)
    return primes

print(slice_list(20,8))
