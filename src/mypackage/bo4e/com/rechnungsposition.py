from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..enum.bdew_artikelnummer import BDEWArtikelnummer
from ..enum.mengeneinheit import Mengeneinheit
from .betrag import Betrag
from .menge import Menge
from .preis import Preis
from .steuerbetrag import Steuerbetrag


class Rechnungsposition(BaseModel):
    """
    Über Rechnungspositionen werden Rechnungen strukturiert.
    In einem Rechnungsteil wird jeweils eine in sich geschlossene Leistung abgerechnet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Rechnungsposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Rechnungsposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Rechnungsposition.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    artikel_id: str | None = Field(default=None, alias="artikelId", title="Artikelid")
    artikelnummer: BDEWArtikelnummer | None = None
    einzelpreis: Preis | None = None
    lieferung_bis: datetime | None = Field(default=None, alias="lieferungBis", title="Lieferungbis")
    lieferung_von: datetime | None = Field(default=None, alias="lieferungVon", title="Lieferungvon")
    lokations_id: str | None = Field(default=None, alias="lokationsId", title="Lokationsid")
    positions_menge: Menge | None = Field(default=None, alias="positionsMenge")
    positionsnummer: int | None = Field(default=None, title="Positionsnummer")
    positionstext: str | None = Field(default=None, title="Positionstext")
    teilrabatt_netto: Betrag | None = Field(default=None, alias="teilrabattNetto")
    teilsumme_netto: Betrag | None = Field(default=None, alias="teilsummeNetto")
    teilsumme_steuer: Steuerbetrag | None = Field(default=None, alias="teilsummeSteuer")
    zeitbezogene_menge: Menge | None = Field(default=None, alias="zeitbezogeneMenge")
    zeiteinheit: Mengeneinheit | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
