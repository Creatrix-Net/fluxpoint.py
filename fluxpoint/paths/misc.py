from typing import Optional

from fluxpoint.vars import RequestTypes
from fluxpoint.http import BaseHTTP


class AboutUs:
    """A class which gives info from the json data of about us

    :param json_data: The json data from the api
    :type json_data: dict

    :Acessible Paramters:
        :id: [:class:`int`] ID of the person
        :created: [:class:`datetime.datetime`] Account creation date
        :success: [:class:`bool`] Success status of the operation
        :code: [:class:`int`] HTTP Status code
        :message: [:class:`str`] Message returned by the api
        :britishAchievement: [:class:`bool`] Achievement received
    """

    def __init__(self, json_data: dict) -> None:
        self.id = "" #dummy for typesetting
        self.code = 0 #dummy for typesetting
        for i in json_data:
            setattr(self, i.lower(), json_data[i])

    def __str__(self) -> str:
        return f"<AboutUs {int(self.code)} ({self.id})>"


class Misc(BaseHTTP):
    """Misc Api endpoints documented in https://docs.fluxpoint.dev/api/endpoints/misc"""

    def __str__(self) -> str:
        return '<MISC>'

    async def me(self) -> AboutUs:
        """Get info on the current user

        :return: The class containing all the information about the current user
        :rtype: AboutUs
        """
        return AboutUs(await self.request(RequestTypes.GET, 'me'))

    async def dadjoke(self) -> str:
        """
        Get a random dadjoke
        :return: The random dadjoke
        :rtype: :class:`str`
        """
        return (await self.request(RequestTypes.GET, 'dadjoke')).get('joke')
