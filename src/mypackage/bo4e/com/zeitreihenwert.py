from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..enum.messwertstatus import Messwertstatus
from ..enum.messwertstatuszusatz import Messwertstatuszusatz
from .zeitspanne import Zeitspanne


class Zeitreihenwert(BaseModel):
    """
    Abbildung eines Zeitreihenwertes bestehend aus Zeitraum, Wert und Statusinformationen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitreihenwert.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitreihenwert JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Zeitreihenwert.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    status: Messwertstatus | None = None
    statuszusatz: Messwertstatuszusatz | None = None
    wert: Decimal | None = Field(default=None, title="Wert")
    zeitspanne: Zeitspanne | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
