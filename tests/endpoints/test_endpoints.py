# Endpoint testing framework using pytest
# As endpoints are added modify @pytest.fixture parameters and ids accordingly.
# Fixtures allow the same set of tests to be executed multiple times against
# various classes/functions/etc.

from NetCloudAPI.endpoints.endpoint import Endpoint
import pytest
import random
import string

def randstr(length):
    """Returns a random string of specified length"""
    return "".join([random.choice(string.ascii_letters)
                    for i in range(length)])


def badparams(params):
    """Builds a parameters dictionary with bad value types"""

    p = {}
    for k,v in params.items():
        if v is str:
            p.update({k: random.randint(0,255)})

        elif v is int:
            p.update({k: randstr(12)})

    return p



@pytest.fixture(scope="module",
                params=[Endpoint()],
                ids=["Endpoint"])
def test_endpoint(request):
    return request.param


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
        test_endpoint.params = {"{}".format(randstr(12)): random.randint(0,255)}

def test_params_value_type_check(test_endpoint):
    """Test that AssertionError is raised if param values are incorrect type"""

    with pytest.raises(AssertionError):
        test_endpoint.params = badparams(test_endpoint.__allowed_params)


def test_params_required_present(test_endpoint):
    """Test that ValueError is raised if fields required for POST requests are missing """


def test_filters_allowed_keys(test_endpoint):
    """Test that ValueError is raised if invalid filter keys are passed.
    Also verify that filter keys do not conflict with assigned parameter keys.
    """

def test_filters_value_type_check(test_endpoint):
    """Test that ValueError is raised if invalid filter values are passed.
    Note: Filters will typically take a list, but the list values need to
    be the same as the type specified for the related parameter value.
    """

def test_expands_value(test_endpoint):
    """Test that ValueError is raised if invalid expands values are passed."""