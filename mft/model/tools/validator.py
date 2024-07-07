import re


def pattern_validator(pattern, message):
    def inner1(function_name):
        def inner2(self, text):
            if isinstance(text, str) and re.match(pattern, text):
                result = function_name(self, text)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


# todo: proofreading errors(date and datetime)
def date_time_validator(message):
    def inner1(function_name):
        def inner2(self, date_time_param):
            if isinstance(date_time_param, date):
                result = function_name(self, date_time_param)
            elif isinstance(date_time_param, str):
                date_time_param = date_time_param.replace('/', '-')
                try:
                    date_time_param = datetime.strptime(date_time_param, '%Y-%m-%d %H:%M:%S').date()
                    result = function_name(self, date_time_param)
                except:
                    raise ValueError(message)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1
