from __future__ import annotations

import aiohttp
from typing import Optional, Union, Awaitable, Coroutine
from ..enums import RequestTypes
from .. import __version__


class BaseHTTP:    
    __slots__ = ['ver', "api_token", "user_agent"]
    
    def __init__(self, api_token):
        self.api_token = api_token
        self.user_agent = f"fluxpoint/{__version__}"       
    
    async def request(
        self, 
        method: RequestTypes, 
        endpoint: str,
        json: Optional[dict], 
        headers: Optional[dict], 
        retry: bool = True
    ) -> Union[Awaitable, Coroutine]:
        """Makes a API request"""
        headers = {} if not headers else headers
                
        headers["Authorization"] = self.api_token
        headers["User-Agent"] = self.user_agent
        
        async with aiohttp.ClientSession() as session:
            with session.request(str(method.name).upper(), f'https://api.fluxpoint.dev/{str(endpoint)}',headers=headers,json=json) as response:
                return await response