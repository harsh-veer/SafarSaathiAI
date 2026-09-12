# orjson.py  — pure-Python shim to replace the blocked native orjson
import json as _json

OPT_NON_STR_KEYS = 1
OPT_SERIALIZE_NUMPY = 2
OPT_INDENT_2 = 4
OPT_OMIT_MICROSECONDS = 8
OPT_NAIVE_UTC = 16
OPT_PASSTHROUGH_DATETIME = 32
OPT_SORT_KEYS = 64
OPT_STRICT_INTEGER = 128
OPT_UTC_Z = 256

JSONDecodeError = _json.JSONDecodeError

def dumps(obj, default=None, option=None):
    return _json.dumps(obj, default=default).encode()

def loads(data):
    if isinstance(data, (bytes, bytearray, memoryview)):
        data = data.decode()
    return _json.loads(data)