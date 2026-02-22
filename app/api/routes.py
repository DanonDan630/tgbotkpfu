import fastapi
from fastapi import status
from app.services.csv_cache import find_group_schedule_local
from app.services.parser import parse_schedule
from app.services.csv_cache import ensure_startup_cache
from fastapi.responses import JSONResponse
import asyncio
from app.api.utils import generate_valid_schedule_json
import app.api.models as models

router = fastapi.APIRouter()

@router.post(
    "/schedule/full/",
    response_model=models.ScheduleFull,
    status_code=status.HTTP_201_CREATED
)
async def get_group(item: models.Group):
    data = find_group_schedule_local(group_code=item.number)
    if data:
        data = parse_schedule(data, item.number)
        ret = models.ScheduleFull(data=generate_valid_schedule_json(data), status_code=200)


        return ret
    else:
        return JSONResponse(content={"status": f"Invalid group code {item.number}", "status_code": 404}, status_code=status.HTTP_404_NOT_FOUND,
                        headers={"X-My-Header": "value"})


