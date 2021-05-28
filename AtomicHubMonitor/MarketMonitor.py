import logging

# package modules 
from AtomicHubMonitor.Utilities import Utilities
from AtomicHubMonitor.MarketSalesRequest import MarketSalesRequest
from AtomicHubMonitor.MonitoredObject import MonitoredObject

class MarketMonitor(): 
    """Provided a list of MonitorObject monitors the Atomic Hub market with given parameters 
    and returns list of assets above and below provided thresholds."""

    request_interval = 100.0;

    monitored_objects = []    

    def __init__(self):
        logging.debug("MarketMonitor::__intit__ -> Initializing with no monitored objects")


    def __init__(self, monitored_objects : list):
        logging.debug("MarketMonitor::__intit__ -> Initializing with monitored objects")

        for obj in monitored_objects: 
            
            # Check is obj is of type MonitorObject
            if isinstance(obj, MonitoredObject) == False: 
                logging.error("MarketMonitor::__intit__ -> ERROR: monitored_objects must be a list of MonitoredObject")
                raise Exception

            self.monitored_objects.append(obj)  # add object to list

    def add_monitored_object(self, monitored_object: MonitoredObject): 
        """ """ 
        self.monitored_objects.append(monitored_object)

    def remove_monitored_object(self, monitored_object: MonitoredObject): 
        """ """ 
        pass

    def set_request_interval(self, interval : float): 
        """ """ 

        self.request_interval = interval

    def search_assets_below_min(self, marketData, min_price): 
        """ """ 

        objects_below_min = []

        for dataIndex in range(0, len(marketData['data'])):
            if int(marketData['data'][dataIndex]['listing_price']) < min_price: 
                asset_object = {
                                'price' : marketData['data'][dataIndex]['price'],
                                'asset' : marketData['data'][dataIndex]['assets'][0],
                                }

                objects_below_min.append(asset_object)

        return objects_below_min

    def search_assets_above_max(self, marketData, max_price): 
        """ """

        objects_above_max = []

        for dataIndex in range(0, len(marketData['data'])):
            if int(marketData['data'][dataIndex]['listing_price']) > max_price: 
                asset_object = {
                                'price' : marketData['data'][dataIndex]['price'],
                                'asset' : marketData['data'][dataIndex]['assets'][0],
                                }

                objects_above_max.append(asset_object)

        return objects_above_max

    def monitor_loop(self, search_min_price : bool = True, search_max_price : bool = True): 
        """ """ 

        logging.debug("MarketMonitor::monitor_loop -> Making API request")
        
        for obj in self.monitored_objects: 

            # Build request
            marketRequest = MarketSalesRequest(obj.attributes['data'])
            logging.debug("MarketMonitor::monitor_loop -> Request Parameters: %s" % marketRequest.sales_parameters)

            # Make request
            response = marketRequest.make_request()
            marketData = Utilities.loads_json(response.text)


            #
            objects_below_min = []
            if search_min_price == True: 
                objects_below_min = self.search_assets_below_min(marketData, obj.attributes['min_price'])

            objects_above_max = []
            if search_max_price == True: 
                objects_above_max = self.search_assets_above_max(marketData, obj.attributes['max_price'])
           
            results = {'under_valued_objects' : objects_below_min, 
                    'over_valued_objects' : objects_above_max
                    }
            logging.info("MarketMonitor::monitor_loop -> under value results: %s\n" % results['under_valued_objects'])
            logging.info("MarketMonitor::monitor_loop -> over value results: %s\n" % results['over_valued_objects'])

            return results 



