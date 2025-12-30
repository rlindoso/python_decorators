# Python Decorators Study Project

This repository is a **study project focused on Python decorators**, showing how they can be used for:
- Cross-cutting concerns (execution time, logging)
- HTTP API consumption abstraction
- Cleaner and reusable code

The project is intentionally simple and educational, but already follows patterns commonly seen in real-world backend code.

---

## Project Structure

```

.
├── decorators.py
├── api_decorator.py
├── api.py
└── README.md

````

---

# 1. decorators.py

## Purpose

This file demonstrates a **basic function decorator** used to:
- Inspect function metadata
- Log positional and named arguments
- Measure execution time

It is a pure Python example with **no external dependencies**, useful for understanding how decorators work internally.

---

## How it works

### Decorator: `measure_time`

```python
def measure_time(func):
    def wrapper(*args, **kwargs):
        ...
        result = func(*args, **kwargs)
        ...
        return result
    return wrapper
````

What it does:

* Wraps any function
* Logs:

  * Function name
  * Positional arguments (`args`)
  * Named arguments (`kwargs`)
* Measures execution time using `time.time()`

---

### Decorated function example

```python
@measure_time
def proccess(param1: int, param2: str):
    time.sleep(param1)
    print(param2)
```

Execution:

```python
proccess(param1=1, param2="valor2")
```

Output includes:

* Function name
* Arguments
* Start and end timestamps
* Total execution time

---

## How to run

```bash
python decorators.py
```

No additional libraries are required.

---

## Possible Improvements

* Use `functools.wraps` to preserve metadata (name, docstring)
* Replace `print` with Python `logging`
* Add support for async functions
* Export execution metrics to a monitoring system

---

# 2. api_decorator.py

## Purpose

This file introduces a **decorator-based HTTP client abstraction**.

The goal is to:

* Centralize HTTP GET logic
* Automatically build URLs with:

  * Path parameters
  * Query parameters
* Measure request execution time
* Inject `request` and `response` objects into the decorated function

This mimics patterns used in:

* API SDKs
* HTTP clients
* Service integration layers

---

## How it works

### Decorator: `get(url, headers=None)`

```python
def get(url, headers=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ...
            response = requests.request(...)
            return func(request_info, response, *args, **kwargs)
        return wrapper
    return decorator
```

Key responsibilities:

* Accepts a **base URL**
* Extracts:

  * `param` → path parameter
  * `query_params` → query string parameters
* Builds the final URL
* Executes the HTTP request using `requests`
* Measures execution time
* Passes `request_info` and `response` to the decorated function

---

### URL construction logic

```python
path_param = kwargs.get("param", "")
query_params = kwargs.get("query_params", {})

query_string = f"?{urlencode(query_params)}" if query_params else ""
full_url = f"{url}{path_param}{query_string}"
```

This allows calls like:

```python
get_pokemon(param="pikachu")
get_pokemons_paginated(query_params={"offset": 0, "limit": 5})
```

---

## Dependencies

Install required library:

```bash
pip install requests
```

---

## Possible Improvements

* Support other HTTP methods (`POST`, `PUT`, `DELETE`)
* Add timeout and retry logic
* Handle HTTP errors with exceptions
* Use `inspect.signature` for safer argument binding
* Add authentication support (Bearer token, API key)
* Convert this decorator into a reusable HTTP client class

---

# 3. api.py

## Purpose

This file demonstrates **real usage** of the `@get` decorator to consume a public API:

* [PokeAPI](https://pokeapi.co)

It shows:

* How to define API functions
* How the decorator injects `request` and `response`
* How to consume paginated endpoints

---

## How it works

### Base URL

```python
base_url = "https://pokeapi.co/api/v2/"
```

---

### Get a single Pokémon

```python
@get(f"{base_url}pokemon/")
def get_pokemon(request: Request, response: Response, param: str):
    return response, request
```

Call:

```python
response, request = get_pokemon(param="pikachu")
```

Generated URL:

```
https://pokeapi.co/api/v2/pokemon/pikachu
```

---

### Get all Pokémon species

```python
@get(f"{base_url}pokemon-species/")
def get_pokemons(request: Request, response: Response):
    return response, request
```

---

### Paginated request

```python
@get(f"{base_url}pokemon-species/")
def get_pokemons_paginated(request: Request, response: Response, query_params: str):
    return response, request
```

Call:

```python
response, request = get_pokemons_paginated(
    query_params={"offset": 0, "limit": 5}
)
```

Generated URL:

```
https://pokeapi.co/api/v2/pokemon-species/?offset=0&limit=5
```

---

## How to run

```bash
pip install requests
python api.py
```

---

## Output examples

* Request URL
* HTTP method
* Status code
* JSON response (pretty printed)
* Total items count
* Items per page

---

## Possible Improvements

* Separate API calls from execution logic (CLI vs library)
* Return parsed domain objects instead of raw JSON
* Add async support (`aiohttp`)
* Introduce response validation
* Add caching
* Create a unified `HttpClient` abstraction
* Add unit tests with mocked HTTP responses

---

# Final Notes

This project demonstrates:

* Core decorator mechanics
* Practical decorator usage beyond toy examples
* How Python decorators can simplify API integrations

It is an excellent foundation for:

* Building SDKs
* Creating internal service clients
* Learning advanced Python patterns

Feel free to fork, extend, and refactor 🚀
