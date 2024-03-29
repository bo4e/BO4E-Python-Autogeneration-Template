from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..enum.arithmetische_operation import ArithmetischeOperation
from ..zusatz_attribut import ZusatzAttribut


class Messlokationszuordnung(BaseModel):
    """
    Mit dieser Komponente werden Messlokationen zu Marktlokationen zugeordnet.
    Dabei kann eine arithmetische Operation (Addition, Subtraktion, Multiplikation, Division) angegeben werden,
    mit der die Messlokation zum Verbrauch der Marktlokation beiträgt.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Messlokationszuordnung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Messlokationszuordnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v202401.0.1-/src/bo4e_schemas/com/Messlokationszuordnung.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    version: str = Field(..., alias="_version", title=" Version")
    arithmetik: ArithmetischeOperation | None = None
    gueltig_bis: datetime | None = Field(default=None, alias="gueltigBis", title="Gueltigbis")
    gueltig_seit: datetime | None = Field(default=None, alias="gueltigSeit", title="Gueltigseit")
    messlokations_id: str | None = Field(default=None, alias="messlokationsId", title="Messlokationsid")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
