from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def valid_station(data: SpaceStation) -> None:

    print('Valid station created:\n')

    print(f"ID: {data.station_id}")
    print(f"Name: {data.name}")
    print(f"Crew: {data.crew_size} people")
    print(f"Power: {data.power_level}%")
    print(f"Oxygen: {data.oxygen_level}%")
    if data.is_operational:
        print('Status: Operational\n')
    else:
        print('Status: Offline\n')


def main() -> None:

    print(
        '\nSpace Station Data Validation\n'
        '========================================'
    )

    try:
        data = SpaceStation(
            station_id='ISS001', name='International Space Station',
            crew_size=6, power_level=85.5, oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
        valid_station(data)
    except ValidationError as err:
        print(err.errors()[0]['msg'])

    print('========================================')
    try:
        data = SpaceStation(
            station_id='ISS001', name='International Space Station',
            crew_size=26, power_level=85.5, oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
        valid_station(data)
    except ValidationError as err:
        print(err.errors()[0]['msg'])


if __name__ == '__main__':
    main()
