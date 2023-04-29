def faktoryel(n, fakt=1):
    for i in range(1, n + 1):
        fakt *= i

    return  fakt

print(f"100 ün faktoryeli : {faktoryel(100)}")

