def calculate_inventory(df):
    lead_time = 5
    safety_stock = df['forecast'].std()

    df['reorder_point'] = df['forecast'] * lead_time + safety_stock
    return df