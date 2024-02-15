from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..enum.geraeteklasse import Geraeteklasse
from ..enum.geraetetyp import Geraetetyp
from ..enum.typ import Typ


class Geraet(BaseModel):
    """
    Mit diesem BO werden alle Geräte modelliert, die keine Zähler sind.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Geraet.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geraet JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Geraet.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    geraeteklasse: Geraeteklasse | None = None
    geraetenummer: str | None = Field(default=None, title="Geraetenummer")
    geraetetyp: Geraetetyp | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
