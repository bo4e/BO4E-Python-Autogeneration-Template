from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..com.adresse import Adresse
from ..com.dienstleistung import Dienstleistung
from ..com.geokoordinaten import Geokoordinaten
from ..com.katasteradresse import Katasteradresse
from ..enum.netzebene import Netzebene
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from .geraet import Geraet
from .zaehler import Zaehler


class Messlokation(BaseModel):
    """
    Object containing information about a Messlokation

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Messlokation.svg" type="image/svg+xml"></object>

    .. HINT::
        `Messlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Messlokation.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    geoadresse: Geokoordinaten | None = None
    geraete: list[Geraet] | None = Field(default=None, title="Geraete")
    grundzustaendiger_msb_codenr: str | None = Field(
        default=None, alias="grundzustaendigerMsbCodenr", title="Grundzustaendigermsbcodenr"
    )
    grundzustaendiger_msbim_codenr: str | None = Field(
        default=None, alias="grundzustaendigerMsbimCodenr", title="Grundzustaendigermsbimcodenr"
    )
    katasterinformation: Katasteradresse | None = None
    messadresse: Adresse | None = None
    messdienstleistung: list[Dienstleistung] | None = Field(default=None, title="Messdienstleistung")
    messgebietnr: str | None = Field(default=None, title="Messgebietnr")
    messlokations_id: str | None = Field(default=None, alias="messlokationsId", title="Messlokationsid")
    messlokationszaehler: list[Zaehler] | None = Field(default=None, title="Messlokationszaehler")
    netzebene_messung: Netzebene | None = Field(default=None, alias="netzebeneMessung")
    sparte: Sparte | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
