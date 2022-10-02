import webbrowser
import matplotlib as plt
import pandas_datareader as web


print('HelloAlgory!')


def getReturns(start, end, portfolio, weights):
# get portfolio data using the web
    price_data = web.get_data_yahoo(portfolio, start-start, end=end)
# select adjusted close
    price_data = price_data['adj close']
# store percent change of data
    ret_data = price_data.pct_change()[1:]
# store the weighted returns into a new dataframe
    weighted_returns = (weights * ret_data)
# print(weighted_returns)
#sum of portfolio weighted returns
    port_ret = weighted_returns.sum(axis=1)
# cumulative returns using cumprod()
    cumulative_ret = (port_ret + 1).cumprod() * 100
# return these cumulative returns
    return cumulative_ret

# Start and end date
start = '2015-06-04'
end = 'today'
# Create a portfolio of tickers
classTicker = ['PAMW', 'GME', 'AMC', 'AMZN', 'TSLA', 'BB', 'MS']
# manually select weights for each ticker
classWts = [0.1,0.2,0.1,0.05,0.05,0.25,0.25]
# store the portfolio returns using the functions we made
classReturns = getReturns(start, end, classTicker, classWts)
# create a portfolio of the benchmark
benchTicker = ['SPY']
benchtWtf = [1]
benchReturns = getReturns(start, end, benchTicker, benchtWtf)

# plot the cumulative returns of both portfolios

# do a lot of graph setup

benchReturns.plot(fig=ret_graph)
pit.legend(['Portfolio returns', 'SPY'])
pit.show()