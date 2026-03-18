from pydantic import BaseModel, model_validator, Field, ValidationError
from enum import Enum
from datetime import datetime


class RankEnum(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: RankEnum
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validation_rules(self) -> 'SpaceMission':

        if not self.mission_id.startswith('M'):
            raise ValueError('Mission ID must start with "M"')

        ranking: int = 0
        for member in self.crew:
            if (
                member.rank.value == 'commander'
                or member.rank.value == 'captain'
            ):
                ranking += 1
        if ranking == 0:
            raise ValueError('Must have at least one Commander or Captain')

        enough_xp: int = 0
        for member in self.crew:
            if member.years_experience >= 5:
                enough_xp += 1

        crew_xp: float = enough_xp / len(self.crew)

        if self.duration_days > 365 and crew_xp < 0.5:
            raise ValueError(
                'Long missions (> 365 days) need 50% '
                'experienced crew (5+ years)'
            )

        for member in self.crew:
            if member.is_active is False:
                raise ValueError('All crew members must be active')

        return self


def main() -> None:
    print(
        'Space Mission Crew Validation\n'
        '========================================='
    )

    try:
        data = SpaceMission(
            mission_id='M2024_MARS', mission_name='Mars Colony Establishment',
            destination='Mars', launch_date=datetime.now(),
            duration_days=900, budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id='SC0', name='Sarah Connor',
                    rank=RankEnum.COMMANDER, age=25,
                    specialization='Mission Command', years_experience=6
                ),
                CrewMember(
                    member_id='JS1', name='John Smith',
                    rank=RankEnum.LIEUTENANT, age=28,
                    specialization='Navigation', years_experience=8
                ),
                CrewMember(
                    member_id='AJ2', name='Alice Johnson',
                    rank=RankEnum.OFFICER, age=32,
                    specialization='Engineering', years_experience=17
                )
            ],
        )
        print('Valid mission created:\n')
        print(
            f'Mission: {data.mission_name}\n'
            f'ID: {data.mission_id}\n'
            f'Destination: {data.destination}\n'
            f'Duration: {data.duration_days} days\n'
            f'Budget: ${data.budget_millions}M\n'
            f'Crew size: {len(data.crew)}'
        )
        print('Crew members:')
        for member in data.crew:
            print(
                f'- {member.name} ({member.rank.value}) '
                f'- {member.specialization}'
            )
    except ValidationError as err:
        print(err.errors()[0]['msg'])

    print('\n=========================================')
    try:
        data = SpaceMission(
            mission_id='M2024_MARS', mission_name='Mars Colony Establishment',
            destination='Mars', launch_date=datetime.now(),
            duration_days=900, budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id='SC0', name='Sarah Connor',
                    rank=RankEnum.OFFICER, age=25,
                    specialization='Mission Command', years_experience=4
                ),
                CrewMember(
                    member_id='JS1', name='John Smith',
                    rank=RankEnum.LIEUTENANT, age=28,
                    specialization='Navigation', years_experience=8
                ),
                CrewMember(
                    member_id='AJ2', name='Alice Johnson',
                    rank=RankEnum.OFFICER, age=32,
                    specialization='Engineering', years_experience=10
                )
            ],
        )
        print('Valid mission created:\n')
        print(
            f'Mission: {data.mission_name}\n'
            f'ID: {data.mission_id}\n'
            f'Destination: {data.destination}\n'
            f'Duration: {data.duration_days} days\n'
            f'Budget: ${data.budget_millions}M\n'
            f'Crew size: {len(data.crew)}'
        )
        print('Crew members:')
        for member in data.crew:
            print(
                f'- {member.name} ({member.rank.value}) '
                f'- {member.specialization}'
            )
    except ValidationError as err:
        print(err.errors()[0]['msg'])


if __name__ == '__main__':
    main()
