from NetCloudAPI.endpoints.endpoint import Endpoint, datetime

URL = "/api/v2/firmwares/"

ALLOWED_METHS = ["GET"]

ALLOWED_PARAMS = {"built_at": datetime,
                  "hash": str,
                  "id": int,
                  "is_deprecated": bool,
                  "product": str,
                  "released_at": datetime,
                  "resource_url": str,
                  "uploaded_at": datetime,
                  "url": str,
                  "version": str}

ALLOWED_FILTERS = {"id__in": list,
                   "version__in": list}


class Firmwares(Endpoint):
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