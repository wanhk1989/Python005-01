
import time
from datetime import datetime
import logging
from pathlib import Path
import os.path

format = '%(asctime)s %(levelname)-8s %(message)s'

today = time.strftime("%Y-%m-%d", time.localtime())
temdir = "".join(["d:/var/log/python-", today])
logdir=Path(temdir)

filename=os.path.join(logdir,"test.log")
logpath = Path(filename)
if not logdir.exists():
    print("logpath not exists")
    logdir.mkdir(parents=True)
    logpath.touch()


logging.basicConfig(filename=filename, format=format, level=logging.INFO)

def logrecorder():
    pass


if __name__ == "__main__":
    logging.info("logrecorder is called")   
    logrecorder()
    