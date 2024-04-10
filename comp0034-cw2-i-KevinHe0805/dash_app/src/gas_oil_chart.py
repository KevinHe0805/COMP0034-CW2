import plotly.graph_objects as go
import plotly.express as px

class EnergyPriceChart:

    def __init__(self, data):
        self.data = data

    def create_chart(self, type):
        type_data = self.data.energy_price
        type = go.Scatter(x=type_data['Date'], y=type_data['Price'],
                          mode='lines',
                          name=type,
                          line=dict(color='firebrick', width=4))

        # Create the layout
        layout = go.Layout(showlegend=True, plot_bgcolor="#ffffff")

        # Create the figure
        figure = go.Figure(layout=layout)

        # Update the figure and add the traces
        figure.add_trace(type)

        # Update the layout
        figure.update_layout(yaxis_title="Price")
        figure.update_yaxes(title_font=dict(size=14, color='#CDCDCD'),
                            tickfont=dict(color='#CDCDCD', size=12),
                            showgrid=True, gridwidth=1, gridcolor='#CDCDCD',
                            tick0=0.0, dtick=10.0)
        figure.update_xaxes(tickangle=90, tickfont=dict(color='#CDCDCD', size=12),
                            showline=True, linewidth=2, linecolor='#CDCDCD')

        return figure

    def draw_all_line_chart(self):
        gas_data = self.data.source_gas
        wti_data = self.data.source_wti
        brent_data = self.data.source_brent
        gas = go.Scatter(x=gas_data['Date'], y=gas_data['Price'],
                          mode='lines',
                          name="gas",
                          line=dict(color='blue', width=4))
        wti = go.Scatter(x=wti_data['Date'], y=wti_data['Price'],
                         mode='lines',
                         name="wti_oil",
                         line=dict(color='green', width=4))
        brent = go.Scatter(x=brent_data['Date'], y=brent_data['Price'],
                         mode='lines',
                         name="brent_oil",
                         line=dict(color='orange', width=4))

        # Create the layout
        layout = go.Layout(showlegend=True, plot_bgcolor="#ffffff")

        # Create the figure
        large_figure = go.Figure(layout=layout)

        # Update the figure and add the traces
        large_figure.add_trace(gas)
        large_figure.add_trace(wti)
        large_figure.add_trace(brent)



        return large_figure


# Creates the recycling bar chart to be used in the dashboard
class EnergyBarChart:

    def __init__(self, data):
        self.data = data

    def create_chart(self, specific_date):
        data = self.data.energy
        data = data.loc[data['Date'] == specific_date]
        data = data.sort_values('Date', ascending=False)
        title_text = f'Daily price of oil and gas in {specific_date}'
        fig = px.bar(data, x='type', y='Price', title=title_text)
        return fig