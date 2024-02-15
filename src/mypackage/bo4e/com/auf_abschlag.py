from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..enum.auf_abschlagstyp import AufAbschlagstyp
from ..enum.auf_abschlagsziel import AufAbschlagsziel
from ..enum.waehrungseinheit import Waehrungseinheit
from .preisstaffel import Preisstaffel
from .zeitraum import Zeitraum


class AufAbschlag(BaseModel):
    """
    Modell für die preiserhöhenden (Aufschlag) bzw. preisvermindernden (Abschlag) Zusatzvereinbarungen,
    die individuell zu einem neuen oder bestehenden Liefervertrag abgeschlossen wurden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlag.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/AufAbschlag.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    auf_abschlagstyp: AufAbschlagstyp | None = Field(default=None, alias="aufAbschlagstyp")
    auf_abschlagsziel: AufAbschlagsziel | None = Field(default=None, alias="aufAbschlagsziel")
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    einheit: Waehrungseinheit | None = None
    gueltigkeitszeitraum: Zeitraum | None = None
    staffeln: list[Preisstaffel] | None = Field(default=None, title="Staffeln")
    website: str | None = Field(default=None, title="Website")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
