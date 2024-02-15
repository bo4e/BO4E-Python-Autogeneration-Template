from pydantic import BaseModel, ConfigDict, Field

from ..zusatz_attribut import ZusatzAttribut


class MarktgebietInfo(BaseModel):
    """
    Informationen zum Marktgebiet im Gas.

    .. raw:: html

        <object data="../_static/images/bo4e/com/MarktgebietInfo.svg" type="image/svg+xml"></object>

    .. HINT::
        `MarktgebietInfo JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/MarktgebietInfo.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    marktgebiet: str | None = Field(default=None, title="Marktgebiet")
    marktgebietcode: str | None = Field(default=None, title="Marktgebietcode")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
