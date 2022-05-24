from yarl import URL
from typing import Optional

from ..enums import RequestTypes
from ..http import BaseHTTP


class NSFW(BaseHTTP):

    def __str__(self) -> URL:
        return f'<Gifs>'
    
    async def azurlane_nsfw(self) -> URL:    
        """
        Returns a random nsfw azurlane image

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/nsfw/img/azurlane', _base_url='https://gallery.fluxpoint.dev/'))['file']
    
    async def feet_nsfw(self, gif: Optional[bool]=False) -> URL:             
        """
        Returns a random nsfw feet image/gif

        :param gif: If image returned should be gif image, defaults to False
        :type gif: Optional[bool], optional
        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (
            await self.request(
                RequestTypes.GET, 
                '/api/nsfw/img/feet' if not gif else '/api/nsfw/gif/feet', 
                _base_url='https://gallery.fluxpoint.dev/'
            )
        )['file']
    
    async def cum_nsfw(self, gif: Optional[bool]=False) -> URL:             
        """
        Returns a random nsfw blowjob image/gif

        :param gif: If image returned should be gif image, defaults to False
        :type gif: Optional[bool], optional
        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (
            await self.request(
                RequestTypes.GET, 
                '/api/nsfw/img/cum' if not gif else '/api/nsfw/gif/cum', 
                _base_url='https://gallery.fluxpoint.dev/'
            )
        )['file']
    
    async def blowjob_nsfw(self, gif: Optional[bool]=False) -> URL:             
        """
        Returns a random nsfw blowjob image/gif

        :param gif: If image returned should be gif image, defaults to False
        :type gif: Optional[bool], optional
        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (
            await self.request(
                RequestTypes.GET, 
                '/api/nsfw/img/blowjob' if not gif else '/api/nsfw/gif/blowjob', 
                _base_url='https://gallery.fluxpoint.dev/'
            )
        )['file']
    
    async def solo_girl_nsfw(self, gif: Optional[bool]=False) -> URL:             
        """
        Returns a random nsfw solo girl image/gif

        :param gif: If image returned should be gif image, defaults to False
        :type gif: Optional[bool], optional
        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (
            await self.request(
                RequestTypes.GET, 
                '/api/nsfw/img/solo' if not gif else '/api/nsfw/gif/solo', 
                _base_url='https://gallery.fluxpoint.dev/'
            )
        )['file']
    
    async def neko_nsfw(self, gif: Optional[bool]=False) -> URL:             
        """
        Returns a random nsfw neko image/gif

        :param gif: If image returned should be gif image, defaults to False
        :type gif: Optional[bool], optional
        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (
            await self.request(
                RequestTypes.GET, 
                '/api/nsfw/img/neko' if not gif else '/api/nsfw/gif/neko', 
                _base_url='https://gallery.fluxpoint.dev/'
            )
        )['file']
    
    async def boobs_nsfw(self, gif: Optional[bool]=False) -> URL:             
        """
        Returns a random nsfw boobs image/gif

        :param gif: If image returned should be gif image, defaults to False
        :type gif: Optional[bool], optional
        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (
            await self.request(
                RequestTypes.GET, 
                '/api/nsfw/img/boobs' if not gif else '/api/nsfw/gif/boobs', 
                _base_url='https://gallery.fluxpoint.dev/'
            )
        )['file']
    
    async def anal_nsfw(self, gif: Optional[bool]=False) -> URL:             
        """
        Returns a random nsfw anal image/gif

        :param gif: If image returned should be gif image, defaults to False
        :type gif: Optional[bool], optional
        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (
            await self.request(
                RequestTypes.GET, 
                '/api/nsfw/img/anal' if not gif else '/api/nsfw/gif/anal', 
                _base_url='https://gallery.fluxpoint.dev/'
            )
        )['file']
    
    async def pussy_nsfw(self, gif: Optional[bool]=False) -> URL:             
        """
        Returns a random nsfw pussy image/gif

        :param gif: If image returned should be gif image, defaults to False
        :type gif: Optional[bool], optional
        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (
            await self.request(
                RequestTypes.GET, 
                '/api/nsfw/img/pussy' if not gif else '/api/nsfw/gif/pussy', 
                _base_url='https://gallery.fluxpoint.dev/'
            )
        )['file']
    
    async def yuri_nsfw(self, gif: Optional[bool]=False) -> URL:             
        """
        Returns a random nsfw yuri image/gif

        :param gif: If image returned should be gif image, defaults to False
        :type gif: Optional[bool], optional
        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (
            await self.request(
                RequestTypes.GET, 
                '/api/nsfw/img/yuri' if not gif else '/api/nsfw/gif/yuri', 
                _base_url='https://gallery.fluxpoint.dev/'
            )
        )['file']
    
    async def bdsm_nsfw(self, gif: Optional[bool]=False) -> URL:             
        """
        Returns a random nsfw bdsm image/gif

        :param gif: If image returned should be gif image, defaults to False
        :type gif: Optional[bool], optional
        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (
            await self.request(
                RequestTypes.GET, 
                '/api/nsfw/img/yuri' if not gif else '/api/nsfw/gif/yuri', 
                _base_url='https://gallery.fluxpoint.dev/'
            )
        )['file']
    
    async def futa_nsfw(self, gif: Optional[bool]=False) -> URL:             
        """
        Returns a random nsfw futa image/gif

        :param gif: If image returned should be gif image, defaults to False
        :type gif: Optional[bool], optional
        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (
            await self.request(
                RequestTypes.GET, 
                '/api/nsfw/img/futa' if not gif else '/api/nsfw/gif/futa', 
                _base_url='https://gallery.fluxpoint.dev/'
            )
        )['file']
    
    async def hentai_nsfw(self) -> URL:    
        """
        Returns a random nsfw hentai gif

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/nsfw/gif/hentai', _base_url='https://gallery.fluxpoint.dev/'))['file']
    
    async def spank_nsfw(self) -> URL:    
        """
        Returns a random nsfw spank gif

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/nsfw/gif/spank', _base_url='https://gallery.fluxpoint.dev/'))['file']
    
    async def ass_nsfw(self, gif: Optional[bool]=False) -> URL:             
        """
        Returns a random nsfw ass image/gif

        :param gif: If image returned should be gif image, defaults to False
        :type gif: Optional[bool], optional
        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (
            await self.request(
                RequestTypes.GET, 
                '/api/nsfw/img/ass' if not gif else '/api/nsfw/gif/ass', 
                _base_url='https://gallery.fluxpoint.dev/'
            )
        )['file']
    
    async def kitsune_nsfw(self, gif: Optional[bool]=False) -> URL:             
        """
        Returns a random nsfw kitsune image/gif

        :param gif: If image returned should be gif image, defaults to False
        :type gif: Optional[bool], optional
        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (
            await self.request(
                RequestTypes.GET, 
                '/api/nsfw/img/kitsune' if not gif else '/api/nsfw/gif/kitsune', 
                _base_url='https://gallery.fluxpoint.dev/'
            )
        )['file']
    
    async def femdom_nsfw(self, gif: Optional[bool]=False) -> URL:             
        """
        Returns a random nsfw femdom image/gif

        :param gif: If image returned should be gif image, defaults to False
        :type gif: Optional[bool], optional
        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (
            await self.request(
                RequestTypes.GET, 
                '/api/nsfw/img/femdom' if not gif else '/api/nsfw/gif/femdom', 
                _base_url='https://gallery.fluxpoint.dev/'
            )
        )['file']
    
    async def nekopara_nsfw(self) -> URL:    
        """
        Returns a random nsfw nekopara image

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/nsfw/img/nekopara', _base_url='https://gallery.fluxpoint.dev/'))['file']
    
    async def lewd_nsfw(self) -> URL:    
        """
        Returns a random nsfw lewd image

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/nsfw/img/lewd', _base_url='https://gallery.fluxpoint.dev/'))['file']
    
    async def pantyhose_nsfw(self) -> URL:    
        """
        Returns a random nsfw pantyhose image

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/nsfw/img/pantyhose', _base_url='https://gallery.fluxpoint.dev/'))['file']
    
    async def cosplay_nsfw(self) -> URL:    
        """
        Returns a random nsfw cosplay image

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/nsfw/img/cosplay', _base_url='https://gallery.fluxpoint.dev/'))['file']
    
    async def petplay_nsfw(self) -> URL:    
        """
        Returns a random nsfw petplay image

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/nsfw/img/petplay', _base_url='https://gallery.fluxpoint.dev/'))['file']
    
    async def gasm_nsfw(self) -> URL:    
        """
        Returns a random nsfw ahego image

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/nsfw/img/gasm', _base_url='https://gallery.fluxpoint.dev/'))['file']
    
    async def ahego_nsfw(self) -> URL:    
        """
        Returns a random nsfw ahego image

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/nsfw/img/gasm', _base_url='https://gallery.fluxpoint.dev/'))['file']
    
    async def trap_nsfw(self) -> URL:    
        """
        Returns a random nsfw trap image

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/nsfw/img/trap', _base_url='https://gallery.fluxpoint.dev/'))['file']
    
    async def anus_nsfw(self) -> URL:    
        """
        Returns a random nsfw anus image

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/nsfw/img/anus', _base_url='https://gallery.fluxpoint.dev/'))['file']
    
    async def holo_nsfw(self) -> URL:    
        """
        Returns a random nsfw holo image

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/nsfw/img/holo', _base_url='https://gallery.fluxpoint.dev/'))['file']
    
    async def yaoi_nsfw(self) -> URL:    
        """
        Returns a random nsfw yaoi image

        :return: Url of the image
        :rtype: :class:`yarl.URL`
        """
        return (await self.request(RequestTypes.GET, 'api/nsfw/img/yaoi', _base_url='https://gallery.fluxpoint.dev/'))['file']