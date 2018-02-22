from NetCloudAPI.endpoints.endpoint import Endpoint, Unsupported, datetime

url = "/api/v2/router_logs/"

allowed_meths = ["GET"]

allowed_params = {"created_at": datetime,
                  "created_at_timeuuid": Unsupported,
                  "exception": str,
                  "level": str,
                  "message": str,
                  "reported_at": datetime,
                  "router": int,
                  "sequence": int,
                  "source": str}

allowed_filters = {"created_at__gt": datetime,
                   "created_at__lt": datetime,
                   "created_at_timeuuid__in": Unsupported,
                   "created_at_timeuuid__gt": Unsupported,
                   "created_at_timeuuid__gte": Unsupported,
                   "created_at_timeuuid__lt": Unsupported,
                   "created_at_timeuuid__lte": Unsupported,
                   "router__in": list}


class RouterLogs(Endpoint):
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