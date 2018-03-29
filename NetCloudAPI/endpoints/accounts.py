"""**NetCloudAPI.endpoints.accounts provides the Accounts subclass.**"""

from NetCloudAPI.endpoints.endpoint import Endpoint

URI = "/api/v2/accounts/"
"""Defines the uri to append to BASE_URL from NetCloudAPI.req"""

ALLOWED_METHS = ["GET", "POST", "PUT", "DELETE"]
"""Defines the allowed methods for the endpoint.

Only one method from this list may be set at a time. The method setter
function validates based on this list. 
"""

ALLOWED_PARAMS = {"account": int,
                  "id": int,
                  "is_disabled": bool,
                  "name": str,
                  "resource_url": str}
"""Defines the allowed params for the endpoint.

The params setter function validates based on this dictionary. Keys passed
to the setter must belong to the set of keys allowed, and the corresponding
value types must match.
"""

REQUIRED_PARAMS = {"account": int,
                   "name": str}
"""Defines the required params for the endpoint when method = "POST".

The params setter function validates based on this dictionary when method = "POST".
Keys passed to the setter must belong to the set of keys allowed in ALLOWED_PARAMS
and include all REQUIRED_PARAMS. The corresponding value types must match.
"""


ALLOWED_FILTERS = {"account__in": list,
                   "id__in": list,
                   "name__in": list}
"""Defines the allowed filters for the endpoint.

The filters setter function validates based on this dictionary, and the
related ALLOWED_PARAMS dictionary. All list elements must match the
corresponding ALLOWED_PARAMS type for the key preceding the '__' within
the ALLOWED_FILTERS dictionary key. A subset of the allowed keys may be passed.
"""

ALLOWED_EXPANDS = ["account"]
"""Defines the allowed expands for the endpoint

The expands setter function validates based on this list, and the passed
object **must** also be a list that is a set of the ALLOWED_EXPANDS values.
"""


class Accounts(Endpoint):
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
                          required_params=REQUIRED_PARAMS,
                          allowed_filters=ALLOWED_FILTERS,
                          allowed_expands=ALLOWED_EXPANDS)

        self.method = method
        self.params = params
        self.filters = filters
        self.expands = expands
        self.fields = fields
        self.paging = paging
        self.body = body
