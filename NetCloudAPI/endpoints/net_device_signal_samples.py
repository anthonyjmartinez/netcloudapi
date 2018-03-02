from NetCloudAPI.endpoints.endpoint import Endpoint, Unsupported, datetime

URL = "/api/v2/net_device_signal_samples/"

ALLOWED_METHS = ["GET"]

ALLOWED_PARAMS = {"cinr": float,
                  "created_at": datetime,
                  "created_at_timeuuid": Unsupported,
                  "dbm": int,
                  "ecio": int,
                  "net_device": int,
                  "rsrp": float,
                  "rsrq": float,
                  "rssi": int,
                  "signal_percent": int,
                  "sinr": float,
                  "uptime": float}

ALLOWED_FILTERS = {"created_at__gt": datetime,
                   "created_at__lt": datetime,
                   "created_at_timeuuid__in": Unsupported,
                   "created_at_timeuuid__gt": Unsupported,
                   "created_at_timeuuid__gte": Unsupported,
                   "created_at_timeuuid__lt": Unsupported,
                   "created_at_timeuuid__lte": Unsupported,
                   "net_device__in": list}


class NetDeviceSignalSamples(Endpoint):
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