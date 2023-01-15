# Programmers
# 가장 큰 수

def solution(numbers):
    # int list -> str list로 변환
    numbers = list(map(str, numbers)) 
    
    # 각 숫자에 3을 곱하여 큰 순서대로 정렬
    # str 타입이므로 3을 곱하면 '6' -> '666'이 됨
    # str 타입이므로 '111'보다 '22'가 더 큼
    numbers.sort(key=lambda x: x * 3, reverse=True) # key에 함수를 넘겨주면 해당 함수의 리턴을 비교하여 sort
    return str(int(''.join(numbers))) # '0011'과 같은 수를 '11'로 바꾸기 위해 int -> str으로 변환 
