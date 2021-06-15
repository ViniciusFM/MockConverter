import json
import re

PLACEHOLDER = "#"
VARSYMBOL = "#"
VARSYMBOL_RE = "\#"
PARSE_REGEX = VARSYMBOL_RE+"[^"+VARSYMBOL_RE+"]+"+VARSYMBOL_RE
MATCH_REGEX = "[^"+VARSYMBOL_RE+"]*("+VARSYMBOL_RE+"[^"+VARSYMBOL_RE+"]+"+VARSYMBOL_RE+"[^"+VARSYMBOL_RE+"]*)*"

class NotPatternFileException(Exception):
    def __init__(self, msg, *args):
        Exception.__init__(self, *args)
        self.__prefix = "NotPatternFileException: "
        if msg:
            self.message = msg
        else:
            self.message = "Unknown"
    def __str__(self):
        return self.__prefix + self.message

class PatternTextConverter(object):
    def __init__(self, jsonFilePath:str):
        self.__jsonPath = jsonFilePath
        self.__model = None
        with open(self.__jsonPath, "r") as f:
            try:
                self.__data = json.load(f)
                if type(self.__data) == list:
                    self.__model = self.__data[0]
                elif type(self.__data) == dict:
                    self.__model = self.__data
                else:
                    raise NotPatternFileException
            except json.JSONDecodeError as err:
                raise NotPatternFileException(err.msg)
        self.__keys = [*self.__model.keys()]
        self.pattern = None

    def getModelAsString(self):
        return json.dumps(self.__model, indent=4)
    
    def __convert(self, value:dict):
        if not self.pattern: return None
        npattern = re.sub(PARSE_REGEX, PLACEHOLDER, self.pattern)
        parts = re.findall(PARSE_REGEX, self.pattern)
        pvars = [re.sub(VARSYMBOL_RE, '', part) for part in parts]
        resp = list(npattern)
        vrs = []
        for v in pvars:
            if not v in value: return None
            vrs.append(value[v])
        j = 0
        for i in range(0, len(resp)):
            if(resp[i] == '#'):
                resp[i] = str(vrs[j])
                j += 1
        return ''.join(resp)

    def getParsePreview(self, pattern:str):
        if re.fullmatch(MATCH_REGEX, pattern):
            self.pattern = pattern
            return self.__convert(self.__model)
        return None

    def isPossibleToConvert(self):
        if not self.pattern: return False
        modelConverted = self.__convert(self.__model)
        return True if modelConverted else False

    def getConvertedData(self):
        converted = ''
        if type(self.__data) == list:
            for jsonObj in self.__data:
                resp = self.__convert(jsonObj)
                if resp:
                    converted += resp
        elif type(self.__data) == dict:
            resp = self.__convert(self.__data)
            if resp:
                converted = resp
        return converted
