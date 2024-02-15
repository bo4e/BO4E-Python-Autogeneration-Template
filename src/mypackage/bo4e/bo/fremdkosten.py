from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..com.betrag import Betrag
from ..com.fremdkostenblock import Fremdkostenblock
from ..com.zeitraum import Zeitraum
from ..enum.typ import Typ


class Fremdkosten(BaseModel):
    """
    Mit diesem BO werden die Fremdkosten, beispielsweise für eine Angebotserstellung oder eine Rechnungsprüfung,
    übertragen.
    Die Fremdkosten enthalten dabei alle Kostenblöcke, die von anderen Marktteilnehmern oder Instanzen erhoben werden.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Fremdkosten.svg" type="image/svg+xml"></object>

    .. HINT::
        `Fremdkosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Fremdkosten.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    gueltigkeit: Zeitraum | None = None
    kostenbloecke: list[Fremdkostenblock] | None = Field(default=None, title="Kostenbloecke")
    summe_kosten: Betrag | None = Field(default=None, alias="summeKosten")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
