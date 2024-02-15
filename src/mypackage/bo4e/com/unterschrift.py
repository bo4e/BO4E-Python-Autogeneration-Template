from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..zusatz_attribut import ZusatzAttribut


class Unterschrift(BaseModel):
    """
    Modellierung einer Unterschrift, z.B. für Verträge, Angebote etc.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Unterschrift.svg" type="image/svg+xml"></object>

    .. HINT::
        `Unterschrift JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Unterschrift.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    datum: datetime | None = Field(default=None, title="Datum")
    name: str | None = Field(default=None, title="Name")
    ort: str | None = Field(default=None, title="Ort")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
