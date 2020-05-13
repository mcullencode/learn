import requests
binsize = '1h'
symbol = 'XBT'
count = '750'
reverse = True

data = []
for i in range(0, 9, 1):
    x = requests.get(f'https://www.bitmex.com/api/v1/trade/bucketed?binSize={binsize}&symbol={symbol}&count={count}&reverse={reverse}').json()
    data.append(x)
    x = '-' * 100
    print(f'success{i}')
    print(x)
    print(data[i])
    print('\n')

