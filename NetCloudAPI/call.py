"""**NetCloudAPI.call is the module that provides the NetCloudAPI.call() function.**

NetCloudAPI.call.call() is imported by the NetCloudAPI package.
"""

from requests import Session

ERROR_CODES = {"Found (Redirected)": 302,
               "Bad Request": 400,
               "Unauthorized": 401,
               "Forbidden": 403,
               "Not Found": 404,
               "Method Not Allowed": 405,
               "Conflict": 409,
               "Too Many Requests": 429,
               "Internal Server Error": 500,
               "Bad Gateway": 502}

ACCEPTED_CODES = {"OK": 200,
                  "Created": 201,
                  "Accepted": 202,
                  "No Content": 204}


def call(request, session=None):
    """Executes remote API calls and returns JSON response data.

    Cradlepoint ECM API calls are made based on the passed requests.PreparedRequest
    object created by NetCloudAPI.req. The API response is analyzed for content
    signaling the success or failure of the request, as well as the need to make
    subsequent requests in order to retrieve all necessary data. This function
    will continue making requests and building the full JSON data object until
    all requested data has been retrieved.

    Args:
        request (requests.PreparedRequest): The successful results from NetCloudAPI.req().
        session (requests.Session, optional): An optional requests.Session object

    Returns:
        JSON object with the appropriate status code and data payload(s).

    """
    def _resp_handler(request, session, response):

        resp = response.json()
        if response.status_code in list(ERROR_CODES.values()):
            resp.update({"NetCloudAPI Error": response.status_code})

        elif resp["meta"]["next"]:
            request.url = resp["meta"]["next"]
            while request.url:
                r_tmp = session.send(request).json()
                for row in r_tmp["data"]:
                    resp["data"].append(row)
                request.url = _next_url(r_tmp)

        return resp

    def _next_url(resp):

        if resp["meta"]["next"]:
            url = resp["meta"]["next"]
        else:
            url = None

        return url

    if session is not None:
        session.headers = request.headers
        resp_i = session.send(request)
        resp_f = _resp_handler(request, session, resp_i)

    else:
        with Session() as s:
            s.headers = request.headers
            resp_i = s.send(request)
            resp_f = _resp_handler(request, s, resp_i)

    return resp_f
