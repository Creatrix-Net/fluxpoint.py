from typing import Union

from yarl import URL

from ..enums import RequestTypes
from ..http import BaseHTTP


class Gifs(BaseHTTP):
    def __str__(self) -> Union[URL, str]:
        return '<Gifs>'

    async def baka(self) -> Union[URL, str]:
        """
        Returns a random baka gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, 'api/sfw/gif/baka', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def bite(self) -> Union[URL, str]:
        """
        Returns a random bite gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/bite', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def blush(self) -> Union[URL, str]:
        """
        Returns a random blush gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/blush', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def cry(self) -> Union[URL, str]:
        """
        Returns a random cry gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/cry', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def dance(self) -> Union[URL, str]:
        """
        Returns a random dance gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/dance', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def feed(self) -> Union[URL, str]:
        """
        Returns a random feed gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/feed', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def fluff(self) -> Union[URL, str]:
        """
        Returns a random fluff gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/fluff', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def grab(self) -> Union[URL, str]:
        """
        Returns a random grab cheeks gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/grab', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def grabcheecks(self) -> Union[URL, str]:
        """
        Returns a random grab cheeks gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/grab', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def handhold(self) -> Union[URL, str]:
        """
        Returns a random hand holding gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/handhold', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def handholding(self) -> Union[URL, str]:
        """
        Returns a random hand holding gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/handhold', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def hand_holding(self) -> Union[URL, str]:
        """
        Returns a random hand holding gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/handhold', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def hand_hold(self) -> Union[URL, str]:
        """
        Returns a random hand holding gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/handhold', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def highfive(self) -> Union[URL, str]:
        """
        Returns a random highfive gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/highfive', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def hug(self) -> Union[URL, str]:
        """
        Returns a random hug gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/hug', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def kiss(self) -> Union[URL, str]:
        """
        Returns a random kiss gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/kiss', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def lick(self) -> Union[URL, str]:
        """
        Returns a random lick gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/lick', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def neko_gif(self) -> Union[URL, str]:
        """
        Returns a random neko gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/neko', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def pat(self) -> Union[URL, str]:
        """
        Returns a random pat gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/pat', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def poke(self) -> Union[URL, str]:
        """
        Returns a random poke gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/poke', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def punch(self) -> Union[URL, str]:
        """
        Returns a random punch gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/punch', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def shrug(self) -> Union[URL, str]:
        """
        Returns a random shrug gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/shrug', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def slap(self) -> Union[URL, str]:
        """
        Returns a random slap gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/slap', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def smug(self) -> Union[URL, str]:
        """
        Returns a random smug gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/smug', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def stare(self) -> Union[URL, str]:
        """
        Returns a random stare gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/stare', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def tickle(self) -> Union[URL, str]:
        """
        Returns a random tickle gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/tickle', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def wag(self) -> Union[URL, str]:
        """
        Returns a random wag gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/wag', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def wasted(self) -> Union[URL, str]:
        """
        Returns a random wasted gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/wasted', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def wave(self) -> Union[URL, str]:
        """
        Returns a random wave gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/wave', _base_url='https://gallery.fluxpoint.dev/'))['file']

    async def wink(self) -> Union[URL, str]:
        """
        Returns a random wink gif

        :return: Url of the image
        :rtype: :class: Union[`yarl.URL` , str]
        """
        return (await self.request(RequestTypes.GET, '/api/sfw/gif/wink', _base_url='https://gallery.fluxpoint.dev/'))['file']
