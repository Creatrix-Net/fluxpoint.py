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