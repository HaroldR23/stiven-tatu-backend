from dataclasses import dataclass

@dataclass
class ScheduleAppointment:
	full_name: str
	email: str
	phone: str

	styles: list[str]
	color: str
	location: str
	size: str
	idea: str
	artist: str
	reference: str

	allergies: str
	preferred_date: str
	is_over_18: bool
	accepts_privacy: bool
