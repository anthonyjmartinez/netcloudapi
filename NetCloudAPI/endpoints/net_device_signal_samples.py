"""**NetCloudAPI.endpoints.net_device_signal_samples provides the
NetDeviceSignalSamples subclass.**"""

from NetCloudAPI.endpoints.endpoint import Endpoint, Unsupported, datetime

URI = "/api/v2/net_device_signal_samples/"
"""Defines the uri to append to BASE_URL from NetCloudAPI.req"""

ALLOWED_METHS = ["GET"]
"""Defines the allowed methods for the endpoint.

Only one method from this list may be set at a time. The method setter
function validates based on this list. 
"""

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
"""Defines the allowed params for the endpoint.

The params setter function validates based on this dictionary. Keys passed
to the setter must belong to the set of keys allowed, and the corresponding
value types must match.
"""

ALLOWED_FILTERS = {"created_at__gt": datetime,
                   "created_at__lt": datetime,
                   "created_at_timeuuid__in": Unsupported,
                   "created_at_timeuuid__gt": Unsupported,
                   "created_at_timeuuid__gte": Unsupported,
                   "created_at_timeuuid__lt": Unsupported,
                   "created_at_timeuuid__lte": Unsupported,
                   "net_device__in": list}
"""Defines the allowed filters for the endpoint.

The filters setter function validates based on this dictionary, and the
related ALLOWED_PARAMS dictionary. All list elements must match the
corresponding ALLOWED_PARAMS type for the key preceding the '__' within
the ALLOWED_FILTERS dictionary key. A subset of the allowed keys may be passed.
"""


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
                          base_uri=URI,
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
