from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

logging.info("Welcome to the custom log")

try:
    a = 1 / 0
except Exception as e:
    raise USvisaException(e, sys) from e
