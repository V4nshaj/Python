prices = {'iphone': 500, 'ipad': 400}
new_prices = {'iphone': 600, 'ipad': 1500}

prices.update(new_prices)
print(prices)
a= prices.pop('ipad')
print(prices)