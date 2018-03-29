"""**NetCloudAPI.endpoints.reboot_activity provides the RebootActivity subclass**"""

from NetCloudAPI.endpoints.endpoint import Endpoint

URI = "/api/v2/reboot_activity/"
"""Defines the uri to append to BASE_URL from NetCloudAPI.req"""


ALLOWED_METHS = ["POST"]
"""Defines the allowed methods for the endpoint.

Only one method from this list may be set at a time. The method setter
function validates based on this list.
"""


class RebootActivity(Endpoint):
    """This Endpoint supports only the "POST" method for specific JSON bodies.

    From the API Documentation:

        To reboot the router with id=42, post the payload:
        ``{"router":"/api/v2/routers/42/"}``

        or using a full resource url (e.g., one obtained from the /api/v2/routers endpoint):
        ``{"router":"http://www.cradlepointecm.com/api/v2/routers/42/"}``

        To reboot the group with id=24, post the payload:
        ``{"group":"/api/v2/groups/24/"}``

        or using a full resource url (e.g., one obtained from the /api/v2/groups endpoint):
        ``{"group":"http://www.cradlepointecm.com/api/v2/groups/24/"}``

    """
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
                          allowed_meths=ALLOWED_METHS)

        self.method = method
        self.params = params
        self.filters = filters
        self.expands = expands
        self.fields = fields
        self.paging = paging
        self.body = body
