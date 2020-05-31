def fib_seq(sqlen):
    fib_seed = [0,1]
    if sqlen == 1:
        print(fib_seed[0])
    elif sqlen == 2:
        print(fib_seed)
    else:
        for i in range(2,sqlen):
            fib_seed.append(fib_seed[i-2] + fib_seed[i-1])
        print(fib_seed)
        

fib_seq(1000)
