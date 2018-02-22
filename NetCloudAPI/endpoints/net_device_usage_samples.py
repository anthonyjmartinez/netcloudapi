from NetCloudAPI.endpoints.endpoint import Endpoint, Unsupported, datetime

url = "/api/v2/net_device_usage_samples/"

allowed_meths = ["GET"]

allowed_params = {"bytes_in": int,
                  "bytes_out": int,
                  "created_at": datetime,
                  "created_at_timeuuid": Unsupported,
                  "period": float,
                  "net_device": int,
                  "uptime": float}

allowed_filters = {"created_at__gt": datetime,
                   "created_at__lt": datetime,
                   "created_at_timeuuid__in": Unsupported,
                   "created_at_timeuuid__gt": Unsupported,
                   "created_at_timeuuid__gte": Unsupported,
                   "created_at_timeuuid__lt": Unsupported,
                   "created_at_timeuuid__lte": Unsupported,
                   "net_device__in": list}


class NetDeviceUsageSamples(Endpoint):
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