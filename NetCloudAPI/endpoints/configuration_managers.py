from NetCloudAPI.endpoints.endpoint import Endpoint

URL = "/api/v2/configuration_managers/"

ALLOWED_METHS = ["GET", "PUT"]

ALLOWED_PARAMS = {"account": int,
                  "id": int,
                  "resource_url": str,
                  "actual": str,
                  "pending": str,
                  "target": str,
                  "version_number": int,
                  "router": int,
                  "synched": bool,
                  "suspended": bool,
                  "configuration": str}

ALLOWED_FILTERS = {"account__in": list,
                   "id__in": list,
                   "router__in": list}

ALLOWED_EXPANDS = ["account", "router"]


class ConfigurationManagers(Endpoint):
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
                          allowed_filters=ALLOWED_FILTERS,
                          allowed_expands=ALLOWED_EXPANDS)

        self.method = method
        self.params = params
        self.filters = filters
        self.expands = expands
        self.fields = fields
        self.paging = paging
        self.body = body