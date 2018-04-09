## Introduction

NetCloudAPI provides a Python 3 interface to the Cradlepoint NetCloud API
in order to facilitate the rapid development of tools that leverage
that API. At this time, direct processing of the returned data is out of scope.

NetCloudAPI's project page is here:
https://github.com/anthonyjmartinez/netcloudapi


## Requirements

NetCloudAPI depends on the 'requests' module for interaction with the
Cradlepoint API endpoints. There are no other requirements or dependencies
outside of the Python 3 standard library.

Python Requests installation information and documentation can be obtained
here: http://docs.python-requests.org/en/master/


## Recommended Modules

While processing of the JSON dataset returned by the Cradlepoint API endpoints
is presently out of scope, the project recommends the use of the Python Data
Analysis Library, Pandas, for processing returned data.

Pandas installation information and documentation can be obtained here:
https://pandas.pydata.org/


## Installation

Use pip from pypi.org:

    pip install netcloudapi

Or download the sdist from the project page:

    pip install /your/path/to/netcloudapi-<version>.tar.gz

## Configuration

Cradlepoint authenticates API users with tokens presented within the request
header. The only configuration necessary is to ensure all scripts using
NetCloudAPI contain the proper declaration of API tokens. These tokens are
available through your NetCloud ECM portal. Define a dictionary, headers, as
follows:

    headers = {
        'X-CP-API-ID': 'somekey',
        'X-CP-API-KEY': 'anotherkey',
        'X-ECM-API-ID': 'yetanotherkey',
        'X-ECM-API-KEY': 'lastkey',
        'Content-Type': 'application/json'
    }

This object will then be passed to the appropriate NetCloudAPI methods when
making calls against the Cradlepoint API.

## Usage

    # Import Pandas for data analysis
    # Not required for NetCloudAPI Use - but recommended
    import pandas as pd
    import NetCloudAPI
    from NetCloudAPI.endpoints import Routers, RouterStateSamples

    RESOURCE_LIMIT = 100
    REPORT_FROM = datetime(someyear, somemonth, someday)

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

    # Some endpoints (RouterStateSamples for example) only support calls for
    # data on a maximum of 100 devices - in these cases you must use a loop
    # such as the following:

    router_ids = routers.id.astype('int')
    routerstatesamples = pd.DataFrame()

    while len(router_ids) > 0:
        router_list = list(router_ids[:RESOURCE_LIMIT])

        routerstatesamples_ep = RouterStateSamples(filters={"router__in" : router_list,
                                                            "created_at__gt": REPORT_FROM},
                                                   fields=["created_at", "period",
                                                           "state", "router"],
                                                   paging={"limit": 500},
                                                   method="GET")

        routerstatesamples_req = req(routerstatesamples_ep, headers)
        rss_data = call(routerstatesamples_req)
        routerstatesamples = routerstatesamples.append(pd.DataFrame(rss_data["data"]))
        router_ids = router_ids.iloc[RESOURCE_LIMIT:]

    routerstatesamples.to_excel("/some/arbitrary/path/routerstatesamples.xlsx", index=False)