from NetCloudAPI.endpoints.endpoint import Endpoint

URL = "/api/v2/groups/"

ALLOWED_METHS = ["GET", "POST", "PUT", "DELETE"]

ALLOWED_PARAMS = {"account": int,
                  "configuration": str,
                  "device_type": str,
                  "id": int,
                  "name": str,
                  "product": str,
                  "resource_url": str,
                  "target_configuration": str}

REQUIRED_PARAMS = {"account": int,
                   "name": str,
                   "product": str,
                   "target_firmware": str}

ALLOWED_FILTERS = {"account__in": list,
                   "device_type__in": list,
                   "id__in": list,
                   "name__in": list}

ALLOWED_EXPANDS = ["account"]


class Groups(Endpoint):
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
                          required_params=REQUIRED_PARAMS,
                          allowed_filters=ALLOWED_FILTERS,
                          allowed_expands=ALLOWED_EXPANDS)

        self.method = method
        self.params = params
        self.filters = filters
        self.expands = expands
        self.fields = fields
        self.paging = paging
        self.body = body