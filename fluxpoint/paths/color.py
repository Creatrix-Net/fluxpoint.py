from typing import Optional, AsyncGenerator

from fluxpoint.vars import RequestTypes
from fluxpoint.http import BaseHTTP

class ResultantColor:
    """
    Data of Color Returned by API

    Attributes
    :param hex: Hexadecimal representation of the color
    :type hex: str
    :param r: The red value of the color
    :type r: int
    :param g: The green value of the color
    :type g: int
    :param b: The blue value of the color
    :type b: int
    :param name: The name of the color
    :type name: str
    """
    def __init__(self, *args, **kwargs) -> None:
        data = kwargs.get("data")
        self.hex = data.get("hex")
        self.r = int(data.get("r",0))
        self.g = int(data.get("g",0))
        self.b = int(data.get("b",0))
        self.name = data.get("name")

class Color(BaseHTTP):
    """
    Color Api endpoints documented in https://docs.fluxpoint.dev/api/endpoints/color
    """

    def __init__(self, *args, **kwargs) -> None:
        self.__baseurl = '/color'
        super().__init__(*args, **kwargs)

    async def random(self) -> ResultantColor:
        """
        Get a random color

        :return: A random color
        :rtype: :class:`ResultantColor`
        """
        return ResultantColor(data=await self.request(RequestTypes.GET,f'{self.__baseurl}/random'))

    async def info(self, name: Optional[str] = None, hexvalue: Optional[str] = None, rgb: Optional[str] = None) -> AsyncGenerator[ResultantColor]:
        """
        Get color info from name, hex or rgb value.

        :param name: The name of the color
        :type name: :class:`Optional[str]`
        :param hexvalue: The hexadecimal representation of the color
        :type hexvalue: :class:`Optional[str]`
        :param rgb: The rgb value of the color
        :type rgb: :class:`Optional[str]`

        :return: A generator of colors information as passed
        :rtype: :class:`AsyncGenerator[ResultantColor]`

          .. note::
            If all parameters are passed i.e. ``name``, ``hexvalue``, ``rgb``` then the generator would go in the order of ``name``, ``hexvalue``, ``rgb``
        """
        if all(v is None for v in [name, hexvalue, rgb]):
            raise ValueError("At least of the parameters are required (name, hexvalue, rgb)")
        if bool(name):
            yield ResultantColor(data=await self.request(RequestTypes.GET,f'{self.__baseurl}/info',params={"name": name}))
        if bool(hexvalue):
            yield ResultantColor(data=await self.request(RequestTypes.GET, f'{self.__baseurl}/info',params={"hex": hexvalue}))
        if bool(rgb):
            yield ResultantColor(data=await self.request(RequestTypes.GET, f'{self.__baseurl}/info',params={"rgb": rgb}))