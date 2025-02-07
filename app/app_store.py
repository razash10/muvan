from dataclasses import dataclass, field

@dataclass
class Paths:
    leases_path: str = 'assets/leases.csv'
    properties_path: str = 'assets/properties.csv'
    units_path: str = 'assets/units.csv'

@dataclass
class Columns:
    lease_id: str = 'lease_id'
    unit_id: str = 'unit_id'
    tenant_id: str = 'tenant_id'
    start_date: str = 'start_date'
    end_date: str = 'end_date'
    property_id: str = 'property_id'
    unit_number: str = 'unit_number'
    size: str = 'size'
    type: str = 'type'
    property_name: str = 'property_name'
    address: str = 'address'
    vacancy_period: str = 'vacancy_period'

@dataclass
class AppStore:
    paths: Paths = field(default_factory=Paths)
    columns: Columns = field(default_factory=Columns)

store = AppStore()
