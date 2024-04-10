from pathlib import Path
import pandas as pd


class EnergyPriceData:

    def __init__(self):
        self.energy = pd.DataFrame()
        self.type_list = []
        self.gas_price = []
        self.source_gas = []
        self.source_wti = []
        self.source_brent = []
        self.energy_price = []
        self.get_data()

    def get_data(self):
        csvfile = Path(__file__).parent.joinpath('data', 'gas_oil_daily_prepared.csv')
        self.energy = pd.read_csv(csvfile)
        self.type_list = self.energy["type"].unique().tolist()

    def process_data_for_type(self, type):
        # Data for the selected type
        self.energy_price = self.energy.loc[self.energy['type'] == type]

        # data for each type
        self.source_gas = self.energy.loc[self.energy['type'] == 'gas']
        self.source_wti = self.energy.loc[self.energy['type'] == 'wti']
        self.source_brent = self.energy.loc[self.energy['type'] == 'brent']

    def process_data_for_date(self, Date):
        # Data for the selected type
        self.energy_price = self.energy.loc[self.energy['Date'] == Date]
