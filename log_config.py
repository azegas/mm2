# https://docs.python.org/3/howto/logging.html


# DEBUG - Detailed information, typically of interest only when diagnosing problems.
# INFO - Confirmation that things are working as expected.
# WARNING - An indication that something unexpected happened, or indicative of
# some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR - Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL - A serious error, indicating that the program itself may be unable to continue running.

# Using logging packages instead of log() from utils.py, because each time I
# want to debug the app, I have to add various print statements to the app,
# then make sure I don't commit those print statements to version control when
# I am done debugging (most of the time deleting those statements, then having
# to rewrite them again next time I am debugging). Logging is a built in
# package, so no additional dependencies. Logging messages can be in the code,
# they are not intrusive. Whether the log messages are printed out or not can
# be controlled by a single variable - level=logging.INFO. Set it to DEBUG and
# you will see the debug logs.

import os
import logging

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
    level="INFO",
)

logger = logging.getLogger(__name__)
