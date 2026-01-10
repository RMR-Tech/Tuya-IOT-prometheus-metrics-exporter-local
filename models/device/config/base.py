from pydantic import BaseModel


class BaseDeviceConfig(BaseModel):
    id: str
    ip: str = "Auto"
    key: str
    name: str = ""
