from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut


class Sigmoidparameter(BaseModel):
    """
    Die Sigmoid-Funktion, beispielsweise zur Berechnung eines Leistungspreises hat die Form:
    LP=A/(1+(P/B)^C)+D

    .. raw:: html

        <object data="../_static/images/bo4e/com/Sigmoidparameter.svg" type="image/svg+xml"></object>

    .. HINT::
        `Sigmoidparameter JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Sigmoidparameter.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    a: Decimal | None = Field(default=None, alias="A", title="A")
    b: Decimal | None = Field(default=None, alias="B", title="B")
    c: Decimal | None = Field(default=None, alias="C", title="C")
    d: Decimal | None = Field(default=None, alias="D", title="D")
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
