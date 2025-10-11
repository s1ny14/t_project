#1
squares = [x ** 2 for x in range(10)]
print(squares)

#2
num = list(range(1, 21))
ch_num = [x for x in num if x % 2 == 0]
print(ch_num)

#3
words = ['python', 'java', 'c++', 'Rust', 'go']
spisok = [x.upper() for x in words if len(x)>3]
print(spisok)

#4
class Countdown:
    def __init__(self, n):
        self.n = n + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.n -= 1
        if self.n < 1:
            raise StopIteration
        return self.n
for x in Countdown(5):
    print(x)
