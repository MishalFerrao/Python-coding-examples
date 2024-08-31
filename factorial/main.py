

def main():
    N = int(input())    # Reading input from STDIN

    factorial = 1
    while (N>0):
        factorial = factorial * N
        N -= 1

    print('%d' % factorial)


if __name__ == '__main__':
    main()


