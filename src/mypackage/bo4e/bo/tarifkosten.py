from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..com.energiemix import Energiemix
from ..com.vertragskonditionen import Vertragskonditionen
from ..com.zeitraum import Zeitraum
from ..enum.kundentyp import Kundentyp
from ..enum.registeranzahl import Registeranzahl
from ..enum.sparte import Sparte
from ..enum.tarifmerkmal import Tarifmerkmal
from ..enum.tariftyp import Tariftyp
from ..enum.typ import Typ
from .kosten import Kosten
from .marktteilnehmer import Marktteilnehmer


class Tarifkosten(BaseModel):
    """
    Objekt zur Kommunikation von Kosten, die im Rahmen der Tarifanwendung entstehen

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Tarifkosten.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifkosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Tarifkosten.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    anbieter: Marktteilnehmer | None = None
    anbietername: str | None = Field(default=None, title="Anbietername")
    anwendung_von: datetime | None = Field(default=None, alias="anwendungVon", title="Anwendungvon")
    bemerkung: str | None = Field(default=None, title="Bemerkung")
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    energiemix: Energiemix | None = None
    kosten: Kosten | None = None
    kundentypen: list[Kundentyp] | None = Field(default=None, title="Kundentypen")
    registeranzahl: Registeranzahl | None = None
    sparte: Sparte | None = None
    tarifmerkmale: list[Tarifmerkmal] | None = Field(default=None, title="Tarifmerkmale")
    tariftyp: Tariftyp | None = None
    vertragskonditionen: Vertragskonditionen | None = None
    website: str | None = Field(default=None, title="Website")
    zeitliche_gueltigkeit: Zeitraum | None = Field(default=None, alias="zeitlicheGueltigkeit")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
