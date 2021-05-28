import math 
import logging

class MonitoredObject(): 
    """Contains data about an object on the Atomic Hub market that one would like to monitor.
     Contains data to pass to API as query parameters"""
    
    attributes = { 'data' : {'asset_id' : '', 
                            'template_id' : '',     
                            'owner': '', 
                            'symbol': '', 
                            'seller': '', 
                            'collection_name': '', 
                            'schema_name': '',
                            }, 
                    'min_price' : -math.inf, 
                    'max_price' : math.inf,
                }
    
    def __init__(self):
        logging.debug("MonitoredObject::__init__ -> attributes : %s" % (self.attributes))

    def __init__(self, input_data : dict, min_price : float = 0.0, max_price : float = 0.0):

        for key in input_data: 
            if key in self.attributes['data']:
                self.attributes['data'][key] = input_data[key] 


        self.attributes['min_price'] = min_price
        self.attributes['max_price'] = max_price

        logging.debug("MonitoredObject::__init__ -> attributes : %s" % (self.attributes))


    def set_min_price(self, price : float): 
        """ """
        
        if price < 0 : 
            logging.error("MonitoredObject::set_min_price -> ERROR: Price min must be a non negative floating point value")
            raise Exception
        if price >= self.attributes['max_price']: 
            logging.error("MonitoredObject::set_min_price -> ERROR: Min price must be less than max price")
            raise Exception

        self.attributes['min_price'] = price

    def set_max_price(self, price: float):
        """ """ 
        if price <= self.attributes['min_price']: 
            logging.error("MonitoredObject::set_max_price -> ERROR: Max price must be greater tahn min price")
            raise Exception

    def set_attributes_data(self, data : dict): 
        """ """

        for key in data: 
            if key in self.attributes['data']:
                self.attributes[key] = data[key]
