from datetime import datetime
from functools import partial
from datetime import timedelta


def convert_to_datetime(date_string: str, format: str = "%Y%m%d"):
    return datetime.strptime(date_string, format)


def strip_text(text: str, strip: str = "/"):
    return text.strip(strip)


def strip_dict_text(dict_to_strip: dict, key: str, strip: str = "/"):
    dict_to_strip[key] = dict_to_strip[key].strip(strip)
    return dict_to_strip


def get_values_dict(dict_to_value: dict, key: str):
    return map(lambda x: x[key], dict_to_value)


def strip_prefix(prefix_list: list, prefix_col: str = "Prefix"):
    return map(partial(strip_dict_text, key=prefix_col), prefix_list)


def convert_list_to_datetime(prefix_list: list, format: str = "%Y%m%d"):
    return map(partial(convert_to_datetime, format=format), prefix_list)


def prefix_to_remove(datetimes: list, hours_back=71):
    days_ago = datetime.now() - timedelta(hours=hours_back)
    return filter(lambda x: x < days_ago, datetimes)


def to_strftime(strptime_list: list, strf_format: str):
    return map(lambda x: x.strftime(strf_format), strptime_list)


def get_removal_prefix(list_prefixes: list):
    stripped = strip_prefix(list_prefixes)
    values = get_values_dict(stripped, "Prefix")
    datetimes = convert_list_to_datetime(values)
    to_remove = prefix_to_remove(datetimes)
    remove_prefix = to_strftime(to_remove, strf_format="%Y%m%d")
    return remove_prefix
