from datetime import datetime
import logging
import json_log_formatter

class CustomizedJSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message: str, extra: dict, record: logging.LogRecord) -> dict:
        extra['message'] = message
        #extra['user_id'] = current_user_id()
        #extra['ip'] = current_ip()

        # Include builtins
        extra['time'] = datetime.utcnow()
        extra['level'] = record.levelname
        #extra['name'] = record.name
        extra['filename'] = record.filename
        extra['funcName'] = record.funcName
        extra['module'] = record.module
        extra['pathname'] = record.pathname

        #if 'time' not in extra:
        #    extra['time'] = django.utils.timezone.now()

        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)

        return extra
