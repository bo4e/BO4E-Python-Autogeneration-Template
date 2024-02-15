from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..com.betrag import Betrag
from ..com.rechnungsposition import Rechnungsposition
from ..com.steuerbetrag import Steuerbetrag
from ..com.zeitraum import Zeitraum
from ..enum.netznutzung_rechnungsart import NetznutzungRechnungsart
from ..enum.netznutzung_rechnungstyp import NetznutzungRechnungstyp
from ..enum.rechnungsstatus import Rechnungsstatus
from ..enum.rechnungstyp import Rechnungstyp
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from .geschaeftspartner import Geschaeftspartner
from .marktlokation import Marktlokation
from .messlokation import Messlokation


class Rechnung(BaseModel):
    """
    Modell für die Abbildung von Rechnungen und Netznutzungsrechnungen im Kontext der Energiewirtschaft;

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Rechnung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Rechnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Rechnung.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    faelligkeitsdatum: datetime | None = Field(default=None, title="Faelligkeitsdatum")
    gesamtbrutto: Betrag | None = None
    gesamtnetto: Betrag | None = None
    gesamtsteuer: Betrag | None = None
    ist_original: bool | None = Field(default=None, alias="istOriginal", title="Istoriginal")
    ist_simuliert: bool | None = Field(default=None, alias="istSimuliert", title="Istsimuliert")
    ist_storno: bool | None = Field(default=None, alias="istStorno", title="Iststorno")
    marktlokation: Marktlokation | None = None
    messlokation: Messlokation | None = None
    netznutzungrechnungsart: NetznutzungRechnungsart | None = None
    netznutzungrechnungstyp: NetznutzungRechnungstyp | None = None
    original_rechnungsnummer: str | None = Field(
        default=None, alias="originalRechnungsnummer", title="Originalrechnungsnummer"
    )
    rabatt_brutto: Betrag | None = Field(default=None, alias="rabattBrutto")
    rechnungsdatum: datetime | None = Field(default=None, title="Rechnungsdatum")
    rechnungsempfaenger: Geschaeftspartner | None = None
    rechnungsersteller: Geschaeftspartner | None = None
    rechnungsnummer: str | None = Field(default=None, title="Rechnungsnummer")
    rechnungsperiode: Zeitraum | None = None
    rechnungspositionen: list[Rechnungsposition] | None = Field(default=None, title="Rechnungspositionen")
    rechnungsstatus: Rechnungsstatus | None = None
    rechnungstitel: str | None = Field(default=None, title="Rechnungstitel")
    rechnungstyp: Rechnungstyp | None = None
    sparte: Sparte | None = None
    steuerbetraege: list[Steuerbetrag] | None = Field(default=None, title="Steuerbetraege")
    vorausgezahlt: Betrag | None = None
    zu_zahlen: Betrag | None = Field(default=None, alias="zuZahlen")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
