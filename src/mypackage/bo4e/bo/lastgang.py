from pydantic import BaseModel, ConfigDict, Field

from ..com.menge import Menge
from ..com.zeitreihenwert import Zeitreihenwert
from ..enum.mengeneinheit import Mengeneinheit
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut
from .marktlokation import Marktlokation
from .messlokation import Messlokation


class Lastgang(BaseModel):
    """
    Modell zur Abbildung eines Lastganges;
    In diesem Modell werden die Messwerte mit einem vollständigen Zeitintervall (zeit_intervall_laenge) angegeben und es bietet daher eine hohe Flexibilität in der Übertragung jeglicher zeitlich veränderlicher Messgrössen.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Lastgang.svg" type="image/svg+xml"></object>

    .. HINT::
        `Lastgang JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Lastgang.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    marktlokation: Marktlokation | None = None
    messgroesse: Mengeneinheit | None = None
    messlokation: Messlokation | None = None
    obis_kennzahl: str | None = Field(default=None, alias="obisKennzahl", title="Obiskennzahl")
    sparte: Sparte | None = None
    version: str | None = Field(default=None, title="Version")
    werte: list[Zeitreihenwert] | None = Field(default=None, title="Werte")
    zeit_intervall_laenge: Menge | None = Field(..., alias="zeitIntervallLaenge")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
