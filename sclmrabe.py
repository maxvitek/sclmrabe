import re
import random


def scramble(string):
    words = re.findall(r"[\w]+|[^\w]+", string)
    reply = []
    for word in words:
        if len(word) < 4:
            reply.append(word)
        else:
            prefix = word[:2]
            suffix = word[-1:]
            stem = word[2:-1]
            reply.append(
                         prefix + 
                         ''.join(random.sample(stem,len(stem))) +
                         suffix
                         )
    return ''.join(reply)
