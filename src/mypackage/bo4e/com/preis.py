from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from ..enum.mengeneinheit import Mengeneinheit
from ..enum.preisstatus import Preisstatus
from ..enum.waehrungseinheit import Waehrungseinheit
from ..zusatz_attribut import ZusatzAttribut


class Preis(BaseModel):
    """
    Abbildung eines Preises mit Wert, Einheit, Bezugswert und Status.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preis.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preis JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Preis.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    bezugswert: Mengeneinheit | None = None
    einheit: Waehrungseinheit | None = None
    status: Preisstatus | None = None
    wert: Decimal | None = Field(default=None, title="Wert")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
