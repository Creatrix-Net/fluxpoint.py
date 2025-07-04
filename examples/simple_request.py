from fluxpoint import FluxpointClient
import asyncio
import sys

# setting up the fluxpoint client handler
a = FluxpointClient(api_token="get api token from fluxpoint.dev/api/access")

# setting up the windows loop policy according to the operating system
if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# getting the random dadjoke
print(asyncio.run(a.dadjoke()))