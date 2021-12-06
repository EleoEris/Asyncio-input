import asyncio
from keyboard import is_pressed

class InterrupClass:
    def __init__(self, interrupt_key = 'k': str):
        self.interrupt_key = interrupt_key  # what to press to exit
        self.program_ended = False          # flag to sync the exit
        
    def run(self):
        asyncio.run(self.check_interrupt())
    
    async def check_interrupt(self):        # treating this as event loop, will probably rework this later
        main = asyncio.create_task(self.main_loop())
        while not self.program_ended:
            await asyncio.sleep(.1)
            if is_pressed(self.interrupt_key):
                self.program_ended = True
                ### Might want to make a decontructor on the main node with an await asyncio.sleep here for timeout (in case main_loop broken)
                main.cancel()

    async def main_loop(self):
        while True:                         # actual main()
            if self.program_ended: pass
        
        self.program_ended = True
