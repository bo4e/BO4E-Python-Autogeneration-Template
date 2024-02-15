from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut


class Geokoordinaten(BaseModel):
    """
    This component provides the geo-coordinates for a location.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Geokoordinaten.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geokoordinaten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Geokoordinaten.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    breitengrad: Decimal | None = Field(default=None, title="Breitengrad")
    laengengrad: Decimal | None = Field(default=None, title="Laengengrad")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
