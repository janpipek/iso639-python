import os
import codecs

# Python 3.4 compatibility
if not 'unicode' in dir():
    unicode = str

class NonExistentLanguageError(RuntimeError):
    pass

def find(whatever=None, language=None, iso639_1=None, iso639_2=None):
    if whatever:
        keys = [u'name', u'iso639_1', u'iso639_2_b', u'iso639_2_t']
        val = whatever
    elif language:
        keys = [u'name']
        val = language
    elif iso639_1:
        keys = [u'iso639_1']
        val = iso639_1
    elif iso639_2:
        keys = [u'iso639_2_b', u'iso639_2_t']
        val = iso639_2
    else:
        raise ValueError('Invalid search criteria.')
    val = unicode(val)
    return next((item for item in data if any(item[key] == val for key in keys)), None)


def is_valid639_1(code):
    if len(code) != 2:
        return False
    return find(iso639_1=code) is not None


def is_valid639_2(code):
    if len(code) != 3:
        return False
    return find(iso639_2=code) is not None


def to_iso639_1(key):
    item = find(whatever=key)
    if not item:
        raise NonExistentLanguageError('Language does not exist.')
    return item[u'iso639_1']


def to_iso639_2(key, type='B'):
    if not type in ('B', 'T'):
        raise ValueError('Type must be either "B" or "T".')
    item = find(whatever=key)
    if not item:
        raise NonExistentLanguageError('Language does not exist.')
    if type == 'T' and item[u'iso639_2_t']:
        return item[u'iso639_2_t']
    return item[u'iso639_2_b']


def to_name(key):
    item = find(whatever=key)
    if not item:
        raise NonExistentLanguageError('Language does not exist.')
    return item[u'name']


def _load_data():
    def parse_line(line):
        data = line.strip().split('|')
        return {
            u'iso639_2_b': data[0],
            u'iso639_2_t': data[1],
            u'iso639_1': data[2],
            u'name': data[3]
        }

    data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ISO-639-2_utf-8.txt')
    with codecs.open(data_file, 'r', 'UTF-8') as f:
        data = [ parse_line(line) for line in f]
    return data

data = _load_data()

