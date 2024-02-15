from pydantic import BaseModel, ConfigDict, Field

from ..com.betrag import Betrag
from ..com.kostenblock import Kostenblock
from ..com.zeitraum import Zeitraum
from ..enum.kostenklasse import Kostenklasse
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut


class Kosten(BaseModel):
    """
    Dieses BO wird zur Übertagung von hierarchischen Kostenstrukturen verwendet.
    Die Kosten werden dabei in Kostenblöcke und diese wiederum in Kostenpositionen strukturiert.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Kosten.svg" type="image/svg+xml"></object>

    .. HINT::
        `Kosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Kosten.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    gueltigkeit: Zeitraum | None = None
    kostenbloecke: list[Kostenblock] | None = Field(default=None, title="Kostenbloecke")
    kostenklasse: Kostenklasse | None = None
    summe_kosten: list[Betrag] | None = Field(default=None, alias="summeKosten", title="Summekosten")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
