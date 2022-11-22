import time

def func1():
    print('hello')
    func2()
    print('bye')

def func2():
    print('enter func2')
    count = 100
    while count != 0:
        time.sleep(2)
        print('-----')
        count -= 1

def main():
    func1()

if __name__ == '__main__':
    main()