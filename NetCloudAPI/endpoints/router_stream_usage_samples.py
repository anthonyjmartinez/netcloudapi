from NetCloudAPI.endpoints.endpoint import Endpoint, Unsupported, datetime

url = "/api/v2/router_stream_usage_samples/"

allowed_meths = ["GET"]

allowed_params = {"bytes_in": int,
                  "bytes_out": int,
                  "created_at": datetime,
                  "created_at_timeuuid": Unsupported,
                  "period": float,
                  "router": int,
                  "uptime": float}

required_params = None

allowed_filters = {"created_at__gt": datetime,
                   "created_at__lt": datetime,
                   "created_at_timeuuid__in": Unsupported,
                   "created_at_timeuuid__gt": Unsupported,
                   "created_at_timeuuid__gte": Unsupported,
                   "created_at_timeuuid__lt": Unsupported,
                   "created_at_timeuuid__lte": Unsupported,
                   "router__in": list}

allowed_expands = None


class RouterStreamUsageSamples(Endpoint):
    def __init__(self,
                 method=None,
                 params=None,
                 filters=None,
                 expands=None):

        Endpoint.__init__(self,
                          base_url=url,
                          allowed_meths=allowed_meths,
                          allowed_params=allowed_params,
                          required_params=required_params,
                          allowed_filters=allowed_filters,
                          allowed_expands=allowed_expands)

        self.method = method
        self.params = params
        self.filters = filters
        self.expands = expands