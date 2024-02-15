from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..com.angebotsvariante import Angebotsvariante
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut
from .ansprechpartner import Ansprechpartner
from .geschaeftspartner import Geschaeftspartner


class Angebot(BaseModel):
    """
    Mit diesem BO kann ein Versorgungsangebot zur Strom- oder Gasversorgung oder die Teilnahme an einer Ausschreibung
    übertragen werden. Es können verschiedene Varianten enthalten sein (z.B. ein- und mehrjährige Laufzeit).
    Innerhalb jeder Variante können Teile enthalten sein, die jeweils für eine oder mehrere Marktlokationen erstellt
    werden.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Angebot.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebot JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Angebot.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    anfragereferenz: str | None = Field(default=None, title="Anfragereferenz")
    angebotsdatum: datetime | None = Field(default=None, title="Angebotsdatum")
    angebotsgeber: Geschaeftspartner | None = None
    angebotsnehmer: Geschaeftspartner | None = None
    angebotsnummer: str | None = Field(default=None, title="Angebotsnummer")
    bindefrist: datetime | None = Field(default=None, title="Bindefrist")
    sparte: Sparte | None = None
    unterzeichner_angebotsgeber: Ansprechpartner | None = Field(default=None, alias="unterzeichnerAngebotsgeber")
    unterzeichner_angebotsnehmer: Ansprechpartner | None = Field(default=None, alias="unterzeichnerAngebotsnehmer")
    varianten: list[Angebotsvariante] | None = Field(default=None, title="Varianten")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
