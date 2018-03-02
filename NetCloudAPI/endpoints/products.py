from NetCloudAPI.endpoints.endpoint import Endpoint

URL = "/api/v2/products/"

ALLOWED_METHS = ["GET"]

ALLOWED_PARAMS = {"device_type": str,
                  "id": int,
                  "resource_url": str,
                  "series": int}

ALLOWED_FILTERS = {"device_type__in": list,
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
                          base_url=URL,
                          allowed_meths=ALLOWED_METHS,
                          allowed_params=ALLOWED_PARAMS,
                          allowed_filters=ALLOWED_FILTERS)

        self.method = method
        self.params = params
        self.filters = filters
        self.expands = expands
        self.fields = fields
        self.paging = paging
        self.body = body