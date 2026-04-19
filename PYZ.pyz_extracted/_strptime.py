# Source Generated with Decompyle++
# File: _strptime.pyc (Python 3.12)

'''Strptime-related classes and functions.

CLASSES:
    LocaleTime -- Discovers and stores locale-specific time information
    TimeRE -- Creates regexes for pattern matching a string of text containing
                time information

FUNCTIONS:
    _getlang -- Figure out what language is being used for the locale
    strptime -- Calculates the time struct represented by the passed-in string

'''
import time
import locale
import calendar
from re import compile as re_compile
from re import sub as re_sub
from re import IGNORECASE
from re import escape as re_escape
from datetime import date as datetime_date, timedelta as datetime_timedelta, timezone as datetime_timezone
from _thread import allocate_lock as _thread_allocate_lock
__all__ = []

def _getlang():
    return locale.getlocale(locale.LC_TIME)


def _findall(haystack, needle):
    pass
# WARNING: Decompyle incomplete


class LocaleTime(object):
    '''Stores and handles locale-specific information related to time.

    ATTRIBUTES:
        f_weekday -- full weekday names (7-item list)
        a_weekday -- abbreviated weekday names (7-item list)
        f_month -- full month names (13-item list; dummy value in [0], which
                    is added by code)
        a_month -- abbreviated month names (13-item list, dummy value in
                    [0], which is added by code)
        am_pm -- AM/PM representation (2-item list)
        LC_date_time -- format string for date/time representation (string)
        LC_date -- format string for date representation (string)
        LC_time -- format string for time representation (string)
        timezone -- daylight- and non-daylight-savings timezone representation
                    (2-item list of sets)
        lang -- Language used by instance (2-item tuple)
    '''
    
    def __init__(self):
        '''Set all attributes.

        Order of methods called matters for dependency reasons.

        The locale language is set at the offset and then checked again before
        exiting.  This is to make sure that the attributes were not set with a
        mix of information from more than one locale.  This would most likely
        happen when using threads where one thread calls a locale-dependent
        function while another thread changes the locale while the function in
        the other thread is still running.  Proper coding would call for
        locks to prevent changing the locale while locale-dependent code is
        running.  The check here is done in case someone does not think about
        doing this.

        Only other possible issue is if someone changed the timezone and did
        not call tz.tzset .  That is an issue for the programmer, though,
        since changing the timezone is worthless without that call.

        '''
        self.lang = _getlang()
        self.__calc_weekday()
        self.__calc_month()
        self.__calc_am_pm()
        self.__calc_timezone()
        self.__calc_date_time()
        if _getlang() != self.lang:
            raise ValueError('locale changed during initialization')
        if time.tzname != self.tzname or time.daylight != self.daylight:
            raise ValueError('timezone changed during initialization')

    
    def __calc_weekday(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __calc_month(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __calc_am_pm(self):
        am_pm = []
        for hour in (1, 22):
            time_tuple = time.struct_time((1999, 3, 17, hour, 44, 55, 2, 76, 0))
            am_pm.append(time.strftime('%p', time_tuple).lower().strip())
        self.am_pm = am_pm

    
    def __calc_date_time(self):
        time_tuple = time.struct_time((1999, 3, 17, 22, 44, 55, 2, 76, 0))
        time_tuple2 = time.struct_time((1999, 1, 3, 1, 1, 1, 6, 3, 0))
        replacement_pairs = [
            ('1999', '%Y'),
            ('99', '%y'),
            ('22', '%H'),
            ('44', '%M'),
            ('55', '%S'),
            ('76', '%j'),
            ('17', '%d'),
            ('03', '%m'),
            ('3', '%m'),
            ('2', '%w'),
            ('10', '%I'),
            ('١٩٩٩', '%Y'),
            ('٩٩', '%Oy'),
            ('٢٢', '%OH'),
            ('٤٤', '%OM'),
            ('٥٥', '%OS'),
            ('١٧', '%Od'),
            ('٠٣', '%Om'),
            ('٣', '%Om'),
            ('٢', '%Ow'),
            ('١٠', '%OI')]
        date_time = []
        for directive in ('%c', '%x', '%X'):
            current_format = time.strftime(directive, time_tuple).lower()
            current_format = current_format.replace('%', '%%')
            (lst, fmt) = self.__find_weekday_format(directive)
            if lst:
                current_format = current_format.replace(lst[2], fmt, 1)
            (lst, fmt) = self.__find_month_format(directive)
            if lst:
                current_format = current_format.replace(lst[3], fmt, 1)
            if self.am_pm[1]:
                current_format = current_format.replace(self.am_pm[1], '%p')
            for tz_values in self.timezone:
                for tz in tz_values:
                    if not tz:
                        continue
                    current_format = current_format.replace(tz, '%Z')
            current_format = re_sub('\\d(?<![0-9])', (lambda m: chr(1632 + int(m[0]))), current_format)
            for old, new in replacement_pairs:
                current_format = current_format.replace(old, new)
            if '00' in time.strftime(directive, time_tuple2):
                U_W = '%W'
            else:
                U_W = '%U'
            current_format = current_format.replace('11', U_W)
            date_time.append(current_format)
        self.LC_date_time = date_time[0]
        self.LC_date = date_time[1]
        self.LC_time = date_time[2]

    
    def __find_month_format(self, directive):
        '''Find the month format appropriate for the current locale.

        In some locales (for example French and Hebrew), the default month
        used in __calc_date_time has the same name in full and abbreviated
        form.  Also, the month name can by accident match other part of the
        representation: the day of the week name (for example in Morisyen)
        or the month number (for example in Japanese).  Thus, cycle months
        of the year and find all positions that match the month name for
        each month,  If no common positions are found, the representation
        does not use the month name.
        '''
        full_indices = None
        abbr_indices = None
    # WARNING: Decompyle incomplete

    
    def __find_weekday_format(self, directive):
        '''Find the day of the week format appropriate for the current locale.

        Similar to __find_month_format().
        '''
        full_indices = None
        abbr_indices = None
    # WARNING: Decompyle incomplete

    
    def __calc_timezone(self):
        
        try:
            time.tzset()
            self.tzname = time.tzname
            self.daylight = time.daylight
            no_saving = frozenset({
                'utc',
                'gmt',
                self.tzname[0].lower()})
            if self.daylight:
                has_saving = frozenset({
                    self.tzname[1].lower()})
            else:
                has_saving = frozenset()
            self.timezone = (no_saving, has_saving)
            return None
        except AttributeError:
            continue




class TimeRE(dict):
    pass
# WARNING: Decompyle incomplete

_cache_lock = _thread_allocate_lock()
_TimeRE_cache = TimeRE()
_CACHE_MAX_SIZE = 5
_regex_cache = { }

def _calc_julian_from_U_or_W(year, week_of_year, day_of_week, week_starts_Mon):
    '''Calculate the Julian day based on the year, week of the year, and day of
    the week, with week_start_day representing whether the week of the year
    assumes the week starts on Sunday or Monday (6 or 0).'''
    first_weekday = datetime_date(year, 1, 1).weekday()
    if not week_starts_Mon:
        first_weekday = (first_weekday + 1) % 7
        day_of_week = (day_of_week + 1) % 7
    week_0_length = (7 - first_weekday) % 7
    if week_of_year == 0:
        return 1 + day_of_week - first_weekday
    days_to_week = None + 7 * (week_of_year - 1)
    return 1 + days_to_week + day_of_week


def _strptime(data_string, format = ('%a %b %d %H:%M:%S %Y',)):
    '''Return a 2-tuple consisting of a time struct and an int containing
    the number of microseconds based on the input string and the
    format string.'''
    global _TimeRE_cache
    for index, arg in enumerate([
        data_string,
        format]):
        if isinstance(arg, str):
            continue
        msg = 'strptime() argument {} must be str, not {}'
        raise TypeError(msg.format(index, type(arg)))
    _cache_lock
    locale_time = _TimeRE_cache.locale_time
    if _getlang() != locale_time.lang and time.tzname != locale_time.tzname or time.daylight != locale_time.daylight:
        _TimeRE_cache = TimeRE()
        _regex_cache.clear()
        locale_time = _TimeRE_cache.locale_time
    if len(_regex_cache) > _CACHE_MAX_SIZE:
        _regex_cache.clear()
    format_regex = _regex_cache.get(format)
    if not format_regex:
        format_regex = _TimeRE_cache.compile(format)
        _regex_cache[format] = format_regex
    None(None, None)
# WARNING: Decompyle incomplete


def _strptime_time(data_string, format = ('%a %b %d %H:%M:%S %Y',)):
    '''Return a time struct based on the input string and the
    format string.'''
    tt = _strptime(data_string, format)[0]
    return time.struct_time(tt[:time._STRUCT_TM_ITEMS])


def _strptime_datetime(cls, data_string, format = ('%a %b %d %H:%M:%S %Y',)):
    '''Return a class cls instance based on the input string and the
    format string.'''
    (tt, fraction, gmtoff_fraction) = _strptime(data_string, format)
    (tzname, gmtoff) = tt[-2:]
    args = tt[:6] + (fraction,)
# WARNING: Decompyle incomplete

