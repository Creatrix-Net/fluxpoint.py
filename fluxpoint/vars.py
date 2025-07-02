import enum

@enum.unique
class RequestTypes(enum.IntEnum):
    """Different requests types for the http request"""

    DELETE = 0
    GET = 1
    HEAD = 2
    PATCH = 3
    PUT = 4
    POST = 5

@enum.unique
class TestImageType(enum.StrEnum):
    """Different test image type for the http request"""

    PNG = "png"
    WEBP = "webp"
    JPEG = "jpeg"

@enum.unique
class SFWImage(enum.StrEnum):
    """Different SFW image type for the http request"""

    anime = "anime"
    azurlane = "azurlane"
    chibi = "chibi"
    christmas = "christmas"
    ddlc = "ddlc"
    halloween = "halloween"
    holo = "holo"
    kitsune = "kitsune"
    maid = "maid"
    neko = "neko"
    nekoboy = "nekoboy"
    nekopara = "nekopara"
    senko = "senko"
    wallpaper = "wallpaper"
    meme = "meme"
    nou = "nou"
    pog = "pog"
    cat = "cat"
    dog = "dog"
    duck = "duck"
    lizard = "lizard"

@enum.unique
class SFWGif(enum.StrEnum):
    """Different SFW Gif image type for the http request"""

    baka = "baka"
    bite = "bite"
    blush = "blush"
    cry = "cry"
    dance = "dance"
    feed = "feed"
    fluff = "fluff"
    grab = "grab"
    handhold = "handhold"
    highfive = "highfive"
    hug = "hug"
    kiss = "kiss"
    laugh = "laugh"
    lick = "lick"
    neko = "neko"
    pat = "pat"
    poke = "poke"
    punch = "punch"
    shrug = "shrug"
    slap = "slap"
    smug = "smug"
    stare = "stare"
    tickle = "tickle"
    wag = "wag"
    wasted = "wasted"
    wave = "wave"
    wink = "wink"

@enum.unique
class NSFWImage(enum.StrEnum):
    """Different NSFW image type for the http request"""

    anal = "anal"
    anus = "anus"
    ass = "ass"
    azurlane = "azurlane"
    bdsm = "bdsm"
    blowjob = "blowjob"
    boobs = "boobs"
    cosplay = "cosplay"
    cum = "cum"
    feet = "feet"
    femdom = "femdom"
    futa = "futa"
    gasm = "gasm"
    holo = "holo"
    kitsune = "kitsune"
    lewd = "lewd"
    neko = "neko"
    nekopara = "nekopara"
    pantyhose = "pantyhose"
    peeing = "peeing"
    petplay = "petplay"
    pussy = "pussy"
    slimes = "slimes"
    solo = "solo"
    swimsuit = "swimsuit"
    tentacle = "tentacle"
    thighs = "thighs"
    trap = "trap"
    yaoi = "yaoi"
    yuri = "yuri"

@enum.unique
class NSFWGif(enum.StrEnum):
    """Different NSFW gif type for the http request"""

    anal = "anal"
    ass = "ass"
    bdsm = "bdsm"
    blowjob = "blowjo"
    boobjob = "boobjob"
    boobs = "boobs"
    cum = "cum"
    feet = "feet"
    futa = "futa"
    handjob = "handjob"
    hentai = "hentai"
    kuni = "kuni"
    neko = "neko"
    pussy = "pussy"
    wank = "wank"
    solo = "solo"
    spank = "spank"
    tentacle = "tentacle"
    toys = "toys"
    yuri = "yuri"