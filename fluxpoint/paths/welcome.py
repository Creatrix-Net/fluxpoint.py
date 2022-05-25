from typing import List, Optional, Union

from yarl import URL

from ..enums import RequestTypes
from ..http import BaseHTTP


class WelcomeConfig:
    def __init__(
        self,
        username:str, 
        avatar:Union[URL, str], 
        background: str, 
        members: Optional[str] = None, 
        icon: Optional[str]= None, 
        banner: Optional[str]= None,
    ) -> None:
        self.username = username
        self.avatar = avatar
        self.background = background
        self.members = members

        self.banner = banner
        self.icon = icon

class Welcome(BaseHTTP):
    """Welcome Images Api endpoints documented in https://bluedocs.page/fluxpoint-api/welcome"""

    async def welcome_icons(self) -> List[str]:
        """Get a list of all the welcome icons
        
        :return: A list of all the welcome icons
        :rtype: list
        """
        return (await self.request(RequestTypes.GET, 'list/icons')).get('list')
    
    async def welcome_banner(self) -> List[str]:
        """Get a list of all the welcome banners
        
        :return: A list of all the welcome banners
        :rtype: list
        """
        return (await self.request(RequestTypes.GET, 'list/banners')).get('list')
