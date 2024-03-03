from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from ..zusatz_attribut import ZusatzAttribut


class TarifpreisstaffelProOrt(BaseModel):
    """
    Gibt die Staffelgrenzen der jeweiligen Preise an

    .. raw:: html

        <object data="../_static/images/bo4e/com/TarifpreisstaffelProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `TarifpreisstaffelProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/TarifpreisstaffelProOrt.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    arbeitspreis: Decimal | None = Field(default=None, title="Arbeitspreis")
    arbeitspreis_nt: Decimal | None = Field(default=None, alias="arbeitspreisNT", title="Arbeitspreisnt")
    grundpreis: Decimal | None = Field(default=None, title="Grundpreis")
    staffelgrenze_bis: Decimal | None = Field(default=None, alias="staffelgrenzeBis", title="Staffelgrenzebis")
    staffelgrenze_von: Decimal | None = Field(default=None, alias="staffelgrenzeVon", title="Staffelgrenzevon")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
