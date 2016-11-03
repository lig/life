import re

from life import RULES


rules_regex = re.compile('^B(\d*)/S(\d*)$')

BORN, SURVIVE = [
    [int(d) for d in list(r)]
    for r in rules_regex.match(RULES).groups()]
