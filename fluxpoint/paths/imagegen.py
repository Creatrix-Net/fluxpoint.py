from typing import Literal, Optional, Dict, Union, List
import io
from ..http import BaseHTTP
from ..enums import RequestTypes


class Square:
    """Square Image class

        :param width: Set the width of the shape
        :type width: int
        :param height: Set the height of the shape
        :type height: int
        :param color: Set the shape to be a color from name/hex/rgb/rgba use rgba for transparency, defaults to None
        :type color: Optional[str], optional
        :param round:  Make the borders of the shape round. (Default 0), defaults to None
        :type round: Optional[int], optional
        :param x: Position the image in pixels, defaults to None
        :type x: Optional[int], optional
        :param y: Position the image in pixels, defaults to None
        :type y: Optional[int], optional
    """
    __slots__ = ["width", "height", "color", "round", "x", "y"]

    def __init__(
        self,
        width: int,
        height: int,
        color: Optional[str] = None,
        round: Optional[int] = None,
        x: Optional[int] = None,
        y: Optional[int] = None
    ) -> None:
        if color is None:
            self.color = color
        self.width = width
        self.height = height
        if round is not None:
            self.round = round
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def to_dict(self) -> dict:
        """Converts the class to a dictionary"""
        return_dict = {'type': 'bitmap'}
        for i in self.__slots__:
            if hasattr(self, i):
                return_dict[i] = getattr(self, i)
        return return_dict


class Triangle:
    """Triangle Image class

        :param color: Set the shape to be a color from name/hex/rgb/rgba use rgba for transparency
        :type color: Optional[str]
        :param width: Set the width of the shape
        :type width: int
        :param height: Set the height of the shape
        :type height: int
        :param cut: Choose where the missing peice of the triangle is
        :type cut: Literal[topleft, topright, bottomleft, bottomright]
        :param x: Position the image in pixels, defaults to None
        :type x: Optional[int], optional
        :param y: Position the image in pixels, defaults to None
        :type y: Optional[int], optional
    """

    __slots__ = ["width", "height", "cut", "color", "x", "y"]

    def __init__(
        self,
        width: int,
        height: int,
        cut: Literal['topleft', 'topright', 'bottomleft', 'bottomright'],
        color: Optional[str] = None,
        x: Optional[int] = None,
        y: Optional[int] = None
    ) -> None:
        if color is not None:
            self.color = color
        self.width = width
        self.height = height
        self.cut = cut
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def to_dict(self) -> dict:
        """Converts the class to a dictionary"""
        return_dict = {'type': 'triangle'}
        for i in self.__slots__:
            if hasattr(self, i):
                return_dict[i] = getattr(self, i)
        return return_dict


class Circle:
    """Circle Image class

        :param color: Set the shape to be a color from name/hex/rgb/rgba use rgba for transparency
        :type color: Optional[str]
        :param radius: Set the size of the circle from the center point
        :type radius: Optional[int]
        :param x: Position the image in pixels, defaults to None
        :type x: Optional[int], optional
        :param y: Position the image in pixels, defaults to None
        :type y: Optional[int], optional
    """
    __slots__ = ["color", "radius", "x", "y"]

    def __init__(self, color: Optional[str] = None, radius: Optional[int] = None, x: Optional[int] = None, y: Optional[int] = None) -> None:
        if color is not None:
            self.color = color
        if radius is not None:
            self.radius = radius
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def to_dict(self) -> dict:
        """Converts the class to a dictionary"""
        given_dict = {'type': 'circle'}
        for i in self.__slots__:
            if hasattr(self, i):
                given_dict[i] = getattr(self, i)
        return given_dict


class ImageUrl:
    """ImageUrl Image class

        :param url: https://website.com/image.png
        :type url: str
        :param cache: Cache the image server-side so it can be easily loaded again such as background images. (Not Recommended for Avatars), defaults to False
        :type cache: Optional[bool], optional
        :param width: Set the width of the image, defaults to None
        :type width: Optional[int], optional
        :param height: Set the height of the image, defaults to None
        :type height: Optional[int], optional
        :param maxwidth: Set the max width so the image can scale properly, defaults to None
        :type maxwidth: Optional[int], optional
        :param maxheight: Set the max height so the image can scale properly, defaults to None
        :type maxheight: Optional[int], optional
        :param round: Make the borders of the image round for stuff like circle avatars, defaults to None
        :type round: Optional[int], optional
        :param x: Position the image in pixels, defaults to None
        :type x: Optional[int], optional
        :param y: Position the image in pixels, defaults to None
        :type y: Optional[int], optional
    """

    __slots__ = ["url", "cache", "width",
                 "height", "maxwidth", "maxheight", "round"]

    def __init__(
        self,
        url: str,
        cache: Optional[bool] = False,
        width: Optional[int] = None,
        height: Optional[int] = None,
        maxwidth: Optional[int] = None,
        maxheight: Optional[int] = None,
        round: Optional[int] = None,
        x: Optional[int] = None,
        y: Optional[int] = None
    ) -> None:
        self.url = url
        self.cache = cache
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if maxwidth is not None:
            self.maxwidth = maxwidth
        if maxheight is not None:
            self.maxheight = maxheight
        if round is not None:
            self.round = round
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def to_dict(self) -> dict:
        """Converts the class to a dictionary"""
        return_dict = {"type": "url"}
        for i in self.__slots__:
            if hasattr(self, i):
                return_dict[i] = getattr(self, i)
        return return_dict


class Text:
    """Text class for custom image

        :param text: Set the text
        :type text: str

        :param size: Set the font size of the text, defaults to 16
        :type size: Optional[int], optional

        :param font: Set the font to use for the text, defaults to "Sans Serif"
        :type font: Optional[str], optional

        :param color: Set the text color from name/hex/rgb/rgba use rgba for transparency, defaults to "white"
        :type color: Optional[str], optional

        :param back: Set the background color for the text box from name/hex/rgb/rgba use rgba for transparency, defaults to None
        :type back: Optional[str], optional

        :param x: Position the text in pixels, defaults to 0
        :type x: Optional[int], optional

        :param y: Position the text in pixels, defaults to 0
        :type y: Optional[int], optional

        :param align: Align the text from left/center/right (Default left), defaults to "l"
        :type align: Optional[Literal[l,m,r]], optional

        :param bold: Set the text to bold style, defaults to False
        :type bold: Optional[bool], optional

        :param italics: Set the text to italics style, defaults to False
        :type italics: Optional[bool], optional

        :param underline: Set the text to underline style, defaults to False
        :type underline: Optional[bool], optional

        :param line: Set the text to underline style, defaults to 1.0
        :type line: Optional[float], optional

        :param weight: Increase the boldness of the tex, defaults to 500
        :type weight: Optional[int], optional

        :param width: Set the max width of the text box before it wraps to a newline, defaults to None
        :type width: Optional[int], optional

        :param height: et the max height of the text box to clip extra text, defaults to None
        :type height: Optional[int], optional

        :param outline: Show text outline with default options, defaults to False
        :type outline: Optional[bool], optional

        :param outlinewidth: Set the outline size from the text, defaults to 9
        :type outlinewidth: Optional[int], optional

        :param outlinecolor: Set the outline color from name/hex/rgb/rgba use rgba for transparency, defaults to "black"
        :type outlinecolor: Optional[str], optional

        :param outlineblur: Make the outline transparency less visible for a cool effect, defaults to 1
        :type outlineblur: Optional[int], optional
    """
    __slots__ = [
        "text",
        "size",
        "font",
        "color",
        "back",
        "x",
        "y",
        "align",
        "bold",
        "italics",
        "underline",
        "line",
        "weight",
        "width",
        "height",
        "outline",
        "outlinewidth",
        "outlinecolor",
        "outlineblur"
    ]

    def __init__(
        self,
        text: str,
        size: Optional[int] = 16,
        font: Optional[str] = "Sans Serif",
        color: Optional[str] = "white",
        back: Optional[str] = None,
        x: Optional[int] = 0,
        y: Optional[int] = 0,
        align: Optional[Literal["l", "m", "r"]] = "l",
        bold: Optional[bool] = False,
        italics: Optional[bool] = False,
        underline: Optional[bool] = False,
        line: Optional[float] = 1.0,
        weight: Optional[int] = 500,
        width: Optional[int] = None,
        height: Optional[int] = None,
        outline: Optional[bool] = False,
        outlinewidth: Optional[int] = 9,
        outlinecolor: Optional[str] = "black",
        outlineblur: Optional[int] = 1,
    ) -> None:
        self.text = text
        self.size = size
        self.font = font
        self.color = color
        if back is not None:
            self.back = back
        self.x = x
        self.y = y
        self.align = align
        self.bold = bold
        self.italics = italics
        self.underline = underline
        self.line = line
        self.weight = weight
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        self.outline = outline
        self.outlinewidth = outlinewidth
        self.outlinecolor = outlinecolor
        self.outlineblur = outlineblur

    def to_dict(self) -> dict:
        """Converts the class to a dictionary"""
        return_dict = {}
        for i in self.__slots__:
            if hasattr(self, i):
                return_dict[i] = getattr(self, i)
        return return_dict


class ImageGenerator(BaseHTTP):
    """Custome image generator Api endpoints documented in https://bluedocs.page/fluxpoint-api/imagegen"""

    def __str__(self):
        return "<Image Generator>"

    async def test(self) -> Union[Dict, io.IOBase]:
        """Test the image generator

        :returns: The response from the server
        :rtype: Union[Dict, io.IOBase]
        """
        return await self.request(RequestTypes.GET, '/test/image', return_bytes=True, return_json=False)  # skipcq: TYP-005

    async def customimage(
        self,
        type: Literal["bitmap", "image"],
        width: int,
        height: int,
        color: str,
        images: Optional[List[Union[ImageUrl, Square, Triangle, Circle]]] = [],
        texts: Optional[List[Text]] = []
    ) -> Union[Dict, io.IOBase]:
        """Get the created image gen image.

        :param type: Image type
        :type type: Literal[bitmap, image]
        :param width: Overall width of the image
        :type width: int
        :param height: Overall height of the image
        :type height: int
        :param color: Background colour of the image
        :type color: str
        :param images: The image(s) that you want to embed in image, defaults to []
        :type images: Optional[List[Union[ImageUrl, Square, Triangle, Circle]]], optional
        :param texts: The text(s) that you want to embed in image, defaults to []
        :type texts: Optional[List[Text]], optional

        :return: The custom generated image bytes data
        :rtype: Union[Dict, io.IOBase]
        """
        json_data = {
            "Base": {
                "type": type,
                "width": width,
                "height": height,
                "color": color
            },
            "Images": list(map(lambda x: x.to_dict(), images)),
            "Texts": list(map(lambda x: x.to_dict(), texts))
        }
        return await self.request(RequestTypes.POST, '/gen/custom', return_bytes=True, return_json=False, json=json_data)
