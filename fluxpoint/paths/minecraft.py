from fluxpoint.http import BaseHTTP
from fluxpoint.vars import RequestTypes
from typing import Optional

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


class Minecraft(BaseHTTP):
    def __init__(self, *args, **kwargs) -> None:
        self.__baseurl = '/mc'
        super().__init__(*args, **kwargs)

    async def ping(self, host: str, port: Optional[int] = 25565, icon: bool = False) -> MinecraftPingData:
        """Ping a minecraft server

        :param host: The hostname of the server
        :type host: str
        :param port: The port of the server
        :type port: int
        :param icon: Whether you want server icon raw data or not
        :type icon: boolean
        """
        return MinecraftPingData(await self.request(RequestTypes.GET, f'{self.__baseurl}/ping?host={host}&port={port}&icon={"true" if icon else "false"}'))  # skipcq: FLK-E50

    async def lookup(self, player: str) -> MinecraftPingData:
        """
        Get a Minecraft player UUID from player name

        :param player: The name of the player
        :type player: str
        """

