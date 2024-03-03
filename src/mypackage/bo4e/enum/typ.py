from enum import Enum


class Typ(str, Enum):
    """
    Auflistung sämtlicher existierender Geschäftsobjekte.
    """

    ANGEBOT = "ANGEBOT"
    ANSPRECHPARTNER = "ANSPRECHPARTNER"
    AUSSCHREIBUNG = "AUSSCHREIBUNG"
    BUENDELVERTRAG = "BUENDELVERTRAG"
    ENERGIEMENGE = "ENERGIEMENGE"
    FREMDKOSTEN = "FREMDKOSTEN"
    GERAET = "GERAET"
    GESCHAEFTSOBJEKT = "GESCHAEFTSOBJEKT"
    GESCHAEFTSPARTNER = "GESCHAEFTSPARTNER"
    KOSTEN = "KOSTEN"
    LASTGANG = "LASTGANG"
    MARKTLOKATION = "MARKTLOKATION"
    MESSLOKATION = "MESSLOKATION"
    MARKTTEILNEHMER = "MARKTTEILNEHMER"
    NETZNUTZUNGSRECHNUNG = "NETZNUTZUNGSRECHNUNG"
    PREISBLATT = "PREISBLATT"
    PREISBLATTDIENSTLEISTUNG = "PREISBLATTDIENSTLEISTUNG"
    PREISBLATTHARDWARE = "PREISBLATTHARDWARE"
    PREISBLATTKONZESSIONSABGABE = "PREISBLATTKONZESSIONSABGABE"
    PREISBLATTMESSUNG = "PREISBLATTMESSUNG"
    PREISBLATTNETZNUTZUNG = "PREISBLATTNETZNUTZUNG"
    PREISBLATTUMLAGEN = "PREISBLATTUMLAGEN"
    RECHNUNG = "RECHNUNG"
    REGION = "REGION"
    REGIONALTARIF = "REGIONALTARIF"
    STANDORTEIGENSCHAFTEN = "STANDORTEIGENSCHAFTEN"
    TARIF = "TARIF"
    TARIFINFO = "TARIFINFO"
    TARIFKOSTEN = "TARIFKOSTEN"
    TARIFPREISBLATT = "TARIFPREISBLATT"
    VERTRAG = "VERTRAG"
    ZAEHLER = "ZAEHLER"
    ZEITREIHE = "ZEITREIHE"
