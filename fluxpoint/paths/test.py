from typing import Union, Dict
import io

from enum import Enum

from fluxpoint.errors import paramEnumValidCheck
from fluxpoint.vars import RequestTypes, ImageType
from fluxpoint.http import BaseHTTP

class Tests(BaseHTTP):
    """Test endpoint documented in https://docs.fluxpoint.dev/api/endpoints/test"""

    def __init__(self, *args, **kwargs) -> None:
        self.__baseurl = '/test'
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return '<Tests>'

    async def home(self) -> Enum:
        """
        Tests if the api is working

        :return: Tests Class
        :rtype: Enum
        """
        return Enum('Color', (await self.request(RequestTypes.GET, '',)))

    async def imagen(self, imgtype: ImageType = ImageType.JPG) -> Union[Dict, io.IOBase]:
        """Test the image generator

        :returns: The response from the server
        :rtype: Union[Dict, io.IOBase]
        """
        paramEnumValidCheck(imgtype, ImageType)
        return await self.request(
            RequestTypes.GET,
            f'{self.__baseurl}/image',
            params={"type":imgtype.value},
            return_bytes=True,
            return_json=False
        )

    async def gallery(self) ->  Dict:
        """ Test the gallery

        :returns: The response from the server
        :rtype: Dict
        """
        return await self.request(
            RequestTypes.GET,
            f'{self.__baseurl}/gallery',
        )

    async def error(self) -> Dict:
        """ Test the error

        :returns: The response from the server
        :rtype: Dict
        """
        return await self.request(RequestTypes.GET, f'{self.__baseurl}/error')

    async def json(self) -> Dict:
        """Test the JSON response

        :returns: The response from the server
        :rtype: Dict
        """
        return await self.request(RequestTypes.GET, f'{self.__baseurl}/json')