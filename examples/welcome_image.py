import asyncio
import sys

from fluxpoint import FluxpointClient, WelcomeConfig

# setting up the fluxpoint client handler
a = FluxpointClient(api_token="get api token from https://fluxpoint.dev/api/access")

# setting up the windows loop policy according to the operating system
if sys.platform.startswith(('win32', 'cygwin')):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# getting the image bytes data
data = asyncio.run(
        a.welcome(
            WelcomeConfig(
                username="Builderb#0001",
	            avatar="https://cdn.discordapp.com/avatars/741291562687922329/d04f3007cf52a3f8be25688ad744e105.png?size=1024",
	            background="#aaaaaa"
            )
        )
    )

#saving the image into a file
with open('welcome_image.png', 'wb+') as f:
    f.write(data)
