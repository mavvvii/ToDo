### Status: Proposed
### Date: 2025-07-03
### Deciders:
- #### Hubert Kwiatek
### Consulted: -
- #### -
### Informed: -
- #### -

---

# ADR-0002: Backend Interface Selection – ASGI vs WSGI

## Context and Problem Statement

Which backend interface should we choose ASGI or WSGI ?

## Decision Drivers

1. Compatibility with the Django framework
2. Support for asynchronous features in the future 

## Considered Options

1. **WSGI** (Web Server Gateway Interface)  
2. **ASGI** (Asynchronous Server Gateway Interface)

## Decision Outcome

We have chosen ASGI because it allows us to run the server with Uvicorn and supports both synchronous and asynchronous workloads.

## Consequences

* Good, because enables us to start with synchronous HTTP and introduce asynchronous features (e.g., WebSockets, background tasks) later.
* Bad, because it requires Django version ≥ 3.0.

## Validation

This decision is driven by the growing popularity of ASGI over WSGI. ASGI provides a clear upgrade path: we can begin with standard synchronous HTTP and gradually add asynchronous capabilities as needed.

## Options  - Pros and Cons

1. **WSGI**  
    **Pros:** 
     - Included in Django’s default project template. 
    **Cons:**
     - Only handles synchronous HTTP requests.
     - Migrating from WSGI to ASGI later may incur additional time and cost. 
2. **ASGI**
    **Pros:**
     - Include both synchronous and asynchronous protocols (HTTP, WebSockets, ...)
     - Increasingly adopted by the community.
     - Simple to implement with Uvicorn or other ASGI servers.  
    **Cons:**
     - Requires Django 3.0 or newer.  

## More Information

This ADR should be implemented as soon as we commence our backend architecture.

[ASGI DOCS](https://asgi.readthedocs.io/en/latest/)

[WSGI DOCS](https://wsgi.readthedocs.io/en/latest/)

