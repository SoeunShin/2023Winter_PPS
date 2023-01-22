# LeetCode
# 1185. Day of the Week

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import datetime

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = days[datetime.date(year, month, day).weekday()]  

        return day
    
# weekday() -> {0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일}
