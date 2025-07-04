from typing import Union, List, Tuple

from fluxpoint.vars import RequestTypes
from fluxpoint.http import BaseHTTP


class Lists(BaseHTTP):
    """Lists Api endpoints documented in https://docs.fluxpoint.dev/api/endpoints/list
    """

    def __init__(self, *args, **kwargs) -> None:
        self.__baseurl = '/list'
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return '<Lists>'

    async def icons(self) -> Union[List[str], Tuple[str]]:
        """Get a list of all the welcome icons

        :return: A list of all the welcome icons
        :rtype: Union[list, tuple]
        """
        return (await self.request(RequestTypes.GET, f'{self.__baseurl}/icons')).get('list')  # skipcq: TYP-005

    async def banner(self) -> Union[List[str], Tuple[str]]:
        """Get a list of all the welcome banners

        :return: A list of all the welcome banners
        :rtype: Union[list, tuple]
        """
        return (await self.request(RequestTypes.GET, f'{self.__baseurl}/banners')).get('list')  # skipcq: TYP-005

    async def fonts(self) -> Union[List[str], Tuple[str]]:
        """Get a list of all the fonts

        :return: A list of all the fonts
        :rtype: Union[list, tuple]
        """
        return (await self.request(RequestTypes.GET, f'{self.__baseurl}/fonts')).get('list')  # skipcq: TYP-005