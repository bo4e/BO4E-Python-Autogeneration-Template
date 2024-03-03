from pydantic import BaseModel, ConfigDict, Field

from ..zusatz_attribut import ZusatzAttribut


class Katasteradresse(BaseModel):
    """
    Dient der Adressierung über die Liegenschafts-Information.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Katasteradresse.svg" type="image/svg+xml"></object>

    .. HINT::
        `Katasteradresse JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Katasteradresse.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    flurstueck: str | None = Field(default=None, title="Flurstueck")
    gemarkung_flur: str | None = Field(default=None, alias="gemarkungFlur", title="Gemarkungflur")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
