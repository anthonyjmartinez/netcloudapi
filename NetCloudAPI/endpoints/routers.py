"""**NetCloudAPI.endpoints.routers provides the Routers subclass.**"""

from NetCloudAPI.endpoints.endpoint import Endpoint, datetime

URI = "/api/v2/routers/"
"""Defines the uri to append to BASE_URL from NetCloudAPI.req"""

ALLOWED_METHS = ["GET", "PUT", "DELETE"]
"""Defines the allowed methods for the endpoint.

Only one method from this list may be set at a time. The *method* setter
function validates based on this list. 
"""

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
"""Defines the allowed params for the endpoint.

The params setter function validates based on this dictionary. Keys passed
to the setter must belong to the set of keys allowed, and the corresponding
value types must match.
"""

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
"""Defines the allowed filters for the endpoint.

The filters setter function validates based on this dictionary, and the
related ALLOWED_PARAMS dictionary. All list elements must match the
corresponding ALLOWED_PARAMS type for the key preceding the '__' within
the ALLOWED_FILTERS dictionary key. A subset of the allowed keys may be passed.
"""

ALLOWED_EXPANDS = ["account", "group"]
"""Defines the allowed expands for the endpoint

The expands setter function validates based on this list, and the passed
object **must** also be a list that is a set of the ALLOWED_EXPANDS values.
"""


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
