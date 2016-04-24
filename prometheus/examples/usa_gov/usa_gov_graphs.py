from pandas import DataFrame
from pprint import pprint

from prometheus.common import utils

TIMEZONE_KEY = "tz"


def plot_most_common_timezones(data_set, count=10):
    frame = DataFrame(data=data_set)
    timezones = frame[TIMEZONE_KEY]
    timezones = utils.soft_wrangle_data(timezones)

    print("The %s most common timezones are:" % count)
    timezones_count = timezones.value_counts()
    pprint(timezones_count[:count])

    timezones_count[:count].plot(kind="barh", rot=0)
