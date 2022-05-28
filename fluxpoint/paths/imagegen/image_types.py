from typing import Literal, Optional


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

        :raises OverflowError: When ``width`` or ``height`` is greater than 100 or less than 1
    """

    def __init__(
        self,
        width: int,
        height: int,
        color: Optional[str] = None,
        round: Optional[int] = None
    ) -> None:
        if self.color is None:
            self.color = color
        if width > 100 or width < 1:
            raise OverflowError("Width must be lesser than 20")
        self.width = width
        if height > 100 or height < 1:
            raise OverflowError("Height must be lesser than 20")
        self.height = height
        if round is not None:
            if round > 60 or round < 1:
                raise OverflowError("Round value must be lesser than 60")
            self.round = round

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

        :raises OverflowError: When ``width`` or ``height`` is greater than 100 or less than 1
    """

    __slots__ = ["width", "height", "cut", "color"]

    def __init__(
        self,
        width: int,
        height: int,
        cut: Literal['topleft', 'topright', 'bottomleft', 'bottomright'],
        color: Optional[str] = None
    ) -> None:
        if color is not None:
            self.color = color
        if width > 100 or width < 1:
            raise OverflowError("Width must be lesser than 20")
        self.width = width
        if height > 100 or height < 1:
            raise OverflowError("Height must be lesser than 20")
        self.height = height
        self.cut = cut

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

        :raises OverflowError: When ``radius`` is greater than 20 or less than 1
    """
    __slots__ = ["color", "radius"]

    def __init__(self, color: Optional[str] = None, radius: Optional[int] = None) -> None:
        if color is not None:
            self.color = color
        if radius is not None:
            if radius > 20 or radius < 1:
                raise OverflowError("Radius must be lesser than 20")
            self.radius = radius

    def to_dict(self) -> dict:
        """Converts the class to a dictionary"""
        given_dict = {'type': 'circle'}
        for i in self.__slots__:
            if hasattr(self, i):
                given_dict[i] = getattr(self, i)
        return given_dict


class ImageUrl:
    """_summary_

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
        
        :raises OverflowError: When ``width``, ``height``, ``maxwidth``or ``maxheight` is greater than 100 or less than 1
        :raises OverflowError: When ``round`` is greater than 60 or less than 1
    """   

    __slots__ = ["url", "cache", "width", "height", "maxwidth", "maxheight", "round"]

    def __init__(
        self,
        url: str,
        cache: Optional[bool] = False,
        width: Optional[int] = None,
        height: Optional[int] = None,
        maxwidth: Optional[int] = None, 
        maxheight: Optional[int] = None, 
        round: Optional[int] = None
    ) -> None: 
        self.url = url
        self.cache = cache
        if width is not None:
            if width > 100 or width < 1:
                raise OverflowError("Width must be lesser than 20")
            self.width = width
        if height is not None:
            if height > 100 or height < 1:
                raise OverflowError("Height must be lesser than 20")
            self.height = height
        if maxwidth is not None:
            if maxwidth > 100 or maxwidth < 1:
                raise OverflowError("Height must be lesser than 20")
            self.maxwidth = maxwidth
        if maxheight is not None:
            if maxheight > 100 or maxheight < 1:
                raise OverflowError("Height must be lesser than 20")
            self.maxheight = maxheight
        if round is not None:
            if round > 60 or round < 1:
                raise OverflowError("Round value must be lesser than 60")
            self.round = round


    def to_dict(self) -> dict:
        """Converts the class to a dictionary"""
        return_dict = {"type": "url"}
        for i in self.__slots__:
            if hasattr(self, i):
                return_dict[i] = getattr(self, i)
        return return_dict