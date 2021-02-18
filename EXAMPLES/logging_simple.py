#!/usr/bin/env python

import logging

logging.basicConfig(
    filename='../TEMP/simple.log',
    level=logging.WARNING,
) # <1>

logging.warning('This is a warning') # <2>
logging.debug('This message is for debugging') # <3>
logging.error('This is an ERROR') # <4>
logging.critical('This is ***CRITICAL***') # <5>
logging.info('The capital of North Dakota is Bismark') # <6>
for i in range(10):
    logging.info("log message", i)

print(logging.DEBUG)
print(logging.INFO)
print(logging.WARNING)
print(logging.ERROR)
print(logging.CRITICAL)