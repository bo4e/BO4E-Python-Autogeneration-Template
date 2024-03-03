from pydantic import BaseModel, ConfigDict, Field

from ..com.adresse import Adresse
from ..com.geokoordinaten import Geokoordinaten
from ..com.katasteradresse import Katasteradresse
from ..com.messlokationszuordnung import Messlokationszuordnung
from ..enum.bilanzierungsmethode import Bilanzierungsmethode
from ..enum.energierichtung import Energierichtung
from ..enum.gasqualitaet import Gasqualitaet
from ..enum.gebiettyp import Gebiettyp
from ..enum.kundentyp import Kundentyp
from ..enum.netzebene import Netzebene
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..enum.verbrauchsart import Verbrauchsart
from ..zusatz_attribut import ZusatzAttribut
from .geschaeftspartner import Geschaeftspartner


class Marktlokation(BaseModel):
    """
    Object containing information about a Marktlokation

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Marktlokation.svg" type="image/svg+xml"></object>

    .. HINT::
        `Marktlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Marktlokation.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    bilanzierungsgebiet: str | None = Field(default=None, title="Bilanzierungsgebiet")
    bilanzierungsmethode: Bilanzierungsmethode | None = None
    endkunde: Geschaeftspartner | None = None
    energierichtung: Energierichtung | None = None
    gasqualitaet: Gasqualitaet | None = None
    gebietstyp: Gebiettyp | None = None
    geoadresse: Geokoordinaten | None = None
    grundversorgercodenr: str | None = Field(default=None, title="Grundversorgercodenr")
    ist_unterbrechbar: bool | None = Field(default=None, alias="istUnterbrechbar", title="Istunterbrechbar")
    katasterinformation: Katasteradresse | None = None
    kundengruppen: list[Kundentyp] | None = Field(default=None, title="Kundengruppen")
    lokationsadresse: Adresse | None = None
    marktlokations_id: str | None = Field(default=None, alias="marktlokationsId", title="Marktlokationsid")
    netzbetreibercodenr: str | None = Field(default=None, title="Netzbetreibercodenr")
    netzebene: Netzebene | None = None
    netzgebietsnr: str | None = Field(default=None, title="Netzgebietsnr")
    sparte: Sparte | None = None
    verbrauchsart: Verbrauchsart | None = None
    zugehoerige_messlokation: Messlokationszuordnung | None = Field(default=None, alias="zugehoerigeMesslokation")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
