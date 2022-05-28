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
            if i in return_dict:
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
            if i in return_dict:
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
