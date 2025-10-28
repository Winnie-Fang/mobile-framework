class LAN:
    ZH = 'ZH'
    EN = 'EN'


def CASEID(LAN: str, TS: int, ID_: int):
    """
    [EN01-01]
    """
    return f'[{LAN}{str(TS).zfill(2)}-{str(ID_).zfill(2)}]'


def ZHID(TS: int, ID_: int):
    return CASEID(LAN.ZH, TS, ID_)


def ENID(TS: int, ID_: int):
    return CASEID(LAN.EN, TS, ID_)
