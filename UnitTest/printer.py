class PrinterError(Exception):
    pass


class Printer:
    def __init__(self,page_per_s:int,capacity:int):
        self.page_per_s = page_per_s
        self._capacity = capacity

    def print(self,pages):
        if pages > self._capacity:
            raise PrinterError("Printer does not allow more pages then it's limit")

        self._capacity -= pages

        return f"Printed {pages} pages in {pages/self.page_per_s:.2f} seconds"
