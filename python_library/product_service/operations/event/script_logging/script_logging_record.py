import logging

class JSONLogRecord(logging.LogRecord):
    pass
    #def getMessage(self):
        #return super().getMessage()
        #return json.dumps(self.msg)

def makeRecord(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    rv = JSONLogRecord(name, level, fn, lno, msg, args)
    return rv

logging.Logger.makeRecord = makeRecord
