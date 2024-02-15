from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from ..enum.auf_abschlagstyp import AufAbschlagstyp
from ..enum.waehrungseinheit import Waehrungseinheit
from ..zusatz_attribut import ZusatzAttribut


class PositionsAufAbschlag(BaseModel):
    """
    Differenzierung der zu betrachtenden Produkte anhand der preiserhöhenden (Aufschlag)
    bzw. preisvermindernden (Abschlag) Zusatzvereinbarungen,
    die individuell zu einem neuen oder bestehenden Liefervertrag abgeschlossen werden können.
    Es können mehrere Auf-/Abschläge gleichzeitig ausgewählt werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/PositionsAufAbschlag.svg" type="image/svg+xml"></object>

    .. HINT::
        `PositionsAufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/PositionsAufAbschlag.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    auf_abschlagstyp: AufAbschlagstyp | None = Field(default=None, alias="aufAbschlagstyp")
    auf_abschlagswaehrung: Waehrungseinheit | None = Field(default=None, alias="aufAbschlagswaehrung")
    auf_abschlagswert: Decimal | None = Field(default=None, alias="aufAbschlagswert", title="Aufabschlagswert")
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
