from dataclasses import dataclass
from datetime import datetime, timedelta
import pandas as pd
from app.app_store import store

@dataclass(kw_only=True)
class AppState:
    leases: pd.DataFrame
    properties: pd.DataFrame
    units: pd.DataFrame
    combined_data: pd.DataFrame

    @classmethod
    def from_csv(cls):
        leases = pd.read_csv(store.paths.leases_path)
        properties = pd.read_csv(store.paths.properties_path)
        units = pd.read_csv(store.paths.units_path)
        combined_data = cls.get_combined_data(leases, properties, units)
        return cls(leases=leases, properties=properties, units=units, combined_data=combined_data)

    @staticmethod
    def get_combined_data(leases: pd.DataFrame, properties: pd.DataFrame, units: pd.DataFrame) -> pd.DataFrame:
        leases_units_combined_data = leases.merge(units, on=store.columns.unit_id)
        combined_data = leases_units_combined_data.merge(properties, on=store.columns.property_id)

        # Calculate vacancy periods
        combined_data[store.columns.start_date] = pd.to_datetime(combined_data[store.columns.start_date])
        combined_data[store.columns.end_date] = pd.to_datetime(combined_data[store.columns.end_date])
        combined_data = combined_data.sort_values(by=[store.columns.unit_id, store.columns.end_date])
        combined_data[store.columns.vacancy_period] = combined_data.groupby(store.columns.unit_id)[store.columns.start_date].shift(-1) - combined_data[store.columns.end_date]

        return combined_data
    
    def insight_properties_of_leases_about_to_expire(self, days: int) -> list:
        # Convert the 'end_date' column to datetime
        self.combined_data[store.columns.end_date] = pd.to_datetime(self.combined_data[store.columns.end_date])

        # Calculate the date 'days' days from now
        today = datetime.today()
        next_days = today + timedelta(days=days)

        # Filter leases that are about to expire in the next 'days' days
        filter_next_days = (self.combined_data[store.columns.end_date] > today)
        filter_next_days &= (self.combined_data[store.columns.end_date] <= next_days)
        expiring_leases = self.combined_data[filter_next_days]

        # Return the list of properties from the expiring leases
        expiring_leases_list = expiring_leases[store.columns.property_id].unique().tolist()
        return expiring_leases_list

    def insight_top_units_with_long_vacancies(self, count: int) -> list:
        # Filter vacancies greater than 30 days and within the last year
        one_year_ago = datetime.today() - timedelta(days=365)
        recent_leases = self.combined_data[self.combined_data[store.columns.end_date] >= one_year_ago]
        long_vacancies = recent_leases[recent_leases[store.columns.vacancy_period] > timedelta(days=30)]

        # Sort long_vacancies by vacancy_period
        long_vacancies = long_vacancies.sort_values(by=store.columns.vacancy_period, ascending=False)

        # Get the top 'count' units with long vacancies and return the list without duplicates
        top_units = long_vacancies.drop_duplicates(subset=store.columns.unit_id).head(count)
        return top_units[store.columns.unit_id].tolist()

state = AppState.from_csv()
