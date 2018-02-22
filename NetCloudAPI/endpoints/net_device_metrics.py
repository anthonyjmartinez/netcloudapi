from NetCloudAPI.endpoints.endpoint import Endpoint, Unsupported, datetime

url = "/api/v2/net_device_metrics/"

allowed_meths = ["GET"]

allowed_params = {"id": int,
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

allowed_filters = {"update_ts__gt": datetime,
                   "update_ts__lt": datetime,
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