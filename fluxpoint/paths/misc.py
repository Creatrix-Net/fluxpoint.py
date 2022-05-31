from typing import Optional

from ..enums import RequestTypes
from ..http import BaseHTTP


class AboutUs:
    """A class which gives info from the json data of about us

    :param json_data: The json data from the api
    :type json_data: dict

    :Acessible Paramters:
        :id: [:class:`int`] ID of the person 
        :name: [:class:`str`] Discord username of the person 
        :token: [:class:`str`] Fluxpoint token of the person 
        :created: [:class:`datetime.datetime`] Account creation date
        :expire: [Optional[:class:`datetime.datetime`]] Expiration date
        :donator: [:class:`bool`] If the perso is a dontor in fluxpoint or not
        :owner: [:class:`bool`] If the person is owner or not
        :disabled: [:class:`bool`] If the acc is disabled or not
        :status: [:class:`str`] HTTP Status
        :code: [:class:`int`] HTTP Status code
        :message: [:class:`str`] Message returned by the api
    """

    def __init__(self, json_data: dict) -> None:
        for i in json_data:
            setattr(self, i.lower(), json_data[i])

    def __str__(self) -> str:
        return f"<AboutUs {self.name} ({self.id})>"


class MinecraftPingData:
    """A class which gives info from the json data of Minecraft server ping

    :param json_data: The json data from the api
    :type json_data: dict

    :Acessible Paramters:
        :online: [:class:`bool`] If the server is online or not
        :icon: [:class:`str`] URL of the server icon
        "motd": [:class:`str`] serverinfo
        :playersOnline: [:class:`int`] Amount of players online
        :playersMax: [:class:`int`] Max amount of players
        :version: [:class:`str`] Minecraft version
        :fullQuery: [:class:`bool`] If the query was full or not
        :players: [Optional[:class:`list`]] List of players
        :status: [:class:`str`] HTTP Status
        :code: [:class:`int`] HTTP Status code
        :message: [:class:`str`] Message returned by the api
    """

    def __init__(self, json_data: dict) -> None:
        for i in json_data:
            setattr(self, i.lower(), json_data[i])

    def __str__(self) -> str:
        return '<Minecraft Server Ping Data>'

    def __repr__(self) -> str:
        return '<Minecraft Server Ping Data>'


class Misc(BaseHTTP):
    """NSFW Api endpoints documented in https://bluedocs.page/fluxpoint-api/misc"""

    def __str__(self) -> str:
        return '<MISC>'

    async def me(self) -> AboutUs:
        """Get info on the current user

        :return: The class containing all the information about the current user
        :rtype: AboutUs
        """
        return AboutUs(await self.request(RequestTypes.GET, 'me'))

    async def mc_ping(self, host: str, port: Optional[int] = 25565) -> MinecraftPingData:
        """Ping a minecraft server

        :param host: The hostname of the server
        :type host: str
        :param port: The port of the server
        :type port: int
        """
        return MinecraftPingData(await self.request(RequestTypes.GET, f'mc/ping?host={host}&{port}'))  # skipcq: FLK-E50
