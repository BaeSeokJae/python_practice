# print('hello, world')
# 변수는 타입 없이 그냥 선언하는 방식인것 같음.
identity = '지구인'
number_of_legs = 4
# console 창에 띄울때는 자바처럼 print로 출력할 수 있는것 같음
# print('안녕 나는', identity, '이야 나이는 ', number_of_legs, '살 이야')

# /** */ 와 같은 주석 처리 방식은
"""
이런식으로 따옴표 3개로 처리함
"""
my_age = 25
# 덧셈 +
my_next_age = my_age + 1
# 뺄셈 -
multiply = 9 * 9
# 나누기 /
divide = 30 / 5
# 거듭제곱
power = 2 ** 10
# 나머지
remainder = 15 % 4
# print(my_next_age, multiply, divide, power, remainder)

my_name = 'Python'

text = '2015' + '1991'
# print(text)

people = 3
apple = 20

# if people < apple / 5:
#     print('사과 파티')

# if apple % people > 0:
#     print('사과수 안맞음')

# if people > apple:
#     print('사람 많음')

# if True:
#     print('1. 블럭이 속한 코드')

#     if False:
#         print('2. 한줄더')

#     if True:
#         print('3. 또 한줄더')

#     print('4. 블럭의 끝 코드')

# print('5. 블럭 끝')

scissor = '가위'
rock = '바위'
paper = '보'

win = '이김'
draw = '비김'
lose = '짐'

mine = '가위'
yours = '바위'

if scissor == yours:
    result = draw
elif scissor == mine:
    result = win

# print(result)


# def test():
#     print('함수에요')


# test()


def print_round(number):
    # round -> 반올림하는 함수
    rounded = round(number)
    print(rounded)


print_round(3.3)
