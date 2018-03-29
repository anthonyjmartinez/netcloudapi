"""**NetCloudAPI provides an interface to the Cradlepoint ECM API.**

NetCloudAPI provides a pythonic way to create and execute requests to the
Cradlepoint ECM API v2. Each of the available endpoints is represented in
classes of the **NetCloudAPI.endpoints** subpackage.

NetCloudAPI imports the following functions:
    * req() for building requests from Endpoints
    * call() for sending requests to the API, and handling the responses

Example::

    # Import Pandas for data analysis
    # Not required for NetCloudAPI Use - but recommended
    import pandas as pd
    import NetCloudAPI
    from NetCloudAPI.endpoints import Routers

    # NetCloud ECM Groups for subset of Routers
    ecm_groups = [12345,
                  67891,
                  34567]

    # Request Headers with NetCloud ECM API IDs/Keys
    headers = {'X-CP-API-ID': 'your_cp_api_id',
               'X-CP-API-KEY': 'your_cp_api_key',
               'X-ECM-API-ID': 'your_ecm_api_id',
               'X-ECM-API-KEY': 'your_ecm_api_key',
               'Content-Type': 'application/json'}

    router_ep = Routers(filters={"group__in": ecm_groups},
                        paging={"limit": 500},
                        fields=["id", "asset_id", "mac", "state"],
                        method="GET")

    router_req = NetCloudAPI.req(endpoint=router_ep,
                                 headers=headers)

    router_data = NetCloudAPI.call(router_req)
    routers = pd.DataFrame(router_data["data"])
    routers.to_excel("/some/arbitrary/path.xlsx", index=False)

Warnings:
    The Cradlepoint ECM API requires authentication. It is necessary for users to
    have the appropriate Cradlepoint ECM API credentials for their account. Use of
    this package is not possible without the appropriate headers::

        headers = {'X-CP-API-ID': 'your_cp_api_id',
                   'X-CP-API-KEY': 'your_cp_api_key',
                   'X-ECM-API-ID': 'your_ecm_api_id',
                   'X-ECM-API-KEY': 'your_ecm_api_key',
                   'Content-Type': 'application/json'}

    If you do not have the credentials above contact your Cradlepoint ECM administrator
    and request them.
"""


from .req import req
from .call import call

