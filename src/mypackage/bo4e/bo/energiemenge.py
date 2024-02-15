from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..com.verbrauch import Verbrauch
from ..enum.lokationstyp import Lokationstyp
from ..enum.typ import Typ


class Energiemenge(BaseModel):
    """
    Abbildung von Mengen, die Lokationen zugeordnet sind

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Energiemenge.svg" type="image/svg+xml"></object>

    .. HINT::
        `Energiemenge JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Energiemenge.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    energieverbrauch: list[Verbrauch] = Field(..., title="Energieverbrauch")
    lokations_id: str | None = Field(default=None, alias="lokationsId", title="Lokationsid")
    lokationstyp: Lokationstyp | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
