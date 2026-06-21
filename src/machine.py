from pydantic import BaseModel, Field
from datetime import datetime

class Machine(BaseModel):
    name: str
    os_type: str
    cpu: int
    ram: int
    status: str = "active"
    date_created: datetime = Field(default_factory=datetime.now)
    date_deleted: datetime | None = None

    def delete(self):
        self.status = "deleted"
        self.date_deleted = datetime.now()

    def is_active(self) -> bool:
        return self.status == "active"

    def __str__(self):
        return (self.name + " (" + self.os_type + ", " + str(self.cpu) + " CPU Cores, " + str(self.ram) + " GB RAM)")