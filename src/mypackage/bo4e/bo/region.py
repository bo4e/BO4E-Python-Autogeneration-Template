from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut
from ..com.regionskriterium import Regionskriterium
from ..enum.typ import Typ


class Region(BaseModel):
    """
    Modellierung einer Region als Menge von Kriterien, die eine Region beschreiben

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Region.svg" type="image/svg+xml"></object>

    .. HINT::
        `Region JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Region.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    negativ_liste: list[Regionskriterium] | None = Field(default=None, alias="negativListe", title="Negativliste")
    positiv_liste: list[Regionskriterium] | None = Field(default=None, alias="positivListe", title="Positivliste")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
