class Accounts:
    METHODS = ['get', 'put', 'patch', 'delete']

    def __init__(self, method):
        self.method = method

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, val):
        if val in self.METHODS:
            self.__method = val
        else:
            raise ValueError("Invalid Method, choose one of: {}".format(",".join(self.METHODS)))