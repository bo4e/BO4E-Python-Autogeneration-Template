from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..com.zeitreihenwert import Zeitreihenwert
from ..enum.medium import Medium
from ..enum.mengeneinheit import Mengeneinheit
from ..enum.messart import Messart
from ..enum.messgroesse import Messgroesse
from ..enum.typ import Typ
from ..enum.wertermittlungsverfahren import Wertermittlungsverfahren


class Zeitreihe(BaseModel):
    """
    Abbildung einer allgemeinen Zeitreihe mit einem Wertvektor.
    Die Werte können mit wahlfreier zeitlicher Distanz im Vektor abgelegt sein.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Zeitreihe.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitreihe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Zeitreihe.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    einheit: Mengeneinheit | None = None
    medium: Medium | None = None
    messart: Messart | None = None
    messgroesse: Messgroesse | None = None
    version: str | None = Field(default=None, title="Version")
    werte: list[Zeitreihenwert] | None = Field(default=None, title="Werte")
    wertherkunft: Wertermittlungsverfahren | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
