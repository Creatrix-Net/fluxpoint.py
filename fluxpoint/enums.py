import enum

@enum.unique
class RequestTypes(enum.IntEnum):
    delete = 0
    get = 1
    head = 2
    patch = 3
    put = 4
    post = 5
 
