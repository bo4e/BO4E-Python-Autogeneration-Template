from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..com.adresse import Adresse
from ..enum.anrede import Anrede
from ..enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from ..enum.kontaktart import Kontaktart
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut


class Geschaeftspartner(BaseModel):
    """
    Mit diesem Objekt können Geschäftspartner übertragen werden.
    Sowohl Unternehmen, als auch Privatpersonen können Geschäftspartner sein.
    Hinweis: Marktteilnehmer haben ein eigenes BO, welches sich von diesem BO ableitet.
    Hier sollte daher keine Zuordnung zu Marktrollen erfolgen.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Geschaeftspartner.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geschaeftspartner JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Geschaeftspartner.json>`_
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
    name1: str = Field(..., title="Name1")
    name2: str | None = Field(default=None, title="Name2")
    name3: str | None = Field(default=None, title="Name3")
    partneradresse: Adresse | None = None
    umsatzsteuer_id: str | None = Field(default=None, alias="umsatzsteuerId", title="Umsatzsteuerid")
    website: str | None = Field(default=None, title="Website")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    foo: datetime | None = Field(default=None, title="Foo")
    erstellungsdatum: datetime | None = Field(default=None, title="Erstellungsdatum")
    geburtstag: datetime | None = Field(default=None, title="Geburtstag")
    telefonnummer_mobil: str | None = Field(default=None, alias="telefonnummerMobil", title="Telefonnummermobil")
    telefonnummer_privat: str | None = Field(default=None, alias="telefonnummerPrivat", title="Telefonnummerprivat")
    telefonnummer_geschaeft: str | None = Field(
        default=None, alias="telefonnummerGeschaeft", title="Telefonnummergeschaeft"
    )
    firmenname: str | None = Field(default=None, title="Firmenname")
    hausbesitzer: bool | None = Field(default=None, title="Hausbesitzer")
