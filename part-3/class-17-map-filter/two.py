prices=[98,198,298,398,498,598]

def addplus(price):
    return price+1

map_data=map(addplus,prices)
new_prices=list(map_data)

print(prices)
print(new_prices)
