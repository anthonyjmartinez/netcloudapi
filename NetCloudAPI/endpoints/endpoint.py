import re

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
                 expands=None):

        self.__base_url = base_url
        self.__allowed_meths = allowed_meths
        self.__allowed_params = allowed_params
        self.__required_params = required_params
        self.__allowed_filters = allowed_filters
        self.__allowed_expands = allowed_expands
        self.method = method
        self.params = params
        self.filters = filters
        self.expands = expands
        self.url = base_url

    @staticmethod
    def __valchk__(passed, allowed, required=None, related=None):
        if passed is None:
            return True

        elif isinstance(passed, str) and isinstance(allowed, str):
            if passed == allowed:
                return True
            else:
                return False

        elif isinstance(passed, str) and isinstance(allowed, list):
            if passed in allowed:
                return True
            else:
                return False

        elif isinstance(passed, list) and isinstance(allowed, list):
            pset = set(passed)
            aset = set(allowed)

            if not bool(pset.difference(aset)):
                return True
            else:
                return False

        elif isinstance(passed, dict) and isinstance(allowed, dict):
            pkset = set(list(passed.keys()))
            akset = set(list(allowed.keys()))
            err = 0

            if not bool(pkset.difference(akset)):
                if related is not None:
                    for k, v in passed.items():
                        if isinstance(v, allowed.get(k)):
                            rk = re.split("__", k)[0]
                            for i in v:
                                if isinstance(i, related.get(rk)):
                                    pass
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

            if err is 0:
                return True
            else:
                return False

        else:
            return False
