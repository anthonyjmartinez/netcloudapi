from NetCloudAPI.endpoints.endpoint import Endpoint, datetime

url = "/api/v2/firmwares/"

allowed_meths = ["GET"]

allowed_params = {"built_at": datetime,
                  "hash": str,
                  "id": int,
                  "is_deprecated": bool,
                  "product": str,
                  "released_at": datetime,
                  "resource_url": str,
                  "uploaded_at": datetime,
                  "url": str,
                  "version": str}

allowed_filters = {"id__in": list,
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