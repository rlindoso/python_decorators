import requests
import time
from functools import wraps
from urllib.parse import urlencode

def get(url, headers=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            path_param = kwargs.get("param", "")
            query_params = kwargs.get("query_params", {})

            query_string = f"?{urlencode(query_params)}" if query_params else ""

            method = "GET"
            start = time.time()

            full_url = f"{url}{path_param}{query_string}"

            response = requests.request(
                method=method,
                url=full_url,
                headers=headers
            )

            end = time.time()

            print(f"Execution time: {end - start:.4f} seconds")

            request_info = {
                "url": full_url,
                "method": method,
                "headers": headers
            }

            return func(request_info, response, *args, **kwargs)

        return wrapper
    return decorator
