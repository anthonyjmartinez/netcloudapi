from .endpoints import Endpoint
from requests import Request

BASE_URL = "https://www.cradlepointecm.com"

REQUIRED_HEADERS = {"X-CP-API-ID": str,
                    "X-CP-API-KEY": str,
                    "X-ECM-API-ID": str,
                    "X-ECM-API-KEY": str,
                    "Content-Type": str}


def req(endpoint=None, headers=None):
    """Builds and returns PreparedRequest object from passed Endpoint and Headers"""
    ep_req = Request()
    ep_attr = ["url",
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
        raise ValueError("""kwargs are required, endpoint and headers must be passed""")

    elif isinstance(endpoint, Endpoint) and Endpoint.__valchk__(headers,
                                                                REQUIRED_HEADERS,
                                                                required=REQUIRED_HEADERS):
        if headers["Content-Type"] == "application/json":
            ep_req.headers = headers
            for i in range(len(ep_attr)):
                if ep_attr[i] == "url":
                    if endpoint.url is not None:
                        ep_req.url = BASE_URL + endpoint.url
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