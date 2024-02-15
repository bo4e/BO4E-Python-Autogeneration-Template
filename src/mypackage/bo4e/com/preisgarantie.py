from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..enum.preisgarantietyp import Preisgarantietyp
from .zeitraum import Zeitraum


class Preisgarantie(BaseModel):
    """
    Definition für eine Preisgarantie mit der Möglichkeit verschiedener Ausprägungen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preisgarantie.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisgarantie JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Preisgarantie.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    preisgarantietyp: Preisgarantietyp | None = None
    zeitliche_gueltigkeit: Zeitraum | None = Field(default=None, alias="zeitlicheGueltigkeit")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
