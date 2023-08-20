def getDataPoint(quote):
    stock, bid_price, ask_price, price = quote
    return stock, bid_price, ask_price, (bid_price + ask_price) / 2
def getRatio(price_a, price_b):
    return price_a / price_b
