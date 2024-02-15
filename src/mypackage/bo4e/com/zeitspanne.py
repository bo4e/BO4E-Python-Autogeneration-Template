from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..zusatz_attribut import ZusatzAttribut


class Zeitspanne(BaseModel):
    """
    Eine Zeitspanne ist definiert aus Start und/oder Ende.
    Der Unterschied zur Menge (die auch zur Abbildung von Zeitmengen genutzt wird) ist, dass konkrete Start- und Endzeitpunkte angegeben werden.
    Die Zeitspanne ist aus dem COM Zeitraum hervorgegangen, das in Zeitspanne und Menge aufgeteilt wurde.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitspanne.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitspanne JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Zeitspanne.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    ende: datetime | None = Field(default=None, title="Ende")
    start: datetime | None = Field(default=None, title="Start")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
