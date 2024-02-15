from pydantic import BaseModel, ConfigDict, Field

from ..enum.rufnummernart import Rufnummernart
from ..zusatz_attribut import ZusatzAttribut


class Rufnummer(BaseModel):
    """
    Contains information to call or fax someone

    .. raw:: html

        <object data="../_static/images/bo4e/com/Rufnummer.svg" type="image/svg+xml"></object>

    .. HINT::
        `Rufnummer JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Rufnummer.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    nummerntyp: Rufnummernart | None = None
    rufnummer: str | None = Field(default=None, title="Rufnummer")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
