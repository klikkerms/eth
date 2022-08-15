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
    balance = False
    for chain in chains:
        url = f'https://openapi.debank.com/v1/user/chain_balance?id={wallet_address}&chain_id={chain}'
        response = json.loads(requests.get(url).text)

        url2 = f'https://openapi.debank.com/v1/user/history_list?id={wallet_address}&chain_id={chain}'
        response2 = json.loads(requests.get(url2).text)
        #print(response2)


        if str(response2) != "{'cate_dict': {}, 'history_list': [], 'project_dict': {}, 'token_dict': {}}":
             balance = True

        while ('message' in response.keys()):
            time.sleep(5)
            response = json.loads(requests.get(url).text)
        #print(response)
        chain_val = round(response['usd_value'],6)

        summ += chain_val
        data_dict['Chain'].append(chain.upper())
        data_dict['Value'].append(chain_val)


    if summ != 0 or balance:
        #print(pd.DataFrame(data_dict))
        print(config['wallet_address'][i],'sum = ', round(summ, 1))


    #print(pd.DataFrame(data_dict))

def read_config():
    #with open('config.json', 'r') as f:
    with open('check.json', 'r') as f:
        config = json.load(f)

    return config

if __name__ == "__main__":
    config = read_config()

    for i in range(2048):
        wallet_address = config['wallet_address'][i]
        getData(wallet_address)
        print("          ")