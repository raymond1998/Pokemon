from common import *
_logfmt = \
'''================================================================================
Level		: %s
Type		: %s
FileName	: %s
LineNumber	: %d
Timestamp	: %d
RuntimeMsg	: %s
Description	: %s
'''

class GeneralException(Exception):
    UNEXPECTED = -1
    EXPECTED = 0
    
    _descriptions_ =\
                   {
                       -1:"Unexpected Exception",
                       0:"Expected Exception",
                    }

    def __init__(self, file_name, line_no, msg='', typ=UNEXPECTED):
        self.msg = msg
        if typ != self.EXPECTED: log(_logfmt%("Exception", str(typ), str(file_name), int(line_no), getTimestamp(), str(msg), self._describe(typ)), "Exception.log")

    def _describe(self, typ):
        if typ in self._descriptions_: return self._descriptions_[typ] 
        else: return ""
        
    def __str__(self): return self.msg

def _main(): raise GeneralException(getName(), getLine(), "An Exception Is Raised!")
if __name__ == "__main__": exit(_main())
