from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..com.adresse import Adresse
from ..enum.anrede import Anrede
from ..enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from ..enum.kontaktart import Kontaktart
from ..enum.marktrolle import Marktrolle
from ..enum.rollencodetyp import Rollencodetyp
from ..enum.sparte import Sparte
from ..enum.typ import Typ


class Marktteilnehmer(BaseModel):
    """
    Objekt zur Aufnahme der Information zu einem Marktteilnehmer

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Marktteilnehmer.svg" type="image/svg+xml"></object>

    .. HINT::
        `Marktteilnehmer JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Marktteilnehmer.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    amtsgericht: str | None = Field(default=None, title="Amtsgericht")
    anrede: Anrede | None = None
    e_mail_adresse: str | None = Field(default=None, alias="eMailAdresse", title="Emailadresse")
    geschaeftspartnerrolle: list[Geschaeftspartnerrolle] | None = Field(default=None, title="Geschaeftspartnerrolle")
    glaeubiger_id: str | None = Field(default=None, alias="glaeubigerId", title="Glaeubigerid")
    hrnummer: str | None = Field(default=None, title="Hrnummer")
    ist_gewerbe: bool | None = Field(default=None, alias="istGewerbe", title="Istgewerbe")
    kontaktweg: list[Kontaktart] | None = Field(default=None, title="Kontaktweg")
    makoadresse: str | None = Field(default=None, title="Makoadresse")
    marktrolle: Marktrolle | None = None
    name1: str | None = Field(default=None, title="Name1")
    name2: str | None = Field(default=None, title="Name2")
    name3: str | None = Field(default=None, title="Name3")
    partneradresse: Adresse | None = None
    rollencodenummer: str | None = Field(default=None, title="Rollencodenummer")
    rollencodetyp: Rollencodetyp | None = None
    sparte: Sparte | None = None
    umsatzsteuer_id: str | None = Field(default=None, alias="umsatzsteuerId", title="Umsatzsteuerid")
    website: str | None = Field(default=None, title="Website")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
