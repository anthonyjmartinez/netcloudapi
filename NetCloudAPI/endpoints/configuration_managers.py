from NetCloudAPI.endpoints.endpoint import Endpoint

url = "/api/v2/configuration_managers/"

allowed_meths = ["GET", "PUT"]

allowed_params = {"account": int,
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

allowed_filters = {"account__in": list,
                   "id__in": list,
                   "router__in": list}

allowed_expands = ["account", "router"]


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
                          base_url=url,
                          allowed_meths=allowed_meths,
                          allowed_params=allowed_params,
                          allowed_filters=allowed_filters,
                          allowed_expands=allowed_expands)

        self.method = method
        self.params = params
        self.filters = filters
        self.expands = expands
        self.fields = fields
        self.paging = paging
        self.body = body