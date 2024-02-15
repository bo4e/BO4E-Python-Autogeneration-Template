from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..com.unterschrift import Unterschrift
from ..com.vertragskonditionen import Vertragskonditionen
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..enum.vertragsart import Vertragsart
from ..enum.vertragsstatus import Vertragsstatus
from .geschaeftspartner import Geschaeftspartner
from .vertrag import Vertrag


class Buendelvertrag(BaseModel):
    """
    Abbildung eines Bündelvertrags.
    Es handelt sich hierbei um eine Liste von Einzelverträgen, die in einem Vertragsobjekt gebündelt sind.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Buendelvertrag.svg" type="image/svg+xml"></object>

    .. HINT::
        `Buendelvertrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Buendelvertrag.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    einzelvertraege: list[Vertrag] | None = Field(default=None, title="Einzelvertraege")
    sparte: Sparte | None = None
    unterzeichnervp1: list[Unterschrift] | None = Field(default=None, title="Unterzeichnervp1")
    unterzeichnervp2: list[Unterschrift] | None = Field(default=None, title="Unterzeichnervp2")
    vertragsart: Vertragsart | None = None
    vertragsbeginn: datetime | None = Field(default=None, title="Vertragsbeginn")
    vertragsende: datetime | None = Field(default=None, title="Vertragsende")
    vertragskonditionen: list[Vertragskonditionen] | None = Field(default=None, title="Vertragskonditionen")
    vertragsnummer: str | None = Field(default=None, title="Vertragsnummer")
    vertragspartner1: Geschaeftspartner | None = None
    vertragspartner2: Geschaeftspartner | None = None
    vertragsstatus: Vertragsstatus | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
