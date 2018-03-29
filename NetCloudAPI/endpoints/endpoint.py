"""**NetCloudAPI.endpoints.endpoint provides the Endpoint superclass.**"""

import re
import json
from datetime import datetime


class Endpoint(object):
    """Superclass for all Cradlepoint ECM API endpoint subclasses.

    Setter methods validate structure and type, where applicable, based on
    Cradlepoint ECM API reference documentation. Subclasses override the
    init method to define subclass specific allowable fields and data types.
    """
    def __init__(self,
                 base_uri=None,
                 allowed_meths=None,
                 allowed_params=None,
                 required_params=None,
                 allowed_filters=None,
                 allowed_expands=None,
                 method=None,
                 params=None,
                 filters=None,
                 expands=None,
                 fields=None,
                 paging=None,
                 body=None):

        self.__base_uri = base_uri
        self.__allowed_meths = allowed_meths
        self.__allowed_params = allowed_params
        self.__required_params = required_params
        self.__allowed_filters = allowed_filters
        self.__allowed_expands = allowed_expands
        self.__allowed_paging = {"limit": int, "offset": int}
        self.method = method
        self.params = params
        self.filters = filters
        self.expands = expands
        self.fields = fields
        self.paging = paging
        self.body = body
        self.uri = base_uri

    @staticmethod
    def __valchk__(passed, allowed, required=None, related=None):
        """Validates passed values against defined allowed, required, or related known data"""

        err = 0
        if passed is None:
            pass

        elif isinstance(passed, str) and isinstance(allowed, str):
            if passed == allowed:
                pass
            else:
                err += 1

        elif isinstance(passed, str) and isinstance(allowed, list):
            if passed in allowed:
                pass
            else:
                err += 1

        elif isinstance(passed, list) and isinstance(allowed, list):
            pset = set(passed)
            aset = set(allowed)

            if not bool(pset.difference(aset)):
                pass
            else:
                err += 1

        elif isinstance(passed, dict) and isinstance(allowed, dict):
            pkset = set(list(passed.keys()))
            akset = set(list(allowed.keys()))

            if not bool(pkset.difference(akset)):
                if related is not None:
                    for k, v in passed.items():
                        if allowed.get(k) is datetime and isinstance(v, allowed.get(k)):
                            pass

                        elif isinstance(v, allowed.get(k)):
                            rk = re.split("__", k)[0]
                            for i in v:
                                if isinstance(i, related.get(rk)):
                                    pass
                                else:
                                    err += 1

                        else:
                            err += 1

                elif required is not None:
                    reqkset = set(list(required.keys()))
                    if not bool(reqkset.difference(pkset)):
                        for k, v in passed.items():
                            if isinstance(v, allowed.get(k)):
                                pass
                            else:
                                err += 1
                    else:
                        err += 1

                else:
                    for k, v in passed.items():
                        if isinstance(v, allowed.get(k)):
                            pass
                        else:
                            err += 1

            else:
                err += 1

        else:
            err += 1

        if err is 0:
            return True
        else:
            return False

    @property
    def uri(self):
        """Class *uri* property getter/setter

        Returns:
                The configured base URI (str).

        Raises:
                ValueError: If the setter attempts to change the uri.
        """
        return self.__uri

    @uri.setter
    def uri(self, passed):
        if passed is None:
            self.__uri = passed

        elif self.__valchk__(passed, self.__base_uri):
            self.__uri = passed

        else:
            raise ValueError("The URI is protected and must be {}"
                             .format(self.__base_uri))

    @property
    def method(self):
        """Class *method* property getter/setter

        Returns:
            The configured HTTP request method (str)

        Raises:
            ValueError: If an invalid or unsupported method is passed to the setter.
            ValueError: If the setter is passed a non-str object.
        """
        return self.__method

    @method.setter
    def method(self, passed):
        if passed is None:
            self.__method = passed

        elif self.__valchk__(passed, self.__allowed_meths):
            self.__method = passed

        else:
            raise ValueError("Invalid HTTP Method. Use one of: {}".
                             format(self.__allowed_meths))

    @property
    def params(self):
        """Class *params* property getter/setter

        Returns:
            The configured request parameters (dict)

        Raises:
            ValueError: If invalid parameter keys are passed to setter.
            ValueError: If invalid parameter values are passed to setter.
            ValueError: If method = 'POST' and required parameters are missing.
            ValueError: If the setter is passed a non-dict object.
        """
        return self.__params

    @params.setter
    def params(self, passed):
        if passed is None:
            self.__params = passed

        elif self.method == "POST" and self.__required_params is not None:
            if self.__valchk__(passed, self.__allowed_params, required=self.__required_params):
                self.__params = passed
            else:
                raise ValueError("Invalid parameters. Allowed: {}, Required: {}".
                                 format(self.__allowed_params, self.__required_params))

        elif self.__valchk__(passed, self.__allowed_params):
            self.__params = passed

        else:
            raise ValueError("Invalid parameters. Allowed: {}, Required: {}".
                             format(self.__allowed_params, self.__required_params))

    @property
    def filters(self):
        """Class *filters* property getter/setter

        Returns:
            The configured filter parameters (dict)

        Raises:
            ValueError: If invalid filter keys are passed to setter.
            ValueError: If invalid filter values are passed to setter.
            ValueError: If the setter is passed a non-dict object.
        """
        return self.__filters

    @filters.setter
    def filters(self, passed):
        if passed is None:
            self.__filters = passed

        elif self.__valchk__(passed,
                             self.__allowed_filters,
                             related=self.__allowed_params):
            self.__filters = passed

        else:
            raise ValueError("Invalid filter keys or values. Allowed: {}, Related: {}".
                             format(self.__allowed_filters, self.__allowed_params))

    @property
    def expands(self):
        """Class *expands* property getter/setter.

        Returns:
            The configured expands parameters (list)

        Raises:
            ValueError: If invalid expands values are passed to setter.
            ValueError: If the setter is passed a non-list object.

        """
        return self.__expands

    @expands.setter
    def expands(self, passed):
        if passed is None:
            self.__expands = passed

        elif isinstance(passed, list) and self.__valchk__(passed, self.__allowed_expands):
            self.__expands = passed

        else:
            raise ValueError("Invalid expand values. List required. Allowed: {}".format(self.__allowed_expands))

    @property
    def fields(self):
        """Class *fields* property getter/setter

        Returns:
            The configured fields to fetch from the API (list)

        Raises:
            ValueError: If invalid fields are passed to the setter.
            ValueError: If the setter is passed a non-list object.

        """
        return self.__fields

    @fields.setter
    def fields(self, passed):
        if passed is None:
            self.__fields = passed

        elif isinstance(passed, list) and self.__valchk__(passed, list(self.__allowed_params.keys())):
            self.__fields = passed

        else:
            raise ValueError("Invalid field selection. List Required. Allowed: {}".format(self.__allowed_params))

    @property
    def paging(self):
        """Class *paging* property getter/setter

        *paging* accepts a dict with two keys:
            * limit (int) - if omitted the API assumes '25'
            * offset (int)

        Use this to limit the number of calls made to the API for a given
        operation.

        Returns:
            The configured paging settings (dict)

        Raises:
            ValueError: If invalid paging options are passed to the setter.
            ValueError: If the setter is passed a non-dict object.

        """
        return self.__paging

    @paging.setter
    def paging(self, passed):
        if passed is None:
            self.__paging = passed

        elif self.__valchk__(passed, self.__allowed_paging):
            self.__paging = passed

        else:
            raise ValueError("Paging options are limited to integer values for 'limit' and 'offest'")

    @property
    def body(self):
        """Class *body* property getter/setter

        Returns:
            The configured body object (dict)

        Raises:
            TypeError: If the the setter is passed a dict that causes an error\
            from json.dumps()
        """
        return self.__body

    @body.setter
    def body(self, passed):
        try:
            self.__body = json.dumps(passed)

        except TypeError as e:
            raise TypeError("Invalid object passed to json.dumps(): {}".format(e))


class Unsupported(object):
    """Placeholder for currently unsupported data types

    Currently used as the data type for all timeuuid fields.
    """
    pass
