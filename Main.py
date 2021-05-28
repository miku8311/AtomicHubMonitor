#! python 3 

import logging
from datetime import datetime
import os
import time

# package modules
from AtomicHubMonitor.Utilities import Utilities
from AtomicHubMonitor.MarketSalesRequest import MarketSalesRequest
from AtomicHubMonitor.MarketMonitor import MarketMonitor
from AtomicHubMonitor.MonitoredObject import MonitoredObject
from AtomicHubMonitor.Alerts import Alerts

#Sets up logging
logging.basicConfig(level=logging.DEBUG, format='\t%(levelname)s:%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.ERROR) # uncomment to block debug logging.debug messages
logging.disable(logging.DEBUG) # uncomment to block debug logging.debug messages
logging.disable(logging.INFO) # uncomment to block debug logging.info messages and below

waxon = MonitoredObject({'asset_id' : '', 
                        'template_id' : '',     
                        'owner': '', 
                        'symbol': '', 
                        'seller': '', 
                        'collection_name': '', 
                        'schema_name': 'lands',
                        }, 
                        min_price= 8000 * 100000000, 
                        )

monitored_objects = [waxon]

if __name__ == "__main__":

    alerts = Alerts()

    monitor = MarketMonitor(monitored_objects)
    monitor.set_request_interval(5.0)

    # Main Loop
    while True:
        print(datetime.now())
        print("---------------------")
        results = monitor.monitor_loop(search_min_price=True, search_max_price=False)

        for result in results['under_valued_objects']: 
            print()
            print("Name: %s" % result['asset']['template']['immutable_data']['name'])
            print("Owner: %s" % result['asset']['owner'])
            print("Schema: %s" % result['asset']['schema']['schema_name'])
            print("Template id: %s" % result['asset']['template']['template_id'])
            print("Asset id: %s" % result['asset']['asset_id'])
            print("\tPrice: %s" % str(float(result['price']['amount'])/100000000))

        print()
        # pause before making next request to API
        time.sleep(monitor.request_interval)
