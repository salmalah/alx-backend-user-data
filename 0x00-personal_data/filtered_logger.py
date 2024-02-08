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
    """
    RedactingFormatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize RedactingFormatter."""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Format log record with redaction."""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
