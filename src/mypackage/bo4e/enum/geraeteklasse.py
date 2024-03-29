from enum import Enum


class Geraeteklasse(str, Enum):
    """
    Auflistung möglicher übergreifenden Geräteklassen.
    """

    WANDLER = "WANDLER"
    KOMMUNIKATIONSEINRICHTUNG = "KOMMUNIKATIONSEINRICHTUNG"
    TECHNISCHE_STEUEREINRICHTUNG = "TECHNISCHE_STEUEREINRICHTUNG"
    MENGENUMWERTER = "MENGENUMWERTER"
    SMARTMETER_GATEWAY = "SMARTMETER_GATEWAY"
    STEUERBOX = "STEUERBOX"
    ZAEHLEINRICHTUNG = "ZAEHLEINRICHTUNG"
