from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..com.auf_abschlag_regional import AufAbschlagRegional
from ..com.energiemix import Energiemix
from ..com.preisgarantie import Preisgarantie
from ..com.tarifberechnungsparameter import Tarifberechnungsparameter
from ..com.tarifeinschraenkung import Tarifeinschraenkung
from ..com.tarifpreisposition_pro_ort import TarifpreispositionProOrt
from ..com.vertragskonditionen import Vertragskonditionen
from ..com.zeitraum import Zeitraum
from ..enum.kundentyp import Kundentyp
from ..enum.registeranzahl import Registeranzahl
from ..enum.sparte import Sparte
from ..enum.tarifmerkmal import Tarifmerkmal
from ..enum.tariftyp import Tariftyp
from ..enum.typ import Typ
from .marktteilnehmer import Marktteilnehmer


class Tarif(BaseModel):
    """
    Abbildung eines Tarifs mit regionaler Zuordnung von Preisen und Auf- und Abschlägen

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Tarif.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarif JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Tarif.json>`_
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
    berechnungsparameter: Tarifberechnungsparameter | None = None
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    energiemix: Energiemix | None = None
    kundentypen: list[Kundentyp] | None = Field(default=None, title="Kundentypen")
    preisgarantie: Preisgarantie | None = None
    preisstand: datetime | None = Field(default=None, title="Preisstand")
    registeranzahl: Registeranzahl | None = None
    sparte: Sparte | None = None
    tarif_auf_abschlaege: list[AufAbschlagRegional] | None = Field(
        default=None, alias="tarifAufAbschlaege", title="Tarifaufabschlaege"
    )
    tarifeinschraenkung: Tarifeinschraenkung | None = None
    tarifmerkmale: list[Tarifmerkmal] | None = Field(default=None, title="Tarifmerkmale")
    tarifpreise: list[TarifpreispositionProOrt] | None = Field(default=None, title="Tarifpreise")
    tariftyp: Tariftyp | None = None
    vertragskonditionen: Vertragskonditionen | None = None
    website: str | None = Field(default=None, title="Website")
    zeitliche_gueltigkeit: Zeitraum | None = Field(default=None, alias="zeitlicheGueltigkeit")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
