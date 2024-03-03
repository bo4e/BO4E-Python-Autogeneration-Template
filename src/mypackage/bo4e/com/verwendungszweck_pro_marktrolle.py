from pydantic import BaseModel, ConfigDict, Field

from ..enum.marktrolle import Marktrolle
from ..enum.verwendungszweck import Verwendungszweck
from ..zusatz_attribut import ZusatzAttribut


class VerwendungszweckProMarktrolle(BaseModel):
    """
    Dient zur Identifizierung des Verwendungszwecks der Marktrolle an der Marktlokation, der die Werte zu übermitteln sind.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Verwendungszweck.svg" type="image/svg+xml"></object>

    .. HINT::
        `Verwendungszweck JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Verwendungszweck.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    marktrolle: Marktrolle | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    zwecke: list[Verwendungszweck] | None = Field(default=None, title="Zwecke")
