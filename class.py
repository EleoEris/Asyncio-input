import asyncio
from keyboard import is_pressed

class something:
    def __init__(self, interrupt_key: str):
        self.interrupt_key = interrupt_key
        
    def run(self):
        asyncio.run(self._run())

    async def _run(self):
        main = asyncio.create_task(self.main_loop())
        check_interrupt = asyncio.create_task(self.check_interrupt())
        await check_interrupt
   
    async def main_loop():
        while True:
            await asyncio.sleep(1)
    
    async def check_interrupt(self):
        while True:
            await asyncio.sleep(.1)
            if is_pressed(self.key):
                self.interrupted = True
                break
