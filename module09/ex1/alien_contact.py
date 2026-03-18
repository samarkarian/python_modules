from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validation_rules(self) -> 'AlienContact':

        if not self.contact_id.startswith('AC'):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type is ContactType.PHYSICAL and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')

        if (
            self.contact_type is ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                'Telepathic contact requires at least 3 witnesses'
            )

        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                'Strong signals (> 7.0) should include received messages'
            )

        return self


def main() -> None:

    print(
        '\nAlien Contact Log Validation\n'
        '======================================'
    )
    try:
        data: AlienContact = AlienContact(
            contact_id='AC_2024_001', timestamp=datetime.now().isoformat(),
            location='Area 51, Nevada', contact_type='radio',
            signal_strength=8.5, duration_minutes=45,
            witness_count=5, message_received='Greetings from Zeta Reticuli'
        )
        print('Valid contact report:\n')
        print(f'ID: {data.contact_id}')
        print(f'Type: {data.contact_type.value}')
        print(f'Location: {data.location}')
        print(f'Signal: {data.signal_strength}/10')
        print(f'Duration: {data.duration_minutes} minutes')
        print(f'Witnesses: {data.witness_count}')
        print(f"Message: '{data.message_received}'")
    except ValidationError as err:
        print(err.errors()[0]['msg'])

    print('\n========================================')
    try:
        data_false: AlienContact = AlienContact(
            contact_id='AC_2024_001', timestamp=datetime.now().isoformat(),
            location='Area 51, Nevada', contact_type='telepathic',
            signal_strength=8.5, duration_minutes=45,
            witness_count=2, message_received='Greetings from Zeta Reticuli',
            is_verified=True
        )
        print('Valid contact report:\n')
        print(f'ID: {data_false.contact_id}')
        print(f'Type: {data_false.contact_type.value}')
        print(f'Location: {data_false.location}')
        print(f'Signal: {data_false.signal_strength}/10')
        print(f'Duration: {data_false.duration_minutes} minutes')
        print(f'Witnesses: {data_false.witness_count}')
        print(f"Message: '{data_false.message_received}'")
    except ValidationError as err:
        print(err.errors()[0]['msg'])


if __name__ == "__main__":
    main()
