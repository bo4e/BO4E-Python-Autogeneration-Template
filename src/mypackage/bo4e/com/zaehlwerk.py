from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..enum.energierichtung import Energierichtung
from ..enum.mengeneinheit import Mengeneinheit
from ..enum.verbrauchsart import Verbrauchsart
from ..enum.waermenutzung import Waermenutzung
from .konzessionsabgabe import Konzessionsabgabe
from .verwendungszweck_pro_marktrolle import VerwendungszweckProMarktrolle
from .zaehlzeitregister import Zaehlzeitregister


class Zaehlwerk(BaseModel):
    """
    Mit dieser Komponente werden Zählwerke modelliert.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zaehlwerk.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlwerk JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Zaehlwerk.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    anzahl_ablesungen: int | None = Field(default=None, alias="anzahlAblesungen", title="Anzahlablesungen")
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    einheit: Mengeneinheit | None = None
    ist_abrechnungsrelevant: bool | None = Field(
        default=None, alias="istAbrechnungsrelevant", title="Istabrechnungsrelevant"
    )
    ist_schwachlastfaehig: bool | None = Field(default=None, alias="istSchwachlastfaehig", title="Istschwachlastfaehig")
    ist_steuerbefreit: bool | None = Field(default=None, alias="istSteuerbefreit", title="Iststeuerbefreit")
    ist_unterbrechbar: bool | None = Field(default=None, alias="istUnterbrechbar", title="Istunterbrechbar")
    konzessionsabgabe: Konzessionsabgabe | None = None
    nachkommastelle: int | None = Field(default=None, title="Nachkommastelle")
    obis_kennzahl: str | None = Field(default=None, alias="obisKennzahl", title="Obiskennzahl")
    richtung: Energierichtung | None = None
    verbrauchsart: Verbrauchsart | None = None
    verwendungszwecke: list[VerwendungszweckProMarktrolle] | None = Field(default=None, title="Verwendungszwecke")
    vorkommastelle: int | None = Field(default=None, title="Vorkommastelle")
    waermenutzung: Waermenutzung | None = None
    wandlerfaktor: Decimal | None = Field(default=None, title="Wandlerfaktor")
    zaehlwerk_id: str | None = Field(default=None, alias="zaehlwerkId", title="Zaehlwerkid")
    zaehlzeitregister: Zaehlzeitregister | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
