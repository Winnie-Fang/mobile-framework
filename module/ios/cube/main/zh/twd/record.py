class FROM:
    ANY = {}

    BANK = {'id': '013', 'rb': '(013)', 'zh': '國泰世華', 'idzh': '013 國泰世華', 'rbzh': '(013) 國泰世華'}
    NAME = ''
    ID12 = ''
    ID16 = ''
    INFO = {'nm12': '', 'nm16': '', 'nmbr12': '', 'nmbr16': ''}

    BEFORE_TOTAL_AMOUNT = {'amt': '', 'ams': '', 'grp': '', 'int': ''}
    BEFORE_TOTAL_AVAILABLE_BALANCE = {'amt': '', 'ams': '', 'grp': '', 'int': ''}
    BEFORE_TOTAL_ACCOUNT_BALANCE = {'amt': '', 'ams': '', 'grp': '', 'int': ''}
    BEFORE_ACCOUNT_BALANCE = {'amt': '', 'ams': '', 'grp': '', 'int': ''}

    AFTER_TOTAL_AMOUNT = {'amt': '', 'ams': '', 'grp': '', 'int': ''}
    AFTER_TOTAL_AVAILABLE_BALANCE = {'amt': '', 'ams': '', 'grp': '', 'int': ''}
    AFTER_TOTAL_ACCOUNT_BALANCE = {'amt': '', 'ams': '', 'grp': '', 'int': ''}
    AFTER_ACCOUNT_BALANCE = {'amt': '', 'ams': '', 'grp': '', 'int': ''}


class TO:
    ANY = {}

    BANK = {'id': '', 'rb': '', 'zh': '', 'idzh': '', 'rbzh': ''}
    NAME = ''
    ID12 = ''
    ID16 = ''
    INFO = {'nm12': '', 'nm16': '', 'bc16': '', 'br16': '', 'nmbr12': '', 'nmbr16': ''}

    BEFORE_TOTAL_AMOUNT = {'amt': '', 'ams': '', 'grp': '', 'int': ''}
    BEFORE_TOTAL_AVAILABLE_BALANCE = {'amt': '', 'ams': '', 'grp': '', 'int': ''}
    BEFORE_TOTAL_ACCOUNT_BALANCE = {'amt': '', 'ams': '', 'grp': '', 'int': ''}
    BEFORE_ACCOUNT_BALANCE = {'amt': '', 'ams': '', 'grp': '', 'int': ''}

    AFTER_TOTAL_AMOUNT = {'amt': '', 'ams': '', 'grp': '', 'int': ''}
    AFTER_TOTAL_AVAILABLE_BALANCE = {'amt': '', 'ams': '', 'grp': '', 'int': ''}
    AFTER_TOTAL_ACCOUNT_BALANCE = {'amt': '', 'ams': '', 'grp': '', 'int': ''}
    AFTER_ACCOUNT_BALANCE = {'amt': '', 'ams': '', 'grp': '', 'int': ''}


class TXN:
    ANY = {}

    TYPE = ''
    BANK_TYPE = ''
    SCHEDULED_TYPE = ''
    VERIFY_CODE = ['555666', '666555', '563729']

    AMOUNT = {'amt': '', 'ams': '', 'grp': '', 'int': ''}
    REMARK = {'input': '', 'info': ''}
    START_DATETIME = ''
    END_DATETIME = ''
    EXECUTE_DATETIME = {'ori': '', 'com': ''}
    EXECUTE_DATE = {'ori': '', 'com': ''}
    TXN_NO = ''
    STAN_NO = ''
    FEE = {'amt': '', 'ams': '', 'grp': '', 'int': ''}

    SCHEDULED_DATE = {'ori': '', 'com': '', 'yyyy': '', 'm': '', 'mm': '', 'd': '', 'dd': '', 'ymzh': ''}
    SCHEDULED_WEEKDAY = {'index': '', 'zhcom': '', 'zhper': '', 'zhspc': ''}
    SCHEDULED_START_DATE = {'ori': '', 'com': '', 'yyyy': '', 'm': '', 'mm': '', 'd': '', 'dd': '', 'ymzh': ''}
    SCHEDULED_END_DATE = {'ori': '', 'com': '', 'yyyy': '', 'm': '', 'mm': '', 'd': '', 'dd': '', 'ymzh': ''}
    SCHEDULED_PERIOD = ''


class K:
    ORI = 'ori'
    COM = 'com'
    ID = 'id'
    RB = 'rb'
    ZH = 'zh'
    IDZH = 'idzh'
    RBZH = 'rbzh'
    NM12 = 'nm12'
    NM16 = 'nm16'
    NMBR12 = 'nmbr12'
    NMBR16 = 'nmbr16'
    BC16 = 'bc16'
    BR16 = 'br16'
    AMT = 'amt'
    AMS = 'ams'
    GRP = 'grp'
    INT = 'int'
    INDEX = 'index'
    INPUT = 'input'
    INFO = 'info'
    START = 'start'
    ACTORI = 'actori'
    ACTCOM = 'actcom'
    END = 'end'
    YYYY = 'yyyy'
    M = 'm'
    MM = 'mm'
    D = 'd'
    DD = 'dd'
    YMZH = 'ymzh'
    ZHCOM = 'zhcom'
    ZHPER = 'zhper'
    ZHSPC = 'zhspc'
