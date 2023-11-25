import pandas as pd
from pathlib import Path
import re


def camel_to_snake(name):
    """
    Convert camelCase, PascalCase, or mixed case with underscores to snake_case.
    
    Args:
    name (str): The string to convert.

    Returns:
    str: The converted string in snake_case.
    """

    # Replace dots with underscores
    step0 = name.replace('.', '_')

    # Insert an underscore before any uppercase letter followed by a lowercase letter, e.g., 'YearMonth' -> 'Year_Month'
    step1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', step0)
    
    # Next, insert an underscore between lowercase letters/numbers and uppercase letters, e.g., 'Made_In' -> 'Made_In', 'Year_Month' -> 'Year_Month'
    step2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', step1)

    # Finally, convert to lowercase and replace multiple consecutive underscores with a single one
    return re.sub('_+', '_', step2).lower()


def import_data():
    path = Path("../data").absolute()

    print('importing data...')
    df = pd.read_parquet(path / "db.parquet")

    df = df.reset_index()

    df.columns = [camel_to_snake(name) for name in df.columns]
    print('end')
    return df

if __name__ == '__main__':
    df = import_data()
