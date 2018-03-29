"""**NetCloudAPI.endpoints.net_devices provides the NetDevices subclass.**"""

from NetCloudAPI.endpoints.endpoint import Endpoint, datetime

URI = "/api/v2/net_devices/"
"""Defines the uri to append to BASE_URL from NetCloudAPI.req"""


ALLOWED_METHS = ["GET"]
"""Defines the allowed methods for the endpoint.

Only one method from this list may be set at a time. The method setter
function validates based on this list. 
"""

ALLOWED_PARAMS = {"account": int,
                  "bsid": str,
                  "carrier": str,
                  "carrier_id": str,
                  "channel": int,
                  "connection_state": str,
                  "dns0": str,
                  "dns1": str,
                  "esn": str,
                  "gateway": str,
                  "gsn": str,
                  "homecarrid": str,
                  "hostname": str,
                  "iccid": str,
                  "id": int,
                  "imei": str,
                  "imsi": str,
                  "ipv4_address": str,
                  "is_asset": bool,
                  "is_gps_supported": bool,
                  "is_upgrade_available": bool,
                  "ltebandwidth": str,
                  "mac": str,
                  "manufacturer": str,
                  "mdn": str,
                  "meid": str,
                  "mfg_model": str,
                  "mn_ha_spi": str,
                  "mn_ha_ss": str,
                  "mode": str,
                  "model": str,
                  "model_fw": str,
                  "mtu": int,
                  "nai": str,
                  "name": str,
                  "netmask": str,
                  "pin_status": str,
                  "port": str,
                  "prlv": str,
                  "mfg_product": str,
                  "profile": str,
                  "resource_url": str,
                  "rfband": str,
                  "rfchannel": str,
                  "roam": str,
                  "router": int,
                  "rxchannel": str,
                  "serial": str,
                  "service_type": str,
                  "ssid": str,
                  "summary": str,
                  "txchannel": str,
                  "type": str,
                  "uid": str,
                  "updated_at": datetime,
                  "uptime": float,
                  "ver_pkg": str,
                  "version": str,
                  "wimax_realm": str}
"""Defines the allowed params for the endpoint.

The params setter function validates based on this dictionary. Keys passed
to the setter must belong to the set of keys allowed, and the corresponding
value types must match.
"""

ALLOWED_FILTERS = {"account__in": list,
                   "connection_state__in": list,
                   "id__in": list,
                   "ipv4_address__in": list,
                   "mode__in": list,
                   "router__in": list,
                   "net_device__in": list}
"""Defines the allowed filters for the endpoint.

The filters setter function validates based on this dictionary, and the
related ALLOWED_PARAMS dictionary. All list elements must match the
corresponding ALLOWED_PARAMS type for the key preceding the '__' within
the ALLOWED_FILTERS dictionary key. A subset of the allowed keys may be passed.
"""

ALLOWED_EXPANDS = ["account", "router"]
"""Defines the allowed expands for the endpoint

The expands setter function validates based on this list, and the passed
object **must** also be a list that is a set of the ALLOWED_EXPANDS values.
"""


class NetDevices(Endpoint):
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
                          allowed_filters=ALLOWED_FILTERS,
                          allowed_expands=ALLOWED_EXPANDS)

        self.method = method
        self.params = params
        self.filters = filters
        self.expands = expands
        self.fields = fields
        self.paging = paging
        self.body = body
