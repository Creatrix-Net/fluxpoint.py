from yarl import URL

from ..enums import RequestTypes
from ..http import BaseHTTP


class Images(BaseHTTP):
    def __str__(self) -> URL:
        return '<Images>'

    async def neko(self) -> URL:
        """
        Returns a random image of nekos

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/sfw/img/neko', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def maid(self) -> URL:
        """
        Returns a random image of maids

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/maid', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def nekopara(self) -> URL:
        """
        Returns a random image from nekopara

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/nekopara', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def azurlane(self) -> URL:
        """
        Returns a random image from azurlane
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/azurlane', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def senko(self) -> URL:
        """
        Returns a random image from senko
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/senko', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def ddlc(self) -> URL:
        """
        Returns a random image from Doki Doki Literature Club
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/ddlc', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def wallpaper(self) -> URL:
        """
        Returns a random wallpaper image
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/wallpaper', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def anime(self) -> URL:
        """
        Returns a random anime image
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/anime', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def meme(self) -> URL:
        """
        Returns a random meme
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/meme', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def nou(self) -> URL:
        """
        Returns a random No U image
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/nou', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def pog(self) -> URL:
        """
        Returns a random pog meme image
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/pog', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def cat(self) -> URL:
        """
        Returns a random cat image
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/cat', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def dog(self) -> URL:
        """
        Returns a random dog image
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/dog', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def lizard(self) -> URL:
        """
        Returns a random lizard image
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/img/lizard', _base_url='https://gallery.fluxpoint.dev/'))['file']
