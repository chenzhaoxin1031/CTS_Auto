import os
import time
original=0
finish = 0

def file():
    path="/home/sqa/STS/202002/android-sts/results"
    count=0
    for file in os.listdir(path):
        count +=1
    return count

def Sleep(finish):
    while True:
        count=file()
        time.sleep(2)
        if count - original != 2:
            continue
        else:
            print('pass')
            finish = 1
            break
    return finish

def run_count():
    original = file()
    # print(original)
    Sleep(finish)

if __name__ == '__main__':
    run_count()
