from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..com.ausschreibungslos import Ausschreibungslos
from ..com.zeitraum import Zeitraum
from ..enum.ausschreibungsportal import Ausschreibungsportal
from ..enum.ausschreibungsstatus import Ausschreibungsstatus
from ..enum.ausschreibungstyp import Ausschreibungstyp
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut
from .geschaeftspartner import Geschaeftspartner


class Ausschreibung(BaseModel):
    """
    Das BO Ausschreibung dient zur detaillierten Darstellung von ausgeschriebenen Energiemengen in der Energiewirtschaft

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Ausschreibung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ausschreibung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Ausschreibung.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    abgabefrist: Zeitraum | None = None
    ausschreibender: Geschaeftspartner | None = None
    ausschreibungportal: Ausschreibungsportal | None = None
    ausschreibungsnummer: str | None = Field(default=None, title="Ausschreibungsnummer")
    ausschreibungsstatus: Ausschreibungsstatus | None = None
    ausschreibungstyp: Ausschreibungstyp | None = None
    bindefrist: Zeitraum | None = None
    ist_kostenpflichtig: bool | None = Field(default=None, alias="istKostenpflichtig", title="Istkostenpflichtig")
    lose: list[Ausschreibungslos] | None = Field(default=None, title="Lose")
    veroeffentlichungszeitpunkt: datetime | None = Field(default=None, title="Veroeffentlichungszeitpunkt")
    webseite: str | None = Field(default=None, title="Webseite")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
