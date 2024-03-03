from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from ..enum.mengeneinheit import Mengeneinheit
from ..enum.messwertstatus import Messwertstatus
from ..enum.wertermittlungsverfahren import Wertermittlungsverfahren
from ..zusatz_attribut import ZusatzAttribut


class Verbrauch(BaseModel):
    """
    Abbildung eines zeitlich abgegrenzten Verbrauchs

    .. raw:: html

        <object data="../_static/images/bo4e/com/Verbrauch.svg" type="image/svg+xml"></object>

    .. HINT::
        `Verbrauch JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Verbrauch.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    einheit: Mengeneinheit | None = None
    enddatum: datetime | None = Field(default=None, title="Enddatum")
    messwertstatus: Messwertstatus | None = None
    obis_kennzahl: str | None = Field(default=None, alias="obisKennzahl", title="Obiskennzahl")
    startdatum: datetime | None = Field(default=None, title="Startdatum")
    wert: Decimal | None = Field(default=None, title="Wert")
    wertermittlungsverfahren: Wertermittlungsverfahren | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
