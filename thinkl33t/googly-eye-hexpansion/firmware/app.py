from app import App
from neopixel import NeoPixel
from tildagonos import tildagonos
from system.scheduler import scheduler
import asyncio

class GooglyEyeApp(App):
    def __init__(self, config):
        self._n = NeoPixel(config.pin[0], 2)
        self._port = config.port
        self._fps = 5
        for a in scheduler.apps:
            if 'PatternDisplay' == a.__class__.__name__:
                self._fps = a._p.fps

    async def background_task(self):
        while True:
            self._n[1] = tildagonos.leds[(2*self._port)-1]
            self._n[0] = tildagonos.leds[2*self._port]
            self._n.write()
            await asyncio.sleep(1 / self._fps)


__app_export__ = GooglyEyeApp
