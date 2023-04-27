import pandas as pd

df = pd.read_csv('etoro.csv', delimiter=',')

df['Data'] = pd.to_datetime(df['Data'], format="%d-%m-%Y")
df = df.sort_values(by='Data')
grouped = df.groupby('Prodotto')
result_df = pd.DataFrame(columns=['Prodotto', 'Capital Gain/Loss'])


for name, group in grouped:

    capital_gain_loss = 0
    lots = []

    for index, row in group.iterrows():
        if row['Quantità'] < 0:  # SELL
            remaining_quantity = -row['Quantità']
            while remaining_quantity > 0 and lots:
                oldest_lot = lots[0]
                if oldest_lot['quantity'] <= remaining_quantity:
                    remaining_quantity -= oldest_lot['quantity']
                    capital_gain_loss += (row['Quotazione'] - oldest_lot['price']) * oldest_lot['quantity']
                    del lots[0]
                else:
                    oldest_lot['quantity'] -= remaining_quantity
                    capital_gain_loss += (row['Quotazione'] - oldest_lot['price']) * remaining_quantity
                    remaining_quantity = 0
        elif row['Quantità'] > 0:  # BUY
            lots.append({'quantity': row['Quantità'], 'price': row['Quotazione']})
    
    new_row = {'Prodotto':name, 'Capital Gain/Loss':capital_gain_loss} 
    print(new_row)
