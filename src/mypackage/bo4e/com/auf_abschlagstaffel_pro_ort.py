from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut


class AufAbschlagstaffelProOrt(BaseModel):
    """
    Gibt den Wert eines Auf- oder Abschlags und dessen Staffelgrenzen an

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlagstaffelProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlagstaffelProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/AufAbschlagstaffelProOrt.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    staffelgrenze_bis: Decimal | None = Field(default=None, alias="staffelgrenzeBis", title="Staffelgrenzebis")
    staffelgrenze_von: Decimal | None = Field(default=None, alias="staffelgrenzeVon", title="Staffelgrenzevon")
    wert: Decimal | None = Field(default=None, title="Wert")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
