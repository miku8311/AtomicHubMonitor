#! python 3

import json 
import requests 
import sys
import os
from datetime import datetime

#modules 
from modules.Utilities import Utilities


if __name__ == "__main__": 

    # parameters
    state = "1"
    assetID= '1099532053077'
    templateID = '116792'
    collectionName = 'rplanet'
    limit = '100'
    afterTime = '1578648256'
    minAssets = '20'

    # format request URL
    marketServerURL = "http://wax.api.atomicassets.io/atomicmarket"
    assetsServerURL = "https://wax.api.atomicassets.io/atomicassets"

    auctionsURL = "/v1/auctions"
    salesURL = "/v1/sales"
    marketplacesURL = "/v1/marketplaces"
    pricesURL = "/v1/prices/sales"

    assetsURL = "/v1/assets" 
    collectionsURL = "/v1/collections"


    URL = marketServerURL + salesURL 

    # Request parameters
    stateParameter = "state=" + state
    assetIDParameter = 'asset_id=' + assetID
    templateIDParameter = "template_id=" + templateID
    collectionsParameter = 'collection_name=' + collectionName
    minAssetsParameter = "min_assets=" + minAssets
    limitParameter = "limit=" + limit
    afterTimeStampParameter = 'after=' + afterTime

    URL = URL + "?" + stateParameter + "&" +  templateIDParameter 

    print("API URL: " + URL)

    # Request Json file from api
    response = requests.get(URL)
    response.raise_for_status()

    # loads json file to python data structure
    marketData = json.loads(response.text)

    # Save json to file
    timeStamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    fileName = "marketServerURL_salesURL_" + timeStamp + ".json"
    jsonFileSavePath =  os.path.join(os.getcwd(), "json")

    # Utilities.SaveJson(os.path.join(jsonFileSavePath, fileName), marketData)


    # print data
    print("Request Successful: " + str(marketData['success']))
   
    print()
    for dataIndex in range(0, len(marketData['data'])):
        print("Name: %s" % marketData['data'][dataIndex]['assets'][0]['template']['immutable_data']['name'])
        print("assetID: " + marketData['data'][dataIndex]['assets'][0]['asset_id'])
        print("templateID: " + marketData['data'][dataIndex]['assets'][0]['template']['template_id'])
        print("\tPrice: %.2f WAX" % (float(marketData['data'][dataIndex]['price']['amount']) / 100000000) )
        print("\tUpdated Time: " + str(datetime.fromtimestamp(float(marketData['data'][dataIndex]['updated_at_time'])/1000)))
        print("\tMint: %s of %s" % (marketData['data'][dataIndex]['assets'][0]['template_mint'], marketData['data'][dataIndex]['assets'][0]['template']['issued_supply']))
        print()

# float(marketData['data'][dataIndex]['updated_at_time']