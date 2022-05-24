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
        Returns a random nsfw feet image

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
    