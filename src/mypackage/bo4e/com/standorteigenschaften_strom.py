from pydantic import BaseModel, ConfigDict, Field

from ..bo4e_schemas.zusatz_attribut import ZusatzAttribut


class StandorteigenschaftenStrom(BaseModel):
    """
    Standorteigenschaften der Sparte Strom

    .. raw:: html

        <object data="../_static/images/bo4e/com/StandorteigenschaftenStrom.svg" type="image/svg+xml"></object>

    .. HINT::
        `StandorteigenschaftenStrom JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/StandorteigenschaftenStrom.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    bilanzierungsgebiet_eic: str | None = Field(
        default=None, alias="bilanzierungsgebietEic", title="Bilanzierungsgebieteic"
    )
    regelzone: str | None = Field(default=None, title="Regelzone")
    regelzone_eic: str | None = Field(default=None, alias="regelzoneEic", title="Regelzoneeic")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
