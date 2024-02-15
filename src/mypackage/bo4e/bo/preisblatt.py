from pydantic import BaseModel, ConfigDict, Field

from ..com.preisposition import Preisposition
from ..com.zeitraum import Zeitraum
from ..enum.preisstatus import Preisstatus
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut
from .marktteilnehmer import Marktteilnehmer


class Preisblatt(BaseModel):
    """
    Das allgemeine Modell zur Abbildung von Preisen;
    Davon abgeleitet können, über die Zuordnung identifizierender Merkmale, spezielle Preisblatt-Varianten modelliert
    werden.

    Die jeweiligen Sätze von Merkmalen sind in der Grafik ergänzt worden und stellen jeweils eine Ausprägung für die
    verschiedenen Anwendungsfälle der Preisblätter dar.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Preisblatt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisblatt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Preisblatt.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    gueltigkeit: Zeitraum | None = None
    herausgeber: Marktteilnehmer | None = None
    preispositionen: list[Preisposition] | None = Field(default=None, title="Preispositionen")
    preisstatus: Preisstatus | None = None
    sparte: Sparte | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
