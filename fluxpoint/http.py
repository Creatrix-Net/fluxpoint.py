import asyncio
import io
from typing import Optional, Union

import aiohttp
from yarl import URL

from . import __version__
from .vars import RequestTypes
from .errors import *


class BaseHTTP:
    """The base class for making http requests

    :param api_token: The fluxpoint api token https://fluxpoint.dev/api/access
    :type api_token: str
    """
    __slots__ = ["api_token", "__user_agent"]

    def __init__(self, api_token: str) -> None:
        self.api_token: str = api_token
        self.__user_agent: str = f"fluxpointpy/{__version__}"

    async def request(
        self,
        method: RequestTypes,
        endpoint: str,
        json: Optional[dict] = None,
        headers: Optional[dict] = None,
        _base_url: Optional[Union[str, URL]] = 'https://api.fluxpoint.dev/',
        retry: bool = True,
        return_json: bool = True,
        return_bytes: bool = False,
        retry_times: int = 1
    ) -> Union[aiohttp.ClientResponse, dict, io.IOBase]:
        """Makes an API request

        :raises RateLimited: When the 429 response is returned
        :raises WrongReturnType: When the :exc:`UnicodeDecodeError` is raised
        :raises ParameterError: When the 400 response is returned
        :raises Unauthorised: When the 401 response is returned
        :raises ApiError: When the 500 response is returned
        :raises HttpException: For the other and generall http exceptions
        :return: Bytes data for the image
        :rtype: Union[aiohttp.ClientResponse, dict, io.IOBase]
        """
        if json is None:
            json = {}
        __base_url: str = _base_url if _base_url.endswith('/') else _base_url.strip() + '/' # type: ignore
        headers = {} if not headers else headers

        headers["Authorization"] = self.api_token
        headers["User-Agent"] = self.__user_agent

        async with aiohttp.ClientSession() as session:
            async with session.request(str(method.name).upper(), f'{__base_url}{str(endpoint)}', headers=headers, json=json) as response:
                if response.status == 429:
                    if not retry:
                        raise RateLimited("Too many requests, try again later")
                    await asyncio.sleep(response.headers.get('Retry-After'))
                    return await self.request(method, endpoint, json, headers, retry=retry_times <= 10, retry_times=retry_times+1)

                try:
                    result = await response.json(content_type="application/json") if return_json else (await response.read()if return_bytes else response)
                    if response.status == 200:
                        return result
                    result = await response.json(content_type="application/json") if not isinstance(result, dict) else result
                except UnicodeDecodeError:
                    raise WrongReturnType("Wrong return type is given")

                if response.status == 400:
                    raise ParameterError(result.get("message")) # type: ignore

                if response.status == 401:
                    raise Unauthorised(result.get("message")) # type: ignore

                if response.status == 500:
                    raise ApiError(result.get("message")) # type: ignore

                raise HttpException(response.status, result) # type: ignore
