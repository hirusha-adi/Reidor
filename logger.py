import os
from datetime import datetime as dt


class c:
    # https://www.codegrepper.com/code-examples/actionscript/escape+code+color+for+grey
    g = '\033[92m'  # GREEN
    y = '\033[93m'  # YELLOW
    r = '\033[91m'  # RED
    w = '\033[0m'  # RESET COLOR
    p = '\033[35m'  # PURPLE
    d = '\033[30;1m'  # DULL


class Logger:
    # ALL < TRACE < DEBUG < INFO < WARN < ERROR < FATAL < OFF
    def __init__(self, printtxt: bool = True, color: bool = False, file: bool = False, filename: str = "log", time: bool = True):
        self.color = color
        self.file = file
        self.filename = filename
        self.time = time
        self.printtxt = printtxt

        if self.file:
            if (f"{self.filename}.log" in os.listdir(os.getcwd())) == False:
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

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.r}OFF:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.r}OFF:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"OFF: {dt.now()} - {final_argsc}")
                else:
                    print(f"OFF: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nOFF: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nOFF: {final_argsc}")

    def FATAL(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.r}FATAL:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.r}FATAL:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"FATAL: {dt.now()} - {final_argsc}")
                else:
                    print(f"FATAL: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nFATAL: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nFATAL: {final_argsc}")

    def ERROR(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.r}ERROR:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.r}ERROR:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"ERROR: {dt.now()} - {final_argsc}")
                else:
                    print(f"ERROR: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nERROR: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nERROR: {final_argsc}")

    def WARN(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.y}WARN:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.y}WARN:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"WARN: {dt.now()} - {final_argsc}")
                else:
                    print(f"WARN: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nWARN: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nWARN: {final_argsc}")

    def INFO(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.p}INFO:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.p}INFO:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"INFO: {dt.now()} - {final_argsc}")
                else:
                    print(f"INFO: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nINFO: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nINFO: {final_argsc}")

    def DEBUG(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.p}DEBUG:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.p}DEBUG:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"DEBUG: {dt.now()} - {final_argsc}")
                else:
                    print(f"DEBUG: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nDEBUG: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nDEBUG: {final_argsc}")

    def TRACE(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.p}TRACE:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.p}TRACE:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"TRACE: {dt.now()} - {final_argsc}")
                else:
                    print(f"TRACE: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nTRACE: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nTRACE: {final_argsc}")

    def CUS(self, *args, topic: str = "INFO", colorc: str = "red"):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.color:
            if colorc == "red":
                colorcf = c.r
            elif colorc == "green":
                colorcf = c.g
            elif colorc == "yellow":
                colorcf = c.y
            elif colorc == "white" or (colorc.lower().startswith('n')):
                colorcf = c.w
            elif colorc == "purple":
                colorcf = c.p
            else:
                colorcf = c.y

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{colorcf}{topic}:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{colorcf}{topic}:{c.d} {final_argsc}")
            else:
                if self.time:
                    print(f"{topic}: {dt.now()} - {final_argsc}")
                else:
                    print(f"{topic}: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\n{topic}: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\n{topic}: {final_argsc}")


l = Logger(printtxt=True, color=True, time=False)
l.CUS("GOD", "DAMN!", "TEST", "LOL", topic="TEST", colorc="yellow")
