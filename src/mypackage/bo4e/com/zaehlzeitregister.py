from pydantic import BaseModel, ConfigDict, Field

from ..zusatz_attribut import ZusatzAttribut


class Zaehlzeitregister(BaseModel):
    """
    Mit dieser Komponente werden Zählzeitregister modelliert. Ein Zählzeitregister beschreibt eine erweiterte Definition der Zählzeit
    in Bezug auf ein Register. Dabei werden alle Codes dazu vom Netzbetreiber vergeben.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zaehlzeitregister.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlzeitregister JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Zaehlzeitregister.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    ist_schwachlastfaehig: bool | None = Field(default=None, alias="istSchwachlastfaehig", title="Istschwachlastfaehig")
    zaehlzeit_definition: str | None = Field(default=None, alias="zaehlzeitDefinition", title="Zaehlzeitdefinition")
    zaehlzeit_register: str | None = Field(default=None, alias="zaehlzeitRegister", title="Zaehlzeitregister")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
