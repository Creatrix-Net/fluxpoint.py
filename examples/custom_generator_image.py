import asyncio
import sys

from fluxpoint import FluxpointClient, ImageUrl, Square, Text

# setting up the fluxpoint client handler
a = FluxpointClient(api_token="get api token from https://fluxpoint.dev/api/access")

# setting up the windows loop policy according to the operating system
if sys.platform.startswith(('win32', 'cygwin')):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# getting the image bytes data
data = asyncio.run(a.customimage(
    type="bitmap",
    width=2000,
    height=2000,
    color="#7289da",
    images=[
        ImageUrl(url="https://img.fluxpoint.dev/thm/1422436083957760.jpg",width=1000,height=1000),
        Square(round=160, x=20, y=240, width=1120, height=360, color="0,0,0,80")
    ],
    texts=[Text(text="Hello", size=120, x=600, y=1060)]
))

#saving the image into a file
with open('custom_generator_image.png', 'wb+') as f:
    f.write(data)
