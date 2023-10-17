def print_formatted(upto: int):
    w = upto.bit_length()
    for num in range(1, upto + 1):
        print(f"{num:>{w}d} {num:>{w}o} {num:>{w}X} {num:>{w}b}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
