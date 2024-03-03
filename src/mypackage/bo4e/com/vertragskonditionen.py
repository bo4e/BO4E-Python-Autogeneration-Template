from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from ..zusatz_attribut import ZusatzAttribut
from .zeitraum import Zeitraum


class Vertragskonditionen(BaseModel):
    """
    Abbildung für Vertragskonditionen. Die Komponente wird sowohl im Vertrag als auch im Tarif verwendet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Vertragskonditionen.svg" type="image/svg+xml"></object>

    .. HINT::
        `Vertragskonditionen JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Vertragskonditionen.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    abschlagszyklus: Zeitraum | None = None
    anzahl_abschlaege: Decimal | None = Field(default=None, alias="anzahlAbschlaege", title="Anzahlabschlaege")
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    kuendigungsfrist: Zeitraum | None = None
    vertragslaufzeit: Zeitraum | None = None
    vertragsverlaengerung: Zeitraum | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
