def main():
    t = int(input()) 
    value_1 = [0] * t
    value_2 = [] * t
    
    for i in range(0, int(t)): 
        value_1[i] = (input().split('\n')[0])

    for i in range(0,int(t)):
        n = int(value_1[i].split(' ')[0])
        k = int(value_1[i].split(' ')[1])
        """total_count = 0
        for i in range(0,int(n)+1):
            print(DecimalToBasek(i,int(k)))
        print(total_count)"""

    


def DecimalToBasek(num,k):
    count = 0
    while num >= k:
        q = (num // k)
        r = (num % k)
        num = q
        if num < k:
            count += 2
            break
        else:
            count += 1
    print(count)
    




if __name__ == '__main__':
    main()