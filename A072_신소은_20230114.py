# LeetCode
# 1154. Day of the Year

d_list = list(map(int, date.split("-"))) # yyyy, mm, dd를 int 타입으로 변환 후 list에 저장

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day_sum = sum(month[:d_list[1]-1]) + d_list[2]

# 윤년 계산 
if (d_list[0] % 4 == 0) and (d_list[0] % 100 != 0) or (d_list[0] % 400 == 0): # 윤년이고 
    if (d_list[1] > 2): # 2월보다 크면
        day_sum += 1
