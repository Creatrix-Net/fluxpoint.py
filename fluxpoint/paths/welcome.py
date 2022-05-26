from typing import List, Optional, Union, Dict, Tuple
import io

from colour import Color
from yarl import URL

from ..enums import RequestTypes
from ..http import BaseHTTP


class WelcomeConfig:
    """Class to configure the welcome image parameters

        :param username: Discord username
        :type username: str
        :param avatar: avatar url
        :type avatar: Union[URL, str]
        :param background: Backgroud color code
        :type background: str
        :param members: Members no tet, defaults to None
        :type members: Optional[str], optional
        :param icon: Icon to use, defaults to None
        :type icon: Optional[str], optional
        :param banner: Banner to be put at background, defaults to None
        :type banner: Optional[str], optional
        :param color_welcome: Colour of the welcome text, defaults to None
        :type color_welcome: Optional[Union[Color, str]], optional
        :param color_username: Colour of the username text, defaults to None
        :type color_username: Optional[Union[Color, str]], optional
        :param color_members: Colour of the member text, defaults to None
        :type color_members: Optional[Union[Color, str]], optional

        .. note::
            The ``color`` parameters are optional, if you don't want to use a color, just pass ``None``
        
        .. warning::
            The ``banner`` and ``icon`` parameters evauation would be done when :func:`Welcome.welcome` is called.
        """    
    
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
            self.color_members = Color(self.color_members) if isinstance(self.color_members, str) else self.color_members
        self.color_username = color_username
        if self.color_username is not None:
            self.color_username = Color(self.color_username) if isinstance(self.color_username, str) else self.color_username
        self.color_welcome = color_welcome
        if self.color_welcome is not None:
            self.color_welcome = Color(self.color_welcome) if isinstance(self.color_welcome, str) else self.color_welcome
    
    def __str__(self) -> str:
        return f'<WelcomeConfig username={self.username} avatar={self.avatar} background={self.background}>'
    
    def to_dict(self) -> dict:
        """A helper function to convert the class parameters to a dictionary"""
        return {
            'username': self.username,
            'avatar': self.avatar,
            'background': self.background,
            'members': self.members,
            'banner': self.banner,
            'icon': self.icon,
            'color_members': self.color_members,
            'color_username': self.color_username,
            'color_welcome': self.color_welcome,
        }


class Welcome(BaseHTTP):
    """Welcome Images Api endpoints documented in https://bluedocs.page/fluxpoint-api/welcome"""

    async def welcome_icons(self) -> Union[List[str], Tuple[str]]:
        """Get a list of all the welcome icons

        :return: A list of all the welcome icons
        :rtype: Union[list, tuple]
        """
        return (await self.request(RequestTypes.GET, 'list/icons')).get('list')

    async def welcome_banner(self) -> Union[List[str], Tuple[str]]:
        """Get a list of all the welcome banners

        :return: A list of all the welcome banners
        :rtype: Union[list, tuple]
        """
        return (await self.request(RequestTypes.GET, 'list/banners')).get('list')
    
    async def welcome(self, config: WelcomeConfig) -> Union[Dict, io.IOBase]:
        """Create a welcome image

        :raises ValueError: When ``banner`` or ``icons`` parameters in ``config`` are invalid

        :param config: A WelcomeConfig object
        :type config: WelcomeConfig
        :return: The image as a byte array
        :rtype: Union[dict, io.IOBase]
        """

        if config.banner is not None:
            if config.banner.lower() not in list(map(lambda x: x.lower(), await self.welcome_banner())):
                raise ValueError(f'Banner {config.banner} not found')
        if config.icon is not None:
            if config.icon.lower() not in list(map(lambda x: x.lower(), await self.welcome_icons())):
                raise ValueError(f'Icon {config.icon} not found')
        return await self.request(RequestTypes.POST, '/gen/welcome', json=config.to_dict())
