import dash
from dash import Dash
from dash import dcc, html
import plotly.express as px
from data import create_unique_list_of_currencies, get_data_from_external_postgres_database, set_data_types

df_exchange_rate = get_data_from_external_postgres_database()
df_exchange_rate = set_data_types(df_exchange_rate)
currency_codes = create_unique_list_of_currencies(df_exchange_rate)


app = Dash(name='big_mac')
server = app.server

currency_options = []
for currency in currency_codes:
    currency_options.append({'label': str(currency), 'value': str(currency)})


app.layout = html.Div([
    html.H2("Choose currency to check its exchange rate for PLN", style={'text-align': 'center'}),
    html.Div([dcc.Dropdown(id='currency-picker', options=currency_options, value=currency_options[42]["value"], searchable=True)]),
    html.Div([dcc.Graph(id='currency')])
])


@app.callback(dash.Output(component_id='currency', component_property='figure'),
              [dash.Input(component_id='currency-picker', component_property='value')])
def choose_currency(selected_currency):
    '''
    Chart for exchange rate
    :return:
    '''
    filtred_df = df_exchange_rate.copy()
    filtred_df = filtred_df.loc[filtred_df['currency_code'] == selected_currency]
    fig_exchange_rate = px.scatter(
        filtred_df,
        x='time_last_update_utc',
        y='rates',
        labels={'time_last_update_utc': 'Time', 'rates': 'Rates'},
        template="seaborn"
    )
    return fig_exchange_rate


if __name__ == '__main__':
    app.run_server(debug=True)
