# NetCloudAPI Request test cases using pytest

from NetCloudAPI import req
from NetCloudAPI.endpoints.endpoint import Endpoint, Unsupported
from NetCloudAPI.endpoints.accounts import Accounts
from datetime import datetime
from requests import PreparedRequest
import pytest
import random
import string
import re


def randstr(length):
    """Returns a random string of specified length"""
    return "".join([random.choice(string.ascii_letters)
                    for i in range(length)])


def badparams(params, related=None):
    """Builds a parameters dictionary with bad value types"""

    if params is not None:
        p = {}
        if related is None:
            for k, v in params.items():
                if v is str:
                    p.update({k: random.randint(0, 255)})

                elif v is int:
                    p.update({k: randstr(12)})

                elif v is float:
                    p.update({k: randstr(12)})

                elif v is datetime:
                    p.update({k: randstr(12)})

                elif v is Unsupported:
                    p.update({k: randstr(4)})

                elif v is bool:
                    p.update({k: randstr(4)})

                elif isinstance(v, str):
                    p.update({k: randstr(4)})

        elif related is not None:
            for k, v in params.items():
                rk = re.split("__", k)[0]
                rt = related.get(rk)
                if rt is str:
                    if v is list:
                        p.update({k: [random.randint(0, 255) for i in params]})
                    else:
                        p.update({k: random.randint(0, 255)})

                elif rt is int:
                    if v is list:
                        p.update({k: [randstr(4) for i in params]})
                    else:
                        p.update({k: randstr(4)})

                elif rt is datetime:
                    p.update({k: randstr(4)})

                elif rt is Unsupported:
                    p.update({k: randstr(4)})

                elif rt is bool:
                    p.update({k: randstr(4)})

    else:
        p = False

    return p


def missingreq(params):
    """Builds a parameters dictionary with a missing required parameter"""

    if params is not None:
        p = {}
        for k, v in params.items():
            if v is str:
                p.update({k: randstr(12)})

            elif v is int:
                p.update({k: random.randint(0, 255)})

            elif v is bool:
                p.update({k: random.choice([True, False])})

            elif v is float:
                p.update({k: float(random.randint(0, 255))})

        p.popitem()

    else:
        p = False

    return p


def badlist(allowed):
    """Builds a list with invalid value types"""

    if isinstance(allowed[0], int):
        p = [randstr(3) for i in allowed]

    elif isinstance(allowed[0], str):
        p = [random.randint(0, 255) for i in allowed]

    else:
        p = False

    return p


@pytest.fixture(scope="function")
def test_endpoint():
    return Endpoint()


def test_req_input_endpoint_obj():
    """Test that ValueError is raised if the passed endpoint is not a valid Endpoint object"""

    with pytest.raises(ValueError):
        headers = {"X-CP-API-ID": "test",
                   "X-CP-API-KEY": "test",
                   "X-ECM-API-ID": "test",
                   "X-ECM-API-KEY": "test",
                   "Content-Type": "application/json"}

        req(endpoint=randstr(12), headers=headers)


def test_req_input_header_obj(test_endpoint):
    """Test that ValueError is raised if the header is missing any required keys"""

    with pytest.raises(ValueError):
        required_headers = {"X-CP-API-ID": str,
                            "X-CP-API-KEY": str,
                            "X-ECM-API-ID": str,
                            "X-ECM-API-KEY": str,
                            "Content-Type": str}
        req(endpoint=test_endpoint, headers=missingreq(required_headers))


def test_req_output_obj():
    """Test that response for valid input is a PreparedRequest object"""

    headers = {"X-CP-API-ID": "test",
               "X-CP-API-KEY": "test",
               "X-ECM-API-ID": "test",
               "X-ECM-API-KEY": "test",
               "Content-Type": "application/json"}

    ep_filters = {"account__in": [1, 2, 3, 4]}

    endpoint = Accounts(method="GET",
                        filters=ep_filters,
                        expands=["account"])

    assert isinstance(req(endpoint=endpoint, headers=headers), PreparedRequest)