from typing import Literal


class Triangle:
    """Triangle Image class

        :param color: Set the shape to be a color from name/hex/rgb/rgba use rgba for transparency
        :type color: str
        :param width: Set the width of the shape
        :type width: int
        :param height: Set the height of the shape
        :type height: int
        :param cut: Choose where the missing peice of the triangle is
        :type cut: Literal[topleft, topright, bottomleft, bottomright]

        :raises OverflowError: When ``width`` or ``height`` is greater than 100 or less than 1
    """    
    
    def __init__(
        self, 
        color: str, 
        width: int, 
        height: int, 
        cut: Literal['topleft', 'topright', 'bottomleft', 'bottomright']
    ) -> None:
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
        return {
            'type': 'triangle',
            'color': self.color,
            'width': self.width,
            'height': self.height,
            'cut': self.cut
        }


class Circle:
    """Circle Image class

        :param color: Set the shape to be a color from name/hex/rgb/rgba use rgba for transparency
        :type color: str
        :param radius: Set the size of the circle from the center point
        :type radius: int

        :raises OverflowError: When ``radius`` is greater than 20 or less than 1
    """       
    def __init__(self, color: str, radius: int) -> None:
        self.color = color
        if radius > 20 or radius < 1:
            raise OverflowError("Radius must be lesser than 20")
        self.radius = radius
    
    def to_dict(self) -> dict:
        """Converts the class to a dictionary"""
        return {
            "type": "circle",
            "color": self.color,
            "radius": self.radius
        }
