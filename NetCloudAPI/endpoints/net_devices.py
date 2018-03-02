from NetCloudAPI.endpoints.endpoint import Endpoint, datetime

URL = "/api/v2/net_devices/"

ALLOWED_METHS = ["GET"]

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

ALLOWED_FILTERS = {"account__in": list,
                   "connection_state__in": list,
                   "id__in": list,
                   "ipv4_address__in": list,
                   "mode__in": list,
                   "router__in": list,
                   "net_device__in": list}

ALLOWED_EXPANDS = ["account", "router"]


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
                          base_url=URL,
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