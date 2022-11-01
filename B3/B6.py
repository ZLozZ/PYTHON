def calculate(info, price):
    if info["value_electric"] >= 0 and info["value_electric"] <= 50:
        total = info["value_electric"] * price[0]

    if info["value_electric"] >= 51 and info["value_electric"] <= 100:
        total = (50*price[0]) + (info["value_electric"] - 50)* price[1]

    if info["value_electric"] >= 101 and info["value_electric"] <= 200:
        total = (50*price[0]) + (50* price[1]) + ((info["value_electric"] - 100)* price[2])

    if info["value_electric"] >= 201 and info["value_electric"] <= 300:
        total = (50*price[0]) + (50* price[1])+ (100* price[2]) + ((info["value_electric"] - 200)* price[3])

    if info["value_electric"] >= 301 and info["value_electric"] <= 400:
        total = (50*price[0]) + (50* price[1]) + (100* price[2]) + (100 * price[3]) + ((info["value_electric"] - 300)* price[4])
    
    if info["value_electric"] >= 401:
        total = (50*price[0]) + (50* price[1]) + (100* price[2]) + (100 * price[3]) + (100* price[4]) + ((info["value_electric"] - 400)*price[5])

    print("Số tiền điện hộ {} là {}đ".format(info["name"], round(total, 2)))

price = (1678, 1734, 2014, 2536, 2834, 2927)
info = {"name":"Nguyen Van B", "DC":"Go Vap", "value_electric": 410}
calculate(info, price)