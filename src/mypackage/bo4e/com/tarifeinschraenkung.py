from pydantic import BaseModel, ConfigDict, Field

from ..bo.geraet import Geraet
from ..enum.voraussetzungen import Voraussetzungen
from ..zusatz_attribut import ZusatzAttribut
from .menge import Menge


class Tarifeinschraenkung(BaseModel):
    """
    Mit dieser Komponente werden Einschränkungen für die Anwendung von Tarifen modelliert.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifeinschraenkung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifeinschraenkung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Tarifeinschraenkung.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    einschraenkungleistung: list[Menge] | None = Field(default=None, title="Einschraenkungleistung")
    einschraenkungzaehler: list[Geraet] | None = Field(default=None, title="Einschraenkungzaehler")
    voraussetzungen: list[Voraussetzungen] | None = Field(default=None, title="Voraussetzungen")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    zusatzprodukte: list[str] | None = Field(default=None, title="Zusatzprodukte")
