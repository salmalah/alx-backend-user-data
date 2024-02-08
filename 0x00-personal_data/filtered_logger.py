#!/usr/bin/env python3
"""
This module to define filtered_logger
"""


import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    function called filter_datum that returns the log message obfuscated
    """
    for i in fields:
        message = re.sub(rf"{i}=(.*?)\{separator}",
                         f'{i}={redaction}{separator}', message)
    return message

class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        return re.sub(
            r'(?<=\b(?:' + '|'.join(self.fields) + r')=)[^{}]*(?=[{}])'.format(
                self.SEPARATOR, self.SEPARATOR
            ),
            self.REDACTION,
            record.getMessage(),
        )
