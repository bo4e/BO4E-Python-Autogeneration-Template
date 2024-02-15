from pydantic import BaseModel, ConfigDict, Field

from ..enum.gueltigkeitstyp import Gueltigkeitstyp
from ..enum.regionskriteriumtyp import Regionskriteriumtyp
from ..zusatz_attribut import ZusatzAttribut


class Regionskriterium(BaseModel):
    """
    Komponente zur Abbildung eines Regionskriteriums

    .. raw:: html

        <object data="../_static/images/bo4e/com/Regionskriterium.svg" type="image/svg+xml"></object>

    .. HINT::
        `Regionskriterium JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Regionskriterium.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    gueltigkeitstyp: Gueltigkeitstyp | None = None
    regionskriteriumtyp: Regionskriteriumtyp | None = None
    wert: str | None = Field(default=None, title="Wert")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
