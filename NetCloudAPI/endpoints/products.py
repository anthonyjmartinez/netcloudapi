"""**NetCloudAPI.endpoints.products provides the Products subclass.**"""

from NetCloudAPI.endpoints.endpoint import Endpoint

URI = "/api/v2/products/"
"""Defines the uri to append to BASE_URL from NetCloudAPI.req"""

ALLOWED_METHS = ["GET"]
"""Defines the allowed methods for the endpoint.

Only one method from this list may be set at a time. The method setter
function validates based on this list. 
"""

ALLOWED_PARAMS = {"device_type": str,
                  "id": int,
                  "resource_url": str,
                  "series": int}

ALLOWED_FILTERS = {"device_type__in": list,
                   "id__in": list}
"""Defines the allowed params for the endpoint.

The params setter function validates based on this dictionary. Keys passed
to the setter must belong to the set of keys allowed, and the corresponding
value types must match.
"""


class Products(Endpoint):
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
