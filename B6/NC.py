class TK:
    def __init__(self, begin, percent):
        self.begin = begin
        self.percent = percent
        self.end_month = 0
        self.end_year = 0
        self.interest_money = 0
    def total(self, add_money):
        self.percent_month = self.percent/12
        self.end_year =(self.begin*107)/100
        for i in range(0, 12):
            self.end_month = ((begin_money+add_money*(i+1)+self.interest_money) *(100+self.percent_month))/100
            self.interest_money += self.end_month - (begin_money+add_money*(i+1))
       

begin_money = float(input("Nhập số tiền ban đầu gửi vào: "))
percent = float(input("Nhập lãi suất theo năm: "))
add_money = float(input("Nhập số tiền gửi hàng tháng: "))
tk = TK(begin_money, percent)
tk.total(add_money)
print(tk.end_year)
print(tk.end_month)


        