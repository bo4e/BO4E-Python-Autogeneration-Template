from pydantic import BaseModel, ConfigDict, Field

from ..com.standorteigenschaften_gas import StandorteigenschaftenGas
from ..com.standorteigenschaften_strom import StandorteigenschaftenStrom
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut


class Standorteigenschaften(BaseModel):
    """
    Modelliert die regionalen und spartenspezifischen Eigenschaften einer gegebenen Adresse.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Standorteigenschaften.svg" type="image/svg+xml"></object>

    .. HINT::
        `Standorteigenschaften JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/bo/Standorteigenschaften.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    typ: Typ = Field(..., alias="_typ")
    version: str = Field(..., alias="_version", title=" Version")
    eigenschaften_gas: StandorteigenschaftenGas | None = Field(default=None, alias="eigenschaftenGas")
    eigenschaften_strom: list[StandorteigenschaftenStrom] | None = Field(
        default=None, alias="eigenschaftenStrom", title="Eigenschaftenstrom"
    )
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
