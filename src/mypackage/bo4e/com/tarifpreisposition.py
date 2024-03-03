from pydantic import BaseModel, ConfigDict, Field

from ..enum.mengeneinheit import Mengeneinheit
from ..enum.preistyp import Preistyp
from ..enum.waehrungseinheit import Waehrungseinheit
from ..zusatz_attribut import ZusatzAttribut
from .preisstaffel import Preisstaffel


class Tarifpreisposition(BaseModel):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen abgebildet werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifpreisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifpreisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Tarifpreisposition.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    bezugseinheit: Mengeneinheit | None = None
    einheit: Waehrungseinheit | None = None
    mengeneinheitstaffel: Mengeneinheit | None = None
    preisstaffeln: list[Preisstaffel] | None = Field(default=None, title="Preisstaffeln")
    preistyp: Preistyp | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
