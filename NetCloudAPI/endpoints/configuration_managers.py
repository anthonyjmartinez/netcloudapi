"""**NetCloudAPI.endpoints.configuration_managers provides the
ConfigurationManagers subclass.**"""

from NetCloudAPI.endpoints.endpoint import Endpoint

URI = "/api/v2/configuration_managers/"
"""Defines the uri to append to BASE_URL from NetCloudAPI.req"""

ALLOWED_METHS = ["GET", "PUT"]
"""Defines the allowed methods for the endpoint.

Only one method from this list may be set at a time. The method setter
function validates based on this list. 
"""

ALLOWED_PARAMS = {"account": int,
                  "id": int,
                  "resource_url": str,
                  "actual": str,
                  "pending": str,
                  "target": str,
                  "version_number": int,
                  "router": int,
                  "synched": bool,
                  "suspended": bool,
                  "configuration": str}
"""Defines the allowed params for the endpoint.

The params setter function validates based on this dictionary. Keys passed
to the setter must belong to the set of keys allowed, and the corresponding
value types must match.
"""

ALLOWED_FILTERS = {"account__in": list,
                   "id__in": list,
                   "router__in": list}
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


class ConfigurationManagers(Endpoint):
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
