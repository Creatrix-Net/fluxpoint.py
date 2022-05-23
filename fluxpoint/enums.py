import enum

@enum.unique
class RequestTypes(enum.IntEnum):
    """Different requests types for the http request"""
    delete = 0
    get = 1
    head = 2
    patch = 3
    put = 4
    post = 5
 
