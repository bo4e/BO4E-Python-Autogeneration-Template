from enum import Enum


class NetznutzungRechnungstyp(str, Enum):
    """
    Abbildung verschiedener in der INVOIC angegebenen Rechnungstypen.
    """

    ABSCHLUSSRECHNUNG = "ABSCHLUSSRECHNUNG"
    ABSCHLAGSRECHNUNG = "ABSCHLAGSRECHNUNG"
    TURNUSRECHNUNG = "TURNUSRECHNUNG"
    MONATSRECHNUNG = "MONATSRECHNUNG"
    WIMRECHNUNG = "WIMRECHNUNG"
    ZWISCHENRECHNUNG = "ZWISCHENRECHNUNG"
    INTEGRIERTE_13_TE_RECHNUNG = "INTEGRIERTE_13TE_RECHNUNG"
    ZUSAETZLICHE_13_TE_RECHNUNG = "ZUSAETZLICHE_13TE_RECHNUNG"
    MEHRMINDERMENGENRECHNUNG = "MEHRMINDERMENGENRECHNUNG"
