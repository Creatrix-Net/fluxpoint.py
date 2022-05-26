from typing import List, Optional, Union

from colour import Color
from yarl import URL

from ..enums import RequestTypes
from ..http import BaseHTTP


class WelcomeConfig:
    def __init__(
        self,
        username: str,
        avatar: Union[URL, str],
        background: str,
        members: Optional[str] = None,
        icon: Optional[str] = None,
        banner: Optional[str] = None,
        color_welcome: Optional[Union[Color, str]] = None,
        color_username: Optional[Union[Color, str]] = None,
        color_members: Optional[Union[Color, str]] = None,
    ) -> None:
        self.username = username
        self.avatar = avatar
        self.background = background
        self.members = members

        self.banner = banner
        self.icon = icon

        self.color_members = color_members
        if self.color_members is not None:
            self.color_members = Color(self.color_members) if isinstance(
                self.color_members, str) else self.color_members
        self.color_username = color_username
        if self.color_username is not None:
            self.color_username = Color(self.color_username) if isinstance(
                self.color_username, str) else self.color_username
        self.color_welcome = color_welcome
        if self.color_welcome is not None:
            self.color_welcome = Color(self.color_welcome) if isinstance(
                self.color_welcome, str) else self.color_welcome


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
