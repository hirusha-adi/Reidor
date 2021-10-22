import os
from datetime import datetime as dt


class Logger:
    def __init__(self, color: bool = False, file: bool = False, filename: str = "log", time: bool = True):
        self.color = color
        self.file = file
        self.filename = filename
        self.time = time

        if self.file:
            with open(f"{self.filename}.log", "w", encoding="utf-8") as lfm:
                if self.time:
                    lfm.write(
                        f"\nINFO: {dt.now()} - {self.filename}.log file created")
                else:
                    lfm.write(
                        f"\nINFO: {self.filename}.log file created")

    def OFF(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"
        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nOFF: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nOFF: {final_argsc}")
