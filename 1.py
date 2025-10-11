squares = [x ** 2 for x in range(10)]
print(squares)

num = list(range(1, 21))
ch_num = [x for x in num if x % 2 == 0]
print(ch_num)

words = ['python', 'java', 'c++', 'Rust', 'go']
spisok = [x.upper() for x in words if len(x)>3]
print(spisok)
