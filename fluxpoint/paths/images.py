from typing import Union

from yarl import URL

from ..enums import RequestTypes
from ..http import BaseHTTP


class Images(BaseHTTP):
    def __str__(self) -> Union[URL, str]:
        return '<Images>'

    async def neko(self) -> Union[URL, str]:
        """
        Returns a random image of nekos

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, 'api/sfw/img/neko', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def maid(self) -> Union[URL, str]:
        """
        Returns a random image of maids

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/maid', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def nekopara(self) -> Union[URL, str]:
        """
        Returns a random image from nekopara

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/nekopara', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def azurlane(self) -> Union[URL, str]:
        """
        Returns a random image from azurlane

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/azurlane', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def senko(self) -> Union[URL, str]:
        """
        Returns a random image from senko

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/senko', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def ddlc(self) -> Union[URL, str]:
        """
        Returns a random image from Doki Doki Literature Club

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/ddlc', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def wallpaper(self) -> Union[URL, str]:
        """
        Returns a random wallpaper image

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/wallpaper', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def anime(self) -> Union[URL, str]:
        """
        Returns a random anime image

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/anime', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def meme(self) -> Union[URL, str]:
        """
        Returns a random meme

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/meme', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def nou(self) -> Union[URL, str]:
        """
        Returns a random No U image

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/nou', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def pog(self) -> Union[URL, str]:
        """
        Returns a random pog meme image

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/pog', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def cat(self) -> Union[URL, str]:
        """
        Returns a random cat image

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/cat', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def dog(self) -> Union[URL, str]:
        """
        Returns a random dog image

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/dog', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def lizard(self) -> Union[URL, str]:
        """
        Returns a random lizard image

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/lizard', _base_url='https://gallery.fluxpoint.dev/'))['file']
