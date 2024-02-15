from enum import Enum


class Kalkulationsmethode(str, Enum):
    """
    Auflistung der verschiedenen Berechnungsmethoden für ein Preisblatt.
    """

    STUFEN = "STUFEN"
    ZONEN = "ZONEN"
    VORZONEN_GP = "VORZONEN_GP"
    SIGMOID = "SIGMOID"
    BLINDARBEIT_GT_50_PROZENT = "BLINDARBEIT_GT_50_PROZENT"
    BLINDARBEIT_GT_40_PROZENT = "BLINDARBEIT_GT_40_PROZENT"
    BLINDARBEIT_MIT_FREIMENGE = "BLINDARBEIT_MIT_FREIMENGE"
    AP_GP_ZONEN = "AP_GP_ZONEN"
    LP_INSTALL_LEISTUNG = "LP_INSTALL_LEISTUNG"
    AP_TRANSPORT_ODER_VERTEILNETZ = "AP_TRANSPORT_ODER_VERTEILNETZ"
    AP_TRANSPORT_ODER_VERTEILNETZ_ORTSVERTEILNETZ_SIGMOID = "AP_TRANSPORT_ODER_VERTEILNETZ_ORTSVERTEILNETZ_SIGMOID"
    LP_JAHRESVERBRAUCH = "LP_JAHRESVERBRAUCH"
    LP_TRANSPORT_ODER_VERTEILNETZ = "LP_TRANSPORT_ODER_VERTEILNETZ"
    LP_TRANSPORT_ODER_VERTEILNETZ_ORTSVERTEILNETZ_SIGMOID = "LP_TRANSPORT_ODER_VERTEILNETZ_ORTSVERTEILNETZ_SIGMOID"
    FUNKTIONEN = "FUNKTIONEN"
    VERBRAUCH_UEBER_SLP_GRENZE_FUNKTIONSBEZOGEN_WEITERE_BERECHNUNG_ALS_LGK = (
        "VERBRAUCH_UEBER_SLP_GRENZE_FUNKTIONSBEZOGEN_WEITERE_BERECHNUNG_ALS_LGK"
    )