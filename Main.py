#! python 3 
import logging
from datetime import datetime
import os

# modules 
from modules.Utilities import Utilities
from modules.MarketSalesRequest import MarketSalesRequest
from modules.MarketMonitor import MarketMonitor

#Sets up logging
logging.basicConfig(level=logging.DEBUG, format='\t%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.ERROR) # uncomment to block debug logging.debug messages
logging.disable(logging.DEBUG) # uncomment to block debug logging.debug messages
#logging.disable(logging.INFO) # uncomment to block debug logging.info messages and below

request_parameters = {'state': '1',
                    'asset_id': '',
                    'symbol': '',
                    'seller': '',
                    'min_price': '',
                    'max_price': '',
                    'collection_name': 'hallowscards',
                    'schema_name': '',
                    'template_id': '',
                    'ids' : '',
                    }

if __name__ == "__main__":

    # Build API
    marketRequest = MarketSalesRequest(request_parameters)
    # print(marketRequest.stringify_parameters())
    # print()

    # Make API Request
    marketRequest.build_url()
    # print(marketRequest.url)
    # print()

    # load json file 
    response = marketRequest.make_request()
    marketData = Utilities.loads_json(response.text)

    # Save json to file
    timeStamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    fileName = "marketServerURL_salesURL_" + timeStamp + ".json"
    jsonFileSavePath =  os.path.join(os.getcwd(), "json//marketData")

    Utilities.save_json_file(os.path.join(jsonFileSavePath, fileName), marketData)

    print()
    for dataIndex in range(0, len(marketData['data'])):
        print("Name: %s" % marketData['data'][dataIndex]['assets'][0]['template']['immutable_data']['name'])
        print("assetID: " + marketData['data'][dataIndex]['assets'][0]['asset_id'])
        print("templateID: " + marketData['data'][dataIndex]['assets'][0]['template']['template_id'])
        print("\tPrice: %.2f WAX" % (float(marketData['data'][dataIndex]['price']['amount']) / 100000000) )
        print("\tMint: %s of %s" % (marketData['data'][dataIndex]['assets'][0]['template_mint'], marketData['data'][dataIndex]['assets'][0]['template']['issued_supply']))
        print()
