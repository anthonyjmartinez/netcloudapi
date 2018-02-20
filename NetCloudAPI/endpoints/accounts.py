from NetCloudAPI.endpoints.endpoint import Endpoint

url = "/api/v2/accounts"

allowed_meths = ["GET", "POST", "PUT", "DELETE"]

allowed_params = {"account": str,
                  "id": int,
                  "is_disabled": bool,
                  "name": str,
                  "resource_url": str}

required_params = {"account": str,
                   "name": str}

allowed_filters = {"account__in": list,
                   "id__in": list,
                   "name__in": list}

allowed_expands = ["account"]


class Accounts(Endpoint):
    def __init__(self):
        Endpoint.__init__(self,
                          base_url=url,
                          allowed_meths=allowed_meths,
                          allowed_params=allowed_params,
                          required_params=required_params,
                          allowed_filters=allowed_filters,
                          allowed_expands=allowed_expands)