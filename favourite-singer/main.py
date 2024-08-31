import numpy as np

def main():
    N = int(input())           
    singers = list(map(int, input().split()))
    singers_array = np.asarray(singers)

    unique_signers = np.unique(singers_array)
    song_count_array = np.empty(len(unique_signers), dtype=object)

    for i in range(len(unique_signers)):
        song_count_array[i] = np.count_nonzero(singers_array == unique_signers[i])

    favourite_singer = np.count_nonzero(song_count_array == np.max(song_count_array))   
    print(favourite_singer)


if __name__ == '__main__':
    main()





