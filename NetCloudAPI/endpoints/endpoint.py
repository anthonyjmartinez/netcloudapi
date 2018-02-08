class Endpoint(object):
    def __init__(self,
                 allowed_meths=None,
                 allowed_params=None,
                 required_params=None,
                 allowed_filters=None,
                 allowed_expands=None,
                 method=None,
                 params=None,
                 filters=None,
                 expands=None):

        self.__allowed_meths = allowed_meths
        self.__allowed_params = allowed_params
        self.__required_params = required_params
        self.__allowed_filters = allowed_filters
        self.__allowed_expands = allowed_expands
        self.method = method
        self.params = params
        self.filters = filters
        self.expands = expands