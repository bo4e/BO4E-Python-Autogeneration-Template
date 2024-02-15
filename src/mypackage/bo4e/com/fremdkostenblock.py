from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from .betrag import Betrag
from .fremdkostenposition import Fremdkostenposition


class Fremdkostenblock(BaseModel):
    """
    Komponente zur Abbildung eines Kostenblocks in den Fremdkosten

    .. raw:: html

        <object data="../_static/images/bo4e/com/Fremdkostenblock.svg" type="image/svg+xml"></object>

    .. HINT::
        `Fremdkostenblock JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Fremdkostenblock.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    kostenblockbezeichnung: str | None = Field(default=None, title="Kostenblockbezeichnung")
    kostenpositionen: list[Fremdkostenposition] | None = Field(default=None, title="Kostenpositionen")
    summe_kostenblock: Betrag | None = Field(default=None, alias="summeKostenblock")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
