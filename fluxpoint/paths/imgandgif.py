from typing import Union

from yarl import URL

from fluxpoint.vars import RequestTypes
from fluxpoint.http import BaseHTTP
from fluxpoint.vars import SFWImage, SFWGif, NSFWImage, NSFWGif
from fluxpoint.errors import InvalidCategory


class ImgAndGif(BaseHTTP):
    """Images Api endpoints documented in
    - https://docs.fluxpoint.dev/api/endpoints/sfw-anime-images
    - https://docs.fluxpoint.dev/api/endpoints/sfw-anime-gifs
    - https://docs.fluxpoint.dev/api/endpoints/animal-images
    - https://docs.fluxpoint.dev/api/endpoints/meme-images
    """

    def __init__(self, *args, **kwargs) -> None:
        self.__baseurlsfw = '/sfw'
        self.__sfwurlimg = f'{self.__baseurlsfw}/img'
        self.__sfwurlgif = f'{self.__baseurlsfw}/gif'

        self.__baseurlnsfw = '/nsfw'
        self.__nsfwurlimg = f'{self.__baseurlnsfw}/img'
        self.__nsfwurlgif = f'{self.__baseurlnsfw}/gif'
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return '<Image and Gif>'

    async def sfw(self, category: Union[SFWImage, SFWGif], gif: bool = False) -> Union[URL, str]:
        """
        Returns a random sfw image/gif from the category provided

        :raises InvalidCategory: When ``gif`` is ``true``  and ``category`` is not from :class:`SFWGif`
        :raises Exception: When ``category`` is not a instance of :class:`SFWImage` or :class:`SFWGif`

        :param category: SFWImage or SFWGif categories as defined in enums
        :type category: Union[:class:`SFWImage` , :class:`SFWGif`]
        :param gif: Set true when want gif
        :type gif:boolean

        :return: Url of the image/gif
        :rtype: Union[:class:`yarl.URL` , :class:`str`]
        """
        if isinstance(category, SFWImage) or isinstance(category, SFWGif):
            raise Exception("Category must be a instance of SFWImage or SFWGif")
        if gif:
            if category not in SFWGif:
                raise InvalidCategory()
            return (await self.request(RequestTypes.GET, f'{self.__sfwurlgif}/{category.value}')).get('file')
        return (await self.request(RequestTypes.GET, f'{self.__sfwurlimg}/{category.value}')).get('file')

    async def nsfw(self, category: Union[NSFWImage, NSFWGif], gif: bool = False) -> Union[URL, str]:
        """
        Returns a random nsfw image/gif from the category provided

        :raises InvalidCategory: When ``gif`` is ``true``  and ``category`` is not from :class:`NSFWGif`
        :raises Exception: When ``category`` is not a instance of :class:`NSFWImage` or :class:`NSFWGif`

        :param category: NSFWImage or NSFWGif categories as defined in enums
        :type category: Union[:class:`NSFWImage` , :class:`NSFWGif`]
        :param gif: Set true when want gif
        :type gif:boolean

        :return: Url of the image/gif
        :rtype: Union[:class:`yarl.URL` , :class:`str`]
        """
        if isinstance(category, NSFWImage) or isinstance(category, NSFWGif):
            raise Exception("Category must be a instance of NSFWImage or NSFWGif")
        if gif:
            if category not in NSFWGif:
                raise InvalidCategory()
            return (await self.request(RequestTypes.GET, f'{self.__nsfwurlgif}/{category.value}')).get('file')
        return (await self.request(RequestTypes.GET, f'{self.__nsfwurlimg}/{category.value}')).get('file')
