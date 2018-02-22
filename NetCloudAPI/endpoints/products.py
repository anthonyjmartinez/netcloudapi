from NetCloudAPI.endpoints.endpoint import Endpoint

url = "/api/v2/products/"

allowed_meths = ["GET"]

allowed_params = {"device_type": str,
                  "id": int,
                  "resource_url": str,
                  "series": int}

allowed_filters = {"device_type__in": list,
                   "id__in": list}


class Products(Endpoint):
    def __init__(self,
                 method=None,
                 params=None,
                 filters=None,
                 expands=None,
                 fields=None,
                 paging=None,
                 body=None):

        Endpoint.__init__(self,
                          base_url=url,
                          allowed_meths=allowed_meths,
                          allowed_params=allowed_params,
                          allowed_filters=allowed_filters)

        self.method = method
        self.params = params
        self.filters = filters
        self.expands = expands
        self.fields = fields
        self.paging = paging
        self.body = body