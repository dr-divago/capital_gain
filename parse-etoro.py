import pandas as pd

df = pd.read_csv('etoro-cleaned.csv', delimiter=',')
df['Open Date'] = pd.to_datetime(df['Open Date'], format="%d/%m/%Y %H:%M:%S")
df['Close Date'] = pd.to_datetime(df['Close Date'], format="%d/%m/%Y %H:%M:%S")
df = df[df['Close Date'].dt.year == 2022]
grouped = df.groupby('Type')
result_df = pd.DataFrame(columns=['Type', 'Capital Gain/Loss'])
#
#
for name, group in grouped:
    capital_gain_loss = 0
    lots = []

    for index, row in group.iterrows():
        capital_gain_loss += row['Profit']
    new_row = {'Prodotto': name, 'Capital Gain/Loss': capital_gain_loss}
    print(new_row)
