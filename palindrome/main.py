def main():
    input_string = input() 
    k = len(input_string)
    reversed_string_list = [None] * k

    small_letters_flag = True
    palindrome_flag = True
    length_flag = True

    if (len(input_string) <= 100) and (len(input_string) >= 1):
        for i in range(len(input_string)):
            if (ord(input_string[i]) <= 122) and (ord(input_string[i]) >= 97):
                reversed_string_list[k - i - 1] = input_string[i]
            else:
                small_letters_flag = False
                break

        for i in range (len(input_string)):
            if reversed_string_list[i] == input_string[i]:
                pass
            else:
                palindrome_flag = False
                break
    else:
        length_flag = False

    if (palindrome_flag == True) and (small_letters_flag == True) and (length_flag == True):
        print("YES")
    else:
        print("NO")








if __name__ == '__main__':
    main()