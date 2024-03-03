from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from ..com.zaehlwerk import Zaehlwerk
from ..enum.befestigungsart import Befestigungsart
from ..enum.messwerterfassung import Messwerterfassung
from ..enum.registeranzahl import Registeranzahl
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..enum.zaehlerauspraegung import Zaehlerauspraegung
from ..enum.zaehlergroesse import Zaehlergroesse
from ..enum.zaehlertyp import Zaehlertyp
from ..enum.zaehlertyp_spezifikation import ZaehlertypSpezifikation
from ..zusatz_attribut import ZusatzAttribut
from .geraet import Geraet
from .geschaeftspartner import Geschaeftspartner


class Zaehler(BaseModel):
    """
    Object containing information about a meter/"Zaehler".

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Zaehler.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehler JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Zaehler.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    befestigungsart: Befestigungsart | None = None
    eichung_bis: datetime | None = Field(default=None, alias="eichungBis", title="Eichungbis")
    geraete: list[Geraet] | None = Field(default=None, title="Geraete")
    ist_fernschaltbar: bool | None = Field(default=None, alias="istFernschaltbar", title="Istfernschaltbar")
    letzte_eichung: datetime | None = Field(default=None, alias="letzteEichung", title="Letzteeichung")
    messwerterfassung: Messwerterfassung | None = None
    registeranzahl: Registeranzahl | None = None
    sparte: Sparte | None = None
    zaehlerauspraegung: Zaehlerauspraegung | None = None
    zaehlergroesse: Zaehlergroesse | None = None
    zaehlerhersteller: Geschaeftspartner | None = None
    zaehlerkonstante: Decimal | None = Field(default=None, title="Zaehlerkonstante")
    zaehlernummer: str | None = Field(default=None, title="Zaehlernummer")
    zaehlertyp: Zaehlertyp | None = None
    zaehlertyp_spezifikation: ZaehlertypSpezifikation | None = Field(default=None, alias="zaehlertypSpezifikation")
    zaehlwerke: list[Zaehlwerk] | None = Field(default=None, title="Zaehlwerke")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
