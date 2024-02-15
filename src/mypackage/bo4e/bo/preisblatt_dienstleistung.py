from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..com.preisposition import Preisposition
from ..com.zeitraum import Zeitraum
from ..enum.bilanzierungsmethode import Bilanzierungsmethode
from ..enum.dienstleistungstyp import Dienstleistungstyp
from ..enum.preisstatus import Preisstatus
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from .geraet import Geraet
from .marktteilnehmer import Marktteilnehmer


class PreisblattDienstleistung(BaseModel):
    """
    Variante des Preisblattmodells zur Abbildung der Preise für wahlfreie Dienstleistungen

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattDienstleistung.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattDienstleistung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/PreisblattDienstleistung.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    basisdienstleistung: Dienstleistungstyp | None = None
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    bilanzierungsmethode: Bilanzierungsmethode | None = None
    geraetedetails: Geraet | None = None
    gueltigkeit: Zeitraum | None = None
    herausgeber: Marktteilnehmer | None = None
    inklusive_dienstleistungen: list[Dienstleistungstyp] | None = Field(
        default=None, alias="inklusiveDienstleistungen", title="Inklusivedienstleistungen"
    )
    preispositionen: list[Preisposition] | None = Field(default=None, title="Preispositionen")
    preisstatus: Preisstatus | None = None
    sparte: Sparte | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
