from __future__ import annotations

import asyncio
from typing import Awaitable, Callable, Coroutine, Optional, Union

import aiohttp
from yarl import URL

from . import __version__
from .enums import RequestTypes


class RateLimited(Exception):
    """Ratelimited expection type
    """
    __slots__ = ['status', 'retry_after', 'error', "request_obj", "retry"]

    def __init__(self, request_obj: Optional[Union[Awaitable, Coroutine, Callable]] = None, retry: bool = False) -> None:
        super().__init__(request_obj, retry)
        self.request_obj = request_obj
        self.status: int = 429
        self.retry_after: Optional[int] = None
        self.error: Optional[str] = None
        self.retry = retry

    def __str__(self) -> str:
        return f'<RateLimited 429 ,timeout={self.retry_after}, error={self.error}>'


class BaseHTTP:
    __slots__ = ["api_token"]

    def __init__(self, api_token: str) -> None:
        self.api_token: str = api_token
        self.__user_agent: str = f"fluxpoint/{__version__}"

    async def request(
        self,
        method: RequestTypes,
        endpoint: str,
        json: Optional[dict] = None,
        headers: Optional[dict] = None,
        _base_url: Optional[Union[str, URL]] = 'https://api.fluxpoint.dev/',
        retry: bool = True,
        return_json: bool = True,
        retry_times: int = 1
    ) -> Union[Awaitable, Coroutine, Callable, dict]:
        """Makes an API request"""
        if json is None:
            json = {}
        __base_url: str = _base_url if _base_url.endswith(
            '/') else _base_url.strip() + '/'
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
                    result = await response.json(content_type="application/json") if return_json else await response
                except Exception:
                    try:
                        raise Exception((await response.json(content_type="application/json"))["message"])
                    except:
                        raise Exception(await response.text())
        if response.status == 200:
            return result if return_json else await response
        try:
            raise Exception((await response.json(content_type="application/json"))["message"])
        except Exception as e:
            raise Exception(await response.text())
