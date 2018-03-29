"""**NetCloudAPI.req is the module that provides the NetCloudAPI.req() function.**

NetCloudAPI.req.req() is imported by the NetCloudAPI package.
"""

from .endpoints import Endpoint
from requests import Request

BASE_URL = "https://www.cradlepointecm.com"
"""Defines the root of the URL for requests.PreparedRequest generation"""

REQUIRED_HEADERS = {"X-CP-API-ID": str,
                    "X-CP-API-KEY": str,
                    "X-ECM-API-ID": str,
                    "X-ECM-API-KEY": str,
                    "Content-Type": str}
"""Defines the header dictionary keys and value types used for header validation"""


def req(endpoint=None, headers=None):
    """Prepares requests.PreparedRequest objects from passed args.

    Argument validation is featured in order to minimize the risk of invalid
    API calls. While both arguments default to None calling
    NetCloudAPI.req with empty arguments will raise an error.

    Args:
        endpoint (Endpoint): Any one of the NetCloudAPI.endpoints subclasses
        headers (dict): The headers dictionary provided by Cradlepoint ECM.

    Returns:
        A requests.PreparedRequest object if both arguments contain the required elements


    Raises:
        ValueError: If attributes are None
        ValueError: If header 'Content-Type' is not 'application/json'
        ValueError: If other invalid input is detected.
    """
    ep_req = Request()
    ep_attr = ["uri",
               "method",
               "paging",
               "params",
               "filters",
               "fields",
               "expands",
               "body"]
    err = []
    ep_params = {}

    if endpoint is None or headers is None:
        raise ValueError("""args are required; endpoint and headers must be passed""")

    elif isinstance(endpoint, Endpoint) and Endpoint.__valchk__(headers,
                                                                REQUIRED_HEADERS,
                                                                required=REQUIRED_HEADERS):
        if headers["Content-Type"] == "application/json":
            ep_req.headers = headers
            for i in range(len(ep_attr)):
                if ep_attr[i] == "uri":
                    if endpoint.uri is not None:
                        ep_req.url = BASE_URL + endpoint.uri
                    else:
                        err.append(ep_attr[i])

                elif ep_attr[i] == "method":
                    if endpoint.method is not None:
                        ep_req.method = endpoint.method
                    else:
                        err.append(ep_attr[i])

                elif ep_attr[i] == "paging":
                    if endpoint.paging is not None:
                        ep_params.update(endpoint.paging)

                elif ep_attr[i] == "params":
                    if endpoint.params is not None:
                        ep_params.update(endpoint.params)

                elif ep_attr[i] == "filters":
                    if endpoint.filters is not None:
                        for k, v in endpoint.filters.items():
                            if isinstance(v, list):
                                ep_params.update({k: ",".join([str(j) for j in v])})
                            else:
                                ep_params.update({k: v})

                elif ep_attr[i] == "fields":
                    if endpoint.fields is not None:
                        ep_params.update({"fields": ",".join([str(j) for j in endpoint.fields])})

                elif ep_attr[i] == "expands":
                    if endpoint.expands is not None:
                        ep_params.update({"expand": ",".join([str(j) for j in endpoint.expands])})

                elif ep_attr[i] == "body":
                    if endpoint.body is not None:
                        ep_req.json = endpoint.body

            if len(err) > 0:
                raise ValueError("Required attributes ({}) are empty".format(",".join(err)))

            else:
                ep_req.params = ep_params

        else:
            raise ValueError("Content-Type must be 'application/json'")

    else:
        raise ValueError("""Invalid input. See docs.""")

    return ep_req.prepare()
