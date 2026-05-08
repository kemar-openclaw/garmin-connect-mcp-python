from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import date

class DateRangeInput(BaseModel):
    start_date: str = Field(..., description="Start date in YYYY-MM-DD format")
    end_date: str = Field(..., description="End date in YYYY-MM-DD format")

class DateInput(BaseModel):
    target_date: str = Field(..., description="Target date in YYYY-MM-DD format")

class ActivityIdInput(BaseModel):
    activity_id: int = Field(..., description="The ID of the activity")

class GearIdInput(BaseModel):
    gear_id: str = Field(..., description="The ID of the gear")

class DeviceIdInput(BaseModel):
    device_id: str = Field(..., description="The ID of the device")
