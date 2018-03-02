from NetCloudAPI.endpoints.endpoint import Endpoint, datetime

URL = "/api/v2/routers/"

ALLOWED_METHS = ["GET", "PUT", "DELETE"]

ALLOWED_PARAMS = {"account": int,
                  "actual_firmware": str,
                  "asset_id": str,
                  "config_status": str,
                  "created_at": datetime,
                  "custom1": str,
                  "custom2": str,
                  "description": str,
                  "device_type": str,
                  "full_product_name": str,
                  "group": int,
                  "id": int,
                  "ipv4_address": str,
                  "locality": str,
                  "mac": str,
                  "name": str,
                  "product": str,
                  "reboot_required": bool,
                  "resource_url": str,
                  "serial_number": str,
                  "state": str,
                  "state_updated_at": datetime,
                  "target_firmware": str,
                  "updated_at": datetime}

ALLOWED_FILTERS = {"account__in": list,
                   "device_type__in": list,
                   "group__in": list,
                   "id__in": list,
                   "ipv4_address__in": list,
                   "mac__in": list,
                   "name__in": list,
                   "reboot_required__in": list,
                   "state__in": list,
                   "state_updated_at__lt": datetime,
                   "state_updated_at__gt": datetime,
                   "updated_at__lt": datetime,
                   "updated_at__gt": datetime}

ALLOWED_EXPANDS = ["account", "group"]


class Routers(Endpoint):
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