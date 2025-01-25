from news_call import get_headlines
from calculate_porcentaje import calculate_porcentage
from stock_price import get_stock_price
from days_before import day_count_date


NEWS_API_KEY = '671121ad496547308763249441f565e9'
STOCK_INFO_API = "RAEJ1JDBDRNWQ7QR"
#Test at the end! this has a 25 uses limit per day


days = day_count_date()
#print(days[0])
price = get_stock_price(days[0], days[1])
#print(price[1])
previous_val = price[0]
current_val = price[1]


if previous_val > current_val:
    print(f"{calculate_porcentage(previous_val, current_val)}% lose")
    get_headlines(3)
elif previous_val < current_val:
    print(f"{calculate_porcentage(previous_val, current_val)}% profit")
    get_headlines(3)
else:
    print("no movements today!")




