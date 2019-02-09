import logging
import re
from datetime import datetime
from functools import partial
from typing import List

import arrow
import jmespath

logger = logging.getLogger(__name__)


class CustomFunctions(jmespath.functions.Functions):
    @jmespath.functions.signature({"types": []})
    def _func_to_int(self, s):
        try:
            return int(s)
        except (TypeError, ValueError):
            if isinstance(s, str):
                return extract_int(s)

    @jmespath.functions.signature({"types": []})
    def _func_to_str(self, s):
        try:
            return str(s)
        except:
            pass

    @jmespath.functions.signature({"types": []})
    def _func_to_percent(self, s):
        try:
            return extract_int(s) / 100
        except:
            pass

    @jmespath.functions.signature({"types": []})
    def _func_to_float(self, s):
        if isinstance(s, str):
            return extract_float(s)

    @jmespath.functions.signature({"types": []})
    def _func_to_percent_value(self, s):
        try:
            return extract_float(s) / 100
        except:
            pass

    @jmespath.functions.signature({"types": []}, {"types": []})
    def _func_to_datetime(self, text, fmt=None, tzinfo='Asia/Shanghai'):
        try:
            return ensure_datetime(text, fmt, tzinfo)
        except:
            return

    @jmespath.functions.signature({"types": []})
    def _func_merge_array(self, dlist):
        data = {}
        for d in dlist or []:
            data.update(d)
        return data


options = jmespath.Options(custom_functions=CustomFunctions())
jmespath_search = partial(jmespath.search, options=options)


def ensure_str(data, encoding=None) -> str:
    """确保数据为字符串
    """
    if isinstance(data, str):
        return data

    if not isinstance(data, bytes):
        raise ValueError(f'{type(data)} not supported')

    if encoding:
        return data.decode(encoding)

    default_codes = ('u8', 'gbk', 'gb2312')
    if encoding is None:
        for code in default_codes:
            try:
                return data.decode(code)
            except UnicodeDecodeError:
                continue
        else:
            raise ValueError('Cannot decode data')


def extract_ints(text) -> List[int]:
    """提取
    """
    text = ensure_str(text)
    pat = re.compile(r"\d+")
    res = pat.findall(text)
    if res:
        return [int(i) for i in res]


def extract_int(text) -> int:
    v = extract_ints(text)
    return v[0] if v else v


def extract_floats(text) -> List[float]:
    text = ensure_str(text)

    pat = re.compile(r"(\d+(\.\d+)*)")
    res = pat.findall(text)
    if res:
        return [float(i[0]) for i in res]


def extract_float(text) -> float:
    v = extract_floats(text)
    return v[0] if v else v


def ensure_datetime(text: str, fmt: str = None, tzinfo=None) -> datetime:
    if isinstance(text, datetime):
        return text
    if fmt:
        return arrow.get(text, fmt, tzinfo=tzinfo).datetime
    else:
        return arrow.get(text, tzinfo=tzinfo).datetime
