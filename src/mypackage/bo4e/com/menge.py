from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from ..enum.mengeneinheit import Mengeneinheit
from ..zusatz_attribut import ZusatzAttribut


class Menge(BaseModel):
    """
    Abbildung einer Menge mit Wert und Einheit.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Menge.svg" type="image/svg+xml"></object>

    .. HINT::
        `Menge JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Menge.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    einheit: Mengeneinheit | None = None
    wert: Decimal | None = Field(default=None, title="Wert")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
