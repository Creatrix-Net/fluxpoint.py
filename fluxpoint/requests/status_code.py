from __future__ import annotations
from typing import Awaitable, Coroutine, Optional, Union, Callable
    
class RateLimited(Exception):
    __slots__ = ['status', 'retry_after', 'error', "request_obj", "retry"]
    
    def __init__(self, request_obj: Optional[Union[Awaitable, Coroutine, Callable]], retry: bool = False):
        self.request_obj = request_obj
        self.status: int = 429
        self.retry_after: int = None
        self.error: str = None
        self.retry = retry
    
    def __str__(self):
        return f'<RateLimited 429 ,timeout={self.retry_after}, error={self.error}>'

class Success:
    __slots__=['http_status','json',]
    def __init__(self, done: Optional[str], reason: Optional[str], json: Optional[dict]):
        self.done = done
        self.reason = reason
        self.http_status = 200
        self.json = json
    
    @classmethod
    def dict_to_object(self):
        if self.json:
            self.done = self.json.get('done')
            self.reason = self.json.get('reason')
            return self
        raise LookupError('No json data was gicen')
    
    @classmethod
    def to_dict(self):
        """Converts this embed object into a dict."""
        result = {
            key[1:]: getattr(self, key)
            for key in self.__slots__
            if key[0] == '_' and hasattr(self, key)
        }
        try:
            colour = result.pop('json')
        except KeyError:
            pass
        return result 


class Error:
    pass