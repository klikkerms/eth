import requests
import json
import pandas as pd
import time

def getData(wallet_address):
    chains = ['eth', 'bsc', 'matic', 'avax']

    columns = ['Chain','Value']
    data_dict = {}

    for column in columns:
        data_dict[column] = [] 

    summ = 0
    for chain in chains:
        url = f'https://openapi.debank.com/v1/user/chain_balance?id={wallet_address}&chain_id={chain}'
        response = json.loads(requests.get(url).text)

        while ('message' in response.keys()):
            time.sleep(5)
            response = json.loads(requests.get(url).text)
        #print(response)
        chain_val = round(response['usd_value'],1)

        summ += chain_val
        data_dict['Chain'].append(chain.upper())
        data_dict['Value'].append(chain_val)
    print('sum = ', round(summ, 2))

    if summ > 0:
        #print(pd.DataFrame(data_dict))
        print(config['wallet_address'][i],'sum = ', round(summ, 2))
        print("ez money", i)
    else:
        #print(pd.DataFrame(data_dict))
        print("bad" , i)

    #print(pd.DataFrame(data_dict))

def read_config():
    with open('config.json', 'r') as f:
        config = json.load(f)

    return config

if __name__ == "__main__":
    config = read_config()

    for i in range(2048):
        wallet_address = config['wallet_address'][i]
        getData(wallet_address)
