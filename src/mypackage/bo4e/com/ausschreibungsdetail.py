from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..enum.zaehlertyp import Zaehlertyp
from .adresse import Adresse
from .menge import Menge
from .zeitraum import Zeitraum


class Ausschreibungsdetail(BaseModel):
    """
    Die Komponente Ausschreibungsdetail wird verwendet um die Informationen zu einer Abnahmestelle innerhalb eines
    Ausschreibungsloses abzubilden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Ausschreibungsdetail.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ausschreibungsdetail JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Ausschreibungsdetail.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    ist_lastgang_vorhanden: bool | None = Field(
        default=None, alias="istLastgangVorhanden", title="Istlastgangvorhanden"
    )
    kunde: str | None = Field(default=None, title="Kunde")
    lieferzeitraum: Zeitraum | None = None
    marktlokations_id: str | None = Field(default=None, alias="marktlokationsId", title="Marktlokationsid")
    marktlokationsadresse: Adresse | None = None
    marktlokationsbezeichnung: str | None = Field(default=None, title="Marktlokationsbezeichnung")
    netzbetreiber: str | None = Field(default=None, title="Netzbetreiber")
    netzebene_lieferung: str | None = Field(default=None, alias="netzebeneLieferung", title="Netzebenelieferung")
    netzebene_messung: str | None = Field(default=None, alias="netzebeneMessung", title="Netzebenemessung")
    prognose_arbeit_lieferzeitraum: Menge | None = Field(default=None, alias="prognoseArbeitLieferzeitraum")
    prognose_jahresarbeit: Menge | None = Field(default=None, alias="prognoseJahresarbeit")
    prognose_leistung: Menge | None = Field(default=None, alias="prognoseLeistung")
    rechnungsadresse: Adresse | None = None
    zaehlernummer: str | None = Field(default=None, title="Zaehlernummer")
    zaehlertechnik: Zaehlertyp | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
