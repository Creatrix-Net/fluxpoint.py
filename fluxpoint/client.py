from .paths import Convert,Color,CustomImage,Template,ImgAndGif,Lists,Minecraft,Misc,Utility


class FluxpointClient(Convert,Color,CustomImage,Template,ImgAndGif,Lists,Minecraft,Misc,Utility):
    '''The fluxpoint client where all the api routes are located'''

    def __str__(self) -> str:
        return '<Fluxpoint Client>'
