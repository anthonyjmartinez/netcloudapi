# NetCloudAPI Call test cases using pytest
# Uses the Accounts endpoint subclass as it can use all HTTP methods

from NetCloudAPI import req
from NetCloudAPI import call
from NetCloudAPI.endpoints.accounts import Accounts
from requests import Session
from requests_mock import Adapter
import re
import random
import pytest


@pytest.fixture(scope="module")
def headers():
    return {"X-CP-API-ID": "abc",
            "X-CP-API-KEY": "def",
            "X-ECM-API-ID": "ghi",
            "X-ECM-API-KEY": "jkl",
            "Content-Type": "application/json"}

@pytest.fixture(scope="function")
def accounts():
    return Accounts()


@pytest.fixture(scope="function")
def adapter():
    return Adapter()


@pytest.fixture(scope="function")
def session():
    return Session()


def test_call_response_json_obj(headers, accounts, adapter, session):
    """Test that the response object exists and is a dictionary"""

    match = re.compile("/api/v2/")

    adapter.register_uri("GET",
                         match,
                         status_code=200,
                         json={"data": [{"id": 42,
                                         "is_disabled": False},
                                        {"id": 23098,
                                         "is_disabled": False},
                                        {"id": 24,
                                         "is_disabled": False}],
                               "meta": {"limit": 20,
                                        "next": None,
                                        "offset": 0,
                                        "previous": None}})
    session.mount("https://www.cradlepointecm.com", adapter)

    accounts.method = "GET"
    accounts.params = {"account": 999}
    ep_req = req(endpoint=accounts, headers=headers)

    assert isinstance(call(ep_req, session=session), dict)


def test_call_response_to_error_codes(headers, accounts, adapter, session):
    """Test that response objects with status codes in the error code list return error details"""

    match = re.compile("account=999")

    adapter.register_uri("GET",
                         match,
                         status_code=random.choice([302, 400, 401, 403, 404, 405, 409, 429, 500, 502]),
                         json={"exception": {"message": "forbidden",
                                             "type": "error"},
                               "errors": []})

    session.mount("https://www.cradlepointecm.com", adapter)
    accounts.method = "GET"
    accounts.params = {"account": 999}
    ep_req = req(endpoint=accounts, headers=headers)

    assert call(ep_req, session=session)["NetCloudAPI Error"] is not None


def test_call_response_no_next(headers, accounts, adapter, session):
    """Test that response objects without a 'next' element still return the response object"""

    match = re.compile("account=999")

    adapter.register_uri("GET",
                         match,
                         status_code=200,
                         json={"data": [{"account": 999,
                                         "id": 12,
                                         "name": "testing"}],
                               "meta": {"limit": 20,
                                        "next": None,
                                        "offset": 0,
                                        "previous": None}})

    session.mount("https://www.cradlepointecm.com", adapter)
    accounts.method = "GET"
    accounts.params = {"account": 999}
    ep_req = req(endpoint=accounts, headers=headers)

    assert call(ep_req, session=session)["meta"]["limit"] == 20


def test_call_response_with_next(headers, accounts, adapter, session):
    """Test that fetching 'next' URLs grows the response data object"""
    match = re.compile("account=999")
    match2 = re.compile("more=1")

    adapter.register_uri("GET",
                         match,
                         status_code=200,
                         json={"data": [{"account": 999,
                                         "id": 12,
                                         "name": "testing"}],
                               "meta": {"limit": 20,
                                        "next": "https://www.cradlepointecm.com/api/v2/accounts/?more=1",
                                        "offset": 0,
                                        "previous": "https://www.cradlepointecm.com/api/v2/accounts/?account=999"}})

    adapter.register_uri("GET",
                         match2,
                         status_code=200,
                         json={"data": [{"account": 1000,
                                         "id": 21,
                                         "name": "testing2"}],
                               "meta": {"limit": 20,
                                        "next": None,
                                        "offset": 0,
                                        "previous": "https://www.cradlepointecm.com/api/v2/accounts/?more=1"}})

    session.mount("https://www.cradlepointecm.com", adapter)
    accounts.method = "GET"
    accounts.params = {"account": 999}
    ep_req = req(endpoint=accounts, headers=headers)

    assert len(call(ep_req, session=session)["data"]) == 2
