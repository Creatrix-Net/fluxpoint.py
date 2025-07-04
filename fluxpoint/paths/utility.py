from fluxpoint.vars import RequestTypes, datetimeformat
from fluxpoint.http import BaseHTTP

class Utility(BaseHTTP):
    """Utility Api endpoints documented in https://docs.fluxpoint.dev/api/endpoints/utility
    """

    def __init__(self, *args, **kwargs) -> None:
        self.__baseurl = '/utility'
        super().__init__(*args, **kwargs)

    async def unix2datetime(self, unixtime: int, format: str) -> str:
        """
        Get unix date/time format from timestamp number

        :raises TypeError: if format is invalid

        :param unixtime: Unix timestamp
        :type unixtime: int
        :param format: Format string
        :type format: str
        """
        if format not in datetimeformat:
            raise TypeError(f'Format must be one of {datetimeformat}')
        return (await self.request(RequestTypes.POST,f'{self.__baseurl}/unix-date', json={"unixtime":unixtime,"format":format})).get('content')

    async def discord2datetime(self, snowflake: int, format: str) -> str:
        """
        Get Discord date/time format from id number

        :raises TypeError: if format is invalid
        :param snowflake: Discord id
        :type snowflake: int
        :param format: Format string
        :type format: str
        """
        if format not in datetimeformat:
            raise TypeError(f'Format must be one of {datetimeformat}')
        return (await self.request(RequestTypes.POST, f'{self.__baseurl}/snowflake-date', json={"snowflake":snowflake,"format":format})).get('format')
