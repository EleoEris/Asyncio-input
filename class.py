import asyncio
from keyboard import is_pressed

class something:
    def __init__(self, interrupt_key = 'k': str):
        self.interrupt_key = interrupt_key
        self.interrupted = False
        
    def run(self):
        asyncio.run(self.check_interrupt())
    
    async def check_interrupt(self):
        main = asyncio.create_task(self.main_loop())
        while not self.program_ended:
            await asyncio.sleep(.1)
            if is_pressed(self.interrupt_key):
                main.cancel()
                self.interrupted = True

    async def main_loop(self):
        while True:
            pass
        
        self.interrupted = True
