import asyncio
import sys

from fluxpoint import FluxpointClient

# setting up the fluxpoint client handler
a = FluxpointClient(api_token="get api token from https://fluxpoint.dev/api/access")

# setting up the windows loop policy according to the operating system
if sys.platform.startswith(('win32', 'cygwin')):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# getting the image bytes data
data = asyncio.run(a.test())

#saving the image into a file
with open('custom_generator_test.png', 'wb+') as f:
    f.write(data)
