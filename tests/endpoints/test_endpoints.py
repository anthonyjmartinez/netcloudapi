# Endpoint testing framework using pytest
# As endpoints are added modify @pytest.fixture parameters and ids accordingly.
# Fixtures allow the same set of tests to be executed multiple times against
# various classes/functions/etc.

from NetCloudAPI.endpoints.endpoint import Endpoint, Unsupported
from NetCloudAPI.endpoints.accounts import Accounts
from NetCloudAPI.endpoints.router_stream_usage_samples import RouterStreamUsageSamples
from NetCloudAPI.endpoints.routers import Routers
from NetCloudAPI.endpoints.net_device_usage_samples import NetDeviceUsageSamples
from NetCloudAPI.endpoints.router_state_samples import RouterStateSamples
from NetCloudAPI.endpoints.router_logs import RouterLogs
from NetCloudAPI.endpoints.router_alerts import RouterAlerts
from NetCloudAPI.endpoints.net_device_signal_samples import NetDeviceSignalSamples
from NetCloudAPI.endpoints.net_devices import NetDevices
from NetCloudAPI.endpoints.groups import Groups
from NetCloudAPI.endpoints.firmwares import Firmwares
from NetCloudAPI.endpoints.configuration_managers import ConfigurationManagers
from NetCloudAPI.endpoints.products import Products
from NetCloudAPI.endpoints.reboot_activity import RebootActivity
from datetime import datetime
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


@pytest.fixture(scope="module",
                params=[Endpoint(),
                        Accounts(),
                        Routers(),
                        RouterStreamUsageSamples(),
                        RouterStateSamples(),
                        NetDeviceUsageSamples(),
                        RouterLogs(),
                        RouterAlerts(),
                        NetDeviceSignalSamples(),
                        NetDevices(),
                        Groups(),
                        Firmwares(),
                        ConfigurationManagers(),
                        Products(),
                        RebootActivity()],
                ids=["Endpoint",
                     "Accounts",
                     "Routers",
                     "RouterStreamUsageSamples",
                     "RouterStateSamples",
                     "NetDeviceUsageSamples",
                     "RouterLogs",
                     "RouterAlerts",
                     "NetDeviceSignalSamples",
                     "NetDevices",
                     "Groups",
                     "Firmwares",
                     "ConfigurationManagers",
                     "Products",
                     "RebootActivity"])
def test_endpoint(request):
    return request.param


def test_valchk_str():
    """Test that an invalid string results in a False status"""

    allowed = "test"
    passed = randstr(5)
    ep = Endpoint()

    assert ep.__valchk__(allowed, passed) is False


def test_valchk_list_element():
    """Test that invalid list elements result in a False status"""

    allowed = [1, 2]
    ep = Endpoint()

    assert ep.__valchk__(3, allowed) is False


def test_valchk_list_match():
    """Test that mismatched lists result in a False status"""

    allowed = [1,2,3]
    ep = Endpoint()

    assert ep.__valchk__(badlist(allowed), allowed) is False


def test_valchk_dict_keys():
    """Test that a invalid keys result in a False status"""

    allowed = {"test": str, "test2": int}
    passed = {"test": "toast", randstr(3): 3}
    ep = Endpoint()

    assert ep.__valchk__(passed, allowed) is False


def test_valchk_dict_value_type():
    """Test that invalid value types result in a False status"""

    allowed = {"test": str, "test2": int, "test3": bool}
    passed = badparams(allowed)
    ep = Endpoint()

    assert ep.__valchk__(passed, allowed) is False


def test_valchk_dict_related():
    """Test that related element types are validated - expect False for bad data"""

    allowed = {"test__in": list, "test2__in": list, "created_at__gt": datetime}
    related = {"test": str, "test2": int, "created_at": datetime}
    passed = {"test__in": [1, 2, 3], "test2__in": ["a", "b", "c"], "created_at__gt": randstr(3)}
    ep = Endpoint()

    assert ep.__valchk__(passed, allowed, related=related) is False


def test_valchk_dict_required():
    """Test that required elements are present and of the correct type - expect False for bad data"""

    allowed = {"test": str, "test2": int, "test3": bool}
    required = {"test": str, "test2": int}
    passed = missingreq(required)
    ep = Endpoint()

    print(passed, allowed, required)
    assert ep.__valchk__(passed, allowed, required=required) is False


def test_valid_endpoint_url(test_endpoint):
    """Test that ValueError is raised if the endpoint URL is incorrect"""

    with pytest.raises(ValueError):
        test_endpoint.url = False


def test_valid_method(test_endpoint):
    """Test that ValueError is raised when an invalid method is set"""

    with pytest.raises(ValueError):
        test_endpoint.method = False


def test_params_type_check(test_endpoint):
    """Test that ValueError is raised when params is not a dict or None"""

    with pytest.raises(ValueError):
        test_endpoint.params = False


def test_params_allowed_keys(test_endpoint):
    """Test that ValueError is raised when invalid parameters are passed"""

    with pytest.raises(ValueError):
        test_endpoint.params = {"{}".format(randstr(12)): random.randint(0, 255)}


def test_params_value_type_check(test_endpoint):
    """Test that ValueError is raised if param values are incorrect type"""

    with pytest.raises(ValueError):
        test_endpoint.params = badparams(test_endpoint._Endpoint__allowed_params)


def test_params_required_present(test_endpoint):
    """Test that ValueError is raised if fields required for POST requests are missing """

    with pytest.raises(ValueError):
        if test_endpoint._Endpoint__allowed_meths is None:
            test_endpoint._Endpoint__allowed_meths = ["POST"]

        test_endpoint.method = "POST"
        required = test_endpoint._Endpoint__required_params

        test_endpoint.params = missingreq(required)


def test_filters_allowed_keys(test_endpoint):
    """Test that ValueError is raised if invalid filter keys are passed.
    Also verify that filter keys do not conflict with assigned parameter keys.
    """

    with pytest.raises(ValueError):
        test_endpoint.filters = {"{}".format(randstr(12)): random.randint(0, 255)}


def test_filters_value_type_check(test_endpoint):
    """Test that ValueError is raised if invalid filter values are passed.
    Note: Filters will typically take a list, but the list values need to
    be the same as the type specified for the related parameter value.
    """

    with pytest.raises(ValueError):

        test_endpoint.filters = badparams(test_endpoint._Endpoint__allowed_filters,
                                          related=test_endpoint._Endpoint__allowed_params)


def test_expands_value(test_endpoint):
    """Test that ValueError is raised if invalid expands values are passed."""

    with pytest.raises(ValueError):
        test_endpoint.expands = False


def test_fields_value(test_endpoint):
    """Test that ValueError is raised if invalid fields values are passed."""

    with pytest.raises(ValueError):
        test_endpoint.filters = False


def test_paging_allowed_keys(test_endpoint):
    """Test that ValueError is raised when invalid paging parameters are passed"""

    with pytest.raises(ValueError):
        test_endpoint.paging = {"{}".format(randstr(4)): randstr(4)}


def test_paging_value_type_check(test_endpoint):
    """Test that ValueError is raised if paging values are incorrect type"""

    with pytest.raises(ValueError):
        test_endpoint.paging = badparams(test_endpoint._Endpoint__allowed_paging)


def test_body(test_endpoint):
    """Test that TypeError is raised if body cannot be converted to JSON"""

    with pytest.raises(TypeError):
        test_endpoint.body = {"bad": datetime(2018, 2, 22)}