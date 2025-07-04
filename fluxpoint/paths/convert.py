from fluxpoint.vars import RequestTypes
from fluxpoint.http import BaseHTTP

class Convert(BaseHTTP):
    """Convert Api endpoints documented in https://docs.fluxpoint.dev/api/endpoints/convert
    """

    def __init__(self, *args, **kwargs) -> None:
        self.__baseurl = '/convert'
        super().__init__(*args, **kwargs)


