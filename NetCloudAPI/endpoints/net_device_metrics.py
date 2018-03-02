from NetCloudAPI.endpoints.endpoint import Endpoint, datetime

URL = "/api/v2/net_device_metrics/"

ALLOWED_METHS = ["GET"]

ALLOWED_PARAMS = {"id": int,
                  "resource_url": str,
                  "bytes_in": int,
                  "bytes_out": int,
                  "cinr": float,
                  "dbm": int,
                  "ecio": int,
                  "net_device": int,
                  "rsrp": float,
                  "rsrq": float,
                  "rssi": int,
                  "signal_strength": int,
                  "sinr": float,
                  "update_ts": datetime,
                  "service_type": str}

ALLOWED_FILTERS = {"update_ts__gt": datetime,
                   "update_ts__lt": datetime,
                   "net_device__in": list}


class NetDeviceMetrics(Endpoint):
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