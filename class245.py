import json 
import requests
from web3 import Web3

API_url = 'https://mainnet.infura.io/v3/0e57d739b12943e9b5fc42438625c61b'
web3 = Web3(Web3.HTTPProvider(API_url))

req_ethgas_data=requests.get('https://ethgasstation.info/json/ethgasAPI.json')
trans_info=json.loads(req_ethgas_data.content)

print('safelow',trans_info['safeLow'])
print('average',trans_info['average'])
print('fast',trans_info['fast'])
print('fastest',trans_info['fastest'])
print('Block number:',trans_info['blockNum'])

gas_price = web3.eth.gas_price
gas_price_ether=gas_price/10**18
print("gas price in ether:", gas_price_ether)

gas_price_dollar=gas_price_ether*1912
print("gas price in dollar:", gas_price_dollar)


Block_data = web3.eth.getBlock(17631014)
latest_transaction=Block_data["transactions"][-1].hex()
print('transaction hash data:', latest_transaction)
transaction_detail = web3.eth.get_transaction(latest_transaction)
gas_estimate=web3.eth.estimateGas({'to': transaction_detail['to'],"from":transaction_detail['from']})
print("gas used by this transaction is:", gas_estimate)
print("gas limit is:", transaction_detail['gas'])

gas_price_pounds=gas_price_ether*1503
print("gas price in pounds:", gas_price_pounds)

gas_price_rupies=gas_price_ether*157416
print("gas price in rupies:", gas_price_rupies)