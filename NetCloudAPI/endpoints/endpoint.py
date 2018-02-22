import re
import json
from datetime import datetime


class Endpoint(object):
    def __init__(self,
                 base_url=None,
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

        self.__base_url = base_url
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
        self.url = base_url

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
                        for k, v in passed.item():
                            if isinstance(v, allowed(k)):
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
    def url(self):
        return self.__url

    @url.setter
    def url(self, passed):
        if passed is None:
            self.__url = passed

        elif self.__valchk__(passed, self.__base_url):
            self.__url = passed

        else:
            raise ValueError("The URL is protected and must be {}"
                             .format(self.__base_url))

    @property
    def method(self):
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
        return self.__expands

    @expands.setter
    def expands(self, passed):
        if passed is None:
            self.__expands = passed

        elif self.__valchk__(passed, self.__allowed_expands):
            self.__expands = passed

        else:
            raise ValueError("Invalid expands values. Allowed: {}".format(self.__allowed_expands))

    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, passed):
        if passed is None:
            self.__fields = passed

        elif self.__valchk__(passed, self.__allowed_params):
            self.__fields = passed

        else:
            raise ValueError("Invalid field selection. Allowed: {}".format(self.__allowed_params))

    @property
    def paging(self):
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
        return self.__body

    @body.setter
    def body(self, passed):
        try:
            self.__body = json.dumps(passed)

        except TypeError as e:
            raise TypeError("Invalid object passed to json.dumps(): {}".format(e))


class Unsupported:
    """Placeholder for currently unsupported data types"""
    pass