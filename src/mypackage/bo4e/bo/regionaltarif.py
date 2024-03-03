from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..com.energiemix import Energiemix
from ..com.regionale_preisgarantie import RegionalePreisgarantie
from ..com.regionale_tarifpreisposition import RegionaleTarifpreisposition
from ..com.regionaler_auf_abschlag import RegionalerAufAbschlag
from ..com.tarifberechnungsparameter import Tarifberechnungsparameter
from ..com.tarifeinschraenkung import Tarifeinschraenkung
from ..com.vertragskonditionen import Vertragskonditionen
from ..com.zeitraum import Zeitraum
from ..enum.kundentyp import Kundentyp
from ..enum.registeranzahl import Registeranzahl
from ..enum.sparte import Sparte
from ..enum.tarifmerkmal import Tarifmerkmal
from ..enum.tariftyp import Tariftyp
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut
from .marktteilnehmer import Marktteilnehmer


class Regionaltarif(BaseModel):
    """
    .. raw:: html

        <object data="../_static/images/bo4e/bo/Regionaltarif.svg" type="image/svg+xml"></object>

    .. HINT::
        `Regionaltarif JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Regionaltarif.json>`_
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
    preisgarantien: list[RegionalePreisgarantie] | None = Field(default=None, title="Preisgarantien")
    preisstand: datetime | None = Field(default=None, title="Preisstand")
    registeranzahl: Registeranzahl | None = None
    sparte: Sparte | None = None
    tarif_auf_abschlaege: list[RegionalerAufAbschlag] | None = Field(
        default=None, alias="tarifAufAbschlaege", title="Tarifaufabschlaege"
    )
    tarifeinschraenkung: Tarifeinschraenkung | None = None
    tarifmerkmale: list[Tarifmerkmal] | None = Field(default=None, title="Tarifmerkmale")
    tarifpreise: list[RegionaleTarifpreisposition] | None = Field(default=None, title="Tarifpreise")
    tariftyp: Tariftyp | None = None
    vertragskonditionen: Vertragskonditionen | None = None
    website: str | None = Field(default=None, title="Website")
    zeitliche_gueltigkeit: Zeitraum | None = Field(default=None, alias="zeitlicheGueltigkeit")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
