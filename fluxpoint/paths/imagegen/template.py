from typing import List, Optional, Union, Dict, Tuple
import io

from yarl import URL

from fluxpoint.vars import RequestTypes
from fluxpoint.http import BaseHTTP
from fluxpoint.errors import InvalidFeature


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
        :type color_welcome: Optional[str], optional
        :param color_username: Colour of the username text, defaults to None
        :type color_username: Optional[str], optional
        :param color_members: Colour of the member text, defaults to None
        :type color_members: Optional[str], optional

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
        color_welcome: Optional[str] = None,
        color_username: Optional[str] = None,
        color_members: Optional[str] = None,
    ) -> None:
        self.username = username
        self.avatar = avatar
        self.background = background
        self.members = members

        self.banner = banner
        self.icon = icon

        self.color_members = color_members
        self.color_username = color_username
        self.color_welcome = color_welcome

    def __str__(self) -> str:
        return f'<WelcomeConfig username={self.username} avatar={self.avatar} background={self.background}>'

    def to_dict(self) -> dict:
        """A helper function to convert the class parameters to a dictionary"""
        return_dummy_dict = {
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
        return_dict = {}
        for i in return_dummy_dict:
            if return_dummy_dict[i] is not None:
                return_dict[i] = return_dummy_dict[i]
        return return_dict


class Template(BaseHTTP):
    """Template Images Api endpoints documented in https://docs.fluxpoint.dev/api/endpoints/image-gen/templates"""

    def __init__(self, *args, **kwargs) -> None:
        self.__listbaseurl = '/list'
        self.__baseurl = '/gen'
        super().__init__(*args, **kwargs)

    async def __welcome_icons(self) -> Union[List[str], Tuple[str]]:
        """Get a list of all the welcome icons

        :return: A list of all the welcome icons
        :rtype: Union[list, tuple]
        """
        return (await self.request(RequestTypes.GET, f'{self.__listbaseurl}/icons')).get('list')  # skipcq: TYP-005

    async def __welcome_banner(self) -> Union[List[str], Tuple[str]]:
        """Get a list of all the welcome banners

        :return: A list of all the welcome banners
        :rtype: Union[list, tuple]
        """
        return (await self.request(RequestTypes.GET, f'{self.__listbaseurl}/banners')).get('list')  # skipcq: TYP-005

    async def welcome(self, config: WelcomeConfig) -> Union[Dict, io.IOBase]:
        """Create a welcome image

        :raises InvalidFeature: When ``banner`` or ``icons`` parameters in ``config`` are invalid

        :param config: A WelcomeConfig object
        :type config: WelcomeConfig
        :return: The image as a byte array
        :rtype: Union[dict, io.IOBase]
        """
        if (
            config.banner is not None
            and config.banner.lower() not in list(map(lambda x: x.lower(), await self.__welcome_banner()))
        ):
            raise InvalidFeature(f'Banner {config.banner} not found')
        if (
            config.icon is not None
            and config.icon.lower() not in list(map(lambda x: x.lower(), await self.__welcome_icons()))
        ):
            raise InvalidFeature(f'Icon {config.icon} not found')
        return await self.request(RequestTypes.POST, f'{self.__baseurl}/welcome', json=config.to_dict(), return_bytes=True, return_json=False)
