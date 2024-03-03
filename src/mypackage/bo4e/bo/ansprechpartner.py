from pydantic import BaseModel, ConfigDict, Field

from ..com.adresse import Adresse
from ..com.rufnummer import Rufnummer
from ..com.zustaendigkeit import Zustaendigkeit
from ..enum.anrede import Anrede
from ..enum.titel import Titel
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut
from .geschaeftspartner import Geschaeftspartner


class Ansprechpartner(BaseModel):
    """
    Object containing information about a Ansprechpartner

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Ansprechpartner.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ansprechpartner JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Ansprechpartner.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    adresse: Adresse | None = None
    anrede: Anrede | None = None
    e_mail_adresse: str | None = Field(default=None, alias="eMailAdresse", title="Emailadresse")
    geschaeftspartner: Geschaeftspartner | None = None
    individuelle_anrede: str | None = Field(default=None, alias="individuelleAnrede", title="Individuelleanrede")
    kommentar: str | None = Field(default=None, title="Kommentar")
    nachname: str | None = Field(default=None, title="Nachname")
    rufnummer: Rufnummer | None = None
    titel: Titel | None = None
    vorname: str | None = Field(default=None, title="Vorname")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    zustaendigkeit: Zustaendigkeit | None = None
