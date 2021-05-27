class Asset():
    asset_parameters = {'owner' : '',
                        'burned' : '',
                        'collection_name' : '',
                        'schema_name' : '',
                        'template_id' : '',
                        'is_transferable' : '',
                        'is_burnable' : '',
                        'match' : '',
                        'collection_blacklist' : '',
                        'collection_whitelist' : '',
                        'only_duplicate_templates' : '',
                        'authorized_account' : '',
                        'hide_offers' : '',
                        'ids' : '',
                        'lower_bound' : '',
                        'upper_bound' : '',
                        'before' : '',
                        'after' : '',
                        'page' : '',
                        'limit' : '',
                        'order' : '',
                        'sort' : '',
                        }



    def __init__(self):
        super().__init__()

    def print_asset_parameters(self): 
        """ """

        for key in self.asset_parameters: 
            print("%s : %s" % (key, self.asset_parameters[key]))

