from fluxpoint.errors import paramEnumValidCheck
from fluxpoint.vars import RequestTypes
from fluxpoint.http import BaseHTTP
from fluxpoint.vars import ImageType
import io
import aiohttp

class Convert(BaseHTTP):
    """Convert Api endpoints documented in https://docs.fluxpoint.dev/api/endpoints/convert
    """

    def __init__(self, *args, **kwargs) -> None:
        self.__baseurl = '/convert'
        super().__init__(*args, **kwargs)

    @staticmethod
    def imgdata2form(image: io.IOBase) -> aiohttp.FormData:
        """
        Converts image data to formdata

        :param image: image data
        :type image: :class:`io.IOBase`
        :return: aiohttp form data class
        :rtype: :class:`aiohttp.FormData`
        """
        form = aiohttp.FormData()
        form.add_field("file", image, filename="upload", content_type="application/octet-stream")
        return form

    async def html2markdown(self, html:str) -> str:
        """
        Convert html to markdown
        :param html: The html to convert
        :type html: str
        :return: The converted html to markdown
        :rtype: str
        """
        return (await self.request(RequestTypes.POST, f'{self.__baseurl}/html-markdown',data=html)).get('markdown')

    async def markdown2html(self, markdown:str) -> str:
        """
        Convert markdown to html
        :param markdown: The markdown to convert
        :type markdown: str
        :return: The converted markdown to html
        :rtype: str
        """
        return (await self.request(RequestTypes.POST, f'{self.__baseurl}/markdown-html',data=markdown)).get('html')

    async def image2type(self, image: io.IOBase, imgtype: ImageType, quality: int = 100) -> io.IOBase:
        """
        Convert an image to png/jpg/webp

        :raises ValueError: When the ``quality`` parameter is not between ``1`` and ``100``

        :param image: The image to convert
        :type image: :class:`io.IOBase`
        :param quality: The quality to convert to
        :type quality: int
        :param imgtype: The type to convert to
        :type imgtype: :class:`ImageType`

        :return: The converted image
        :rtype: :class:`io.IOBase`
        """
        if quality > 100 or quality < 1:
            raise ValueError("The return quality value must be between 1 and 100")
        paramEnumValidCheck(image, ImageType)
        return await self.request(
            RequestTypes.POST,
            f'{self.__baseurl}/image-{imgtype.value}',
            data=self.__class__.imgdata2form(image),
            return_bytes=True,
            return_json=False,
            params={"quality": quality}
        )