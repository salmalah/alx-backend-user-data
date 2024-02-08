#!/usr/bin/env python3
"""
This module to define filtered_logger
"""


import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    function called filter_datum that returns the log message obfuscated
    """
    for i in fields:
        message = re.sub(rf"{i}=(.*?)\{separator}",
                         f'{i}={redaction}{separator}', message)
    return message
