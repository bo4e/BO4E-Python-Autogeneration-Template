from pydantic import BaseModel, ConfigDict, Field

from ..zusatz_attribut import ZusatzAttribut
from .auf_abschlagstaffel_pro_ort import AufAbschlagstaffelProOrt


class AufAbschlagProOrt(BaseModel):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen im Zusammenhang
    mit örtlichen Gültigkeiten abgebildet werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlagProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlagProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/AufAbschlagProOrt.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    netznr: str | None = Field(default=None, title="Netznr")
    ort: str | None = Field(default=None, title="Ort")
    postleitzahl: str | None = Field(default=None, title="Postleitzahl")
    staffeln: list[AufAbschlagstaffelProOrt] | None = Field(default=None, title="Staffeln")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
