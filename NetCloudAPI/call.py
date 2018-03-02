# Responsible for executing the request object returned by req.py
# must return the full set of responses from the endpoint
# and should be prepared to loop when method = GET and the response["meta"]["next"]
# value is not null. All of the response objects should be appended to a single
# iterable data structure that could be easily ingested by Pandas or another
# statistical analysis package.
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
    def resp_handler(request, session, response):
        resp = response.json()
        if response.status_code in list(ERROR_CODES.values()):
            resp.update({"NetCloudAPI Error": response.status_code})

        elif resp["meta"]["next"]:
            url = resp["meta"]["next"]
            while url:
                r_tmp = session.get(url, headers=request.headers).json()
                for row in r_tmp["data"]:
                    resp["data"].append(row)
                url = next_url(r_tmp)

        return resp

    def next_url(resp):
        if resp["meta"]["next"]:
            url = resp["meta"]["next"]
        else:
            url = None

        return url

    if session is not None:
        resp_i = session.send(request)
        resp_f = resp_handler(request, session, resp_i)

    else:
        with Session() as s:
            resp_i = s.send(request)
            resp_f = resp_handler(request, session, resp_i)
            # print(resp.status_code, resp.json())

    return resp_f