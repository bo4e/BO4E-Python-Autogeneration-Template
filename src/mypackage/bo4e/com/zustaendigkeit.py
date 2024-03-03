from pydantic import BaseModel, ConfigDict, Field

from ..enum.themengebiet import Themengebiet
from ..zusatz_attribut import ZusatzAttribut


class Zustaendigkeit(BaseModel):
    """
    Enthält die zeitliche Zuordnung eines Ansprechpartners zu Abteilungen und Zuständigkeiten.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zustaendigkeit.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zustaendigkeit JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Zustaendigkeit.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    abteilung: str | None = Field(default=None, title="Abteilung")
    jobtitel: str | None = Field(default=None, title="Jobtitel")
    themengebiet: Themengebiet | None = None
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
