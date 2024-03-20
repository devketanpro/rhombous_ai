import pandas as pd


def infer_and_convert_data_types(df):
    for col in df.columns:
        # Attempt to convert to numeric first
        try:
            df[col] = df[col].astype('object')
            continue
        except(ValueError, TypeError):
            pass
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            continue
        except (ValueError, TypeError):
            pass

        # Attempt to convert to datetime
        try:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            continue
        except (ValueError, TypeError):
            pass

        # Attempt to convert to timedelta if the column is timedelta-like
        try:
            df[col] = pd.to_timedelta(df[col], errors='coerce')
            continue
        except (ValueError, TypeError):
            pass

        # Check if the column should be categorical
        if len(df[col].unique()) / len(df[col]) < 0.5:  # Example threshold for categorization
            df[col] = pd.Categorical(df[col])
            continue

        # # If none of the above conversions work, retain the original object dtype
        # df[col] = df[col].astype('object')

    return df
