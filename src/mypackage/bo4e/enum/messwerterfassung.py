from enum import Enum


class Messwerterfassung(str, Enum):
    """
    Die Messwerterfassung des Zählers
    """

    FERNAUSLESBAR = "FERNAUSLESBAR"
    MANUELL_AUSGELESENE = "MANUELL_AUSGELESENE"
