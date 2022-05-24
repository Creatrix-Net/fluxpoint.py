from ..enums import RequestTypes
from ..http import BaseHTTP

class AboutUs:
    """A class which gives info from the json data of about us

    :param json_data: The json data from the api
    :type json_data: dict

    Acessible Parameter
    --------------------

    - id str
    """
    def __init__(self, json_data: dict) -> None:     
        for i in json_data:
            setattr(self, i, json_data[i])

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