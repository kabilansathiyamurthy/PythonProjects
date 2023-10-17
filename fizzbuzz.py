def fizz_buzz(n=15):
    for i in range(0, n + 1):
        if i % 3==0 and i % 5==0:
            print('FizzBuzz')
        elif i % 3 ==0:
            print('Fizz')
        elif i % 5 ==0:
            print('Buzz')
        else:
            print(i)
if __name__ == '__main__':
    fizz_buzz()
