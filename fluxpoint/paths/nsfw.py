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