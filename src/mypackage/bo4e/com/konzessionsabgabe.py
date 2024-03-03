from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from ..enum.abgabe_art import AbgabeArt
from ..zusatz_attribut import ZusatzAttribut


class Konzessionsabgabe(BaseModel):
    """
    Diese Komponente wird zur Übertagung der Details zu einer Konzessionsabgabe verwendet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Konzessionsabgabe.svg" type="image/svg+xml"></object>

    .. HINT::
        `Konzessionsabgabe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Konzessionsabgabe.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    kategorie: str | None = Field(default=None, title="Kategorie")
    kosten: Decimal | None = Field(default=None, title="Kosten")
    satz: AbgabeArt | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
