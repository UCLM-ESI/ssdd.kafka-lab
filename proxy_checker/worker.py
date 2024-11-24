import time

from threading import Thread
from typing import Optional

import Ice

from .publisher import Publisher


class Worker(Thread):
    def __init__(self, proxy: Ice.ObjectPrx, producer: Publisher, period: Optional[float] = 0.0):
        super(Worker, self).__init__(daemon=True)
        self.prx = proxy
        self.producer = producer
        self.period = period
    
    def work(self) -> bool:
        try:
            self.prx.ice_ping()
            return True

        except Exception:
            return False
    
    def run(self) -> None:
        str_prx = str(self.prx)
        result = self.work()

        if not self.period:
            self.producer.notify_result(str_prx, result)
            return

        iteration = 0
            
        while True:
            self.producer.notify_result(str_prx, result, iteration)
            time.sleep(self.period)

            result = self.work()
            iteration += 1
