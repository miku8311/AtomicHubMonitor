import requests
import logging

class MarketSalesRequest():
    # API Server URL
    market_server = "http://wax.api.atomicassets.io/atomicmarket"

    # Services URL 
    sales_server = "/v1/sales"

    # parameters 
    sales_parameters = {'state': '1',
                        'max_assets': '',
                        'min_assets': '',
                        'show_seller_contracts' : '',
                        'contract_whitelist' : '',
                        'seller_blacklist' : '',
                        'asset_id': '',
                        'marketplace': '',
                        'maker_marketplace': '',
                        'taker_marketplace': '',
                        'symbol': '',
                        'seller': '',
                        'buyer': '',
                        
                        'min_price': '',
                        'max_price': '',

                        'min_template_mint': '',
                        'max_template_mint': '',
                        'owner': '',
                        'burned': '',
                        'collection_name': '',
                        'schema_name': '',
                        'template_id': '',
                        'is_transferable': '',
                        'is_burnable': '',
                        'match': '',
                        'collection_blacklist': '',
                        'collection_whitelist': '',
                        'ids': '',
                        'lower_bound': '',
                        'upper_bound': '',
                        'before': '',
                        'after': '',
                        'page': '',
                        'limit': '',
                        'order': '',
                        'sort': '',          
                        }


    url = ""

    # Constructors
    def __init__(self):
        logging.debug("MarketSalesRequest::__init__-> Initializing with NO input parameters") 


    def __init__(self, request_parameters : dict): 

        for key in request_parameters: 
            if key in self.sales_parameters:
                self.sales_parameters[key] = request_parameters[key]

        logging.debug("MarketSalesRequest::__init__-> Initializing with input parameters") 


    # Methods
    def add_parameter(self, parameter_key : str, value):
        """Adds parameter to sales_parameters dictionary"""

        self.sales_parameters[parameter_key] = value
        logging.debug("MarketSalesRequest::add_parameter-> key: %s value: %s" % (parameter_key, str(value))) 


    def remove_parameter(self, parameter_key : str): 
        """Removes parameter from sales_parameters dictionary. Sets key to empty string"""

        self.sales_parameters[parameter_key] = ''
        logging.debug("MarketSalesRequest::remove_parameter-> key: %s value: %s" % (parameter_key, str(self.sales_parameters[parameter_key]))) 

    def clear_parameters(self): 
        "Clears sales_parameters dictionary"

        self.sales_parameters.clear()
        logging.debug("MarketSalesRequest::clear_parameters-> Removing all parameters from dictionary") 

    def update_parameters(self, input_parameters : dict): 
        """Takes input dictionary and updates sales_parameters. 
        Will not add new keys to sales_parameters dictionary. Only update existing keys"""

        for key in input_parameters: 
            if key in self.sales_parameters:
                self.sales_parameters[key] = input_parameters[key]

    def build_url(self):
        """Creates a request URL based on parameter""" 
        self.url = self.market_server + self.sales_server # create base url

        self.url += "?"
        for key in self.sales_parameters: # Add parameters
            
            # skip blank parameters
            if self.sales_parameters[key] == '': 
                continue

            self.url += key + "=" + str(self.sales_parameters[key])
            self.url += "&"

        self.url = self.url[:-1]    # remove the last '&'
        
        logging.debug("MarketSalesRequest::build_url-> url built: %s" % self.url) 


    def make_request(self): 
        """Request Json from AtomicHub API. 
        Returns 'Response' object""" 

        logging.debug("MarketSalesRequest::make_request-> Requesting Json from web API") 

        response = requests.get(self.url)
        response.raise_for_status()
        
        return response

    def set_state(self, state : int): 
        """Add or update sale state parameter"""

        if state < 1 or state > 3: 
            logging.error("MarketSalesRequest::set_state -> ERROR: Invalid state input. Must be integer between 1 and 3")
            raise Exception

        self.request_parameters['state'] = str(state)

    def stringify_parameters(self): 
        """Prints fomatted string of request paramaters"""
        for key in self.sales_parameters: 
            print("%s : %s" % (key, self.sales_parameters[key]))
