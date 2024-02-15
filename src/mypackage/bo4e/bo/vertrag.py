from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..com.unterschrift import Unterschrift
from ..com.vertragskonditionen import Vertragskonditionen
from ..com.vertragsteil import Vertragsteil
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..enum.vertragsart import Vertragsart
from ..enum.vertragsstatus import Vertragsstatus
from ..zusatz_attribut import ZusatzAttribut
from .geschaeftspartner import Geschaeftspartner


class Vertrag(BaseModel):
    """
    Modell für die Abbildung von Vertragsbeziehungen;
    Das Objekt dient dazu, alle Arten von Verträgen, die in der Energiewirtschaft Verwendung finden, abzubilden.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Vertrag.svg" type="image/svg+xml"></object>

    .. HINT::
        `Vertrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Vertrag.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    sparte: Sparte | None = None
    unterzeichnervp1: list[Unterschrift] | None = Field(default=None, title="Unterzeichnervp1")
    unterzeichnervp2: list[Unterschrift] | None = Field(default=None, title="Unterzeichnervp2")
    vertragsart: Vertragsart | None = None
    vertragsbeginn: datetime | None = Field(default=None, title="Vertragsbeginn")
    vertragsende: datetime | None = Field(default=None, title="Vertragsende")
    vertragskonditionen: Vertragskonditionen | None = None
    vertragsnummer: str | None = Field(default=None, title="Vertragsnummer")
    vertragspartner1: Geschaeftspartner | None = None
    vertragspartner2: Geschaeftspartner | None = None
    vertragsstatus: Vertragsstatus | None = None
    vertragsteile: list[Vertragsteil] | None = Field(default=None, title="Vertragsteile")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
