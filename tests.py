import os
import pandas as pd
import pytest

CSV_FILE = "data/reviews-per-country.csv"

# Fixture to load the CSV file once for all tests
@pytest.fixture(scope="module")
def df():
    return pd.read_csv(CSV_FILE)

# Test to check if the CSV file exists
def test_file_exists():
    assert os.path.exists(CSV_FILE), "CSV file does not exist"

# Test to check if the expected columns exist in the CSV file
def test_columns_exist(df):
    expected_columns = ['country', 'count', 'points']
    for col in expected_columns:
        assert col in df.columns, f"Column {col} does not exist"

# Parameterized test to check values for specific countries
@pytest.mark.parametrize("country_name,expected_count,expected_points", [
    ('US', 54504, 88.6),
    ('France', 22093, 88.8),
    ('Italy', 19540, 88.6),
    ('Spain', 6645, 87.3),
    ('Israel', 505, 88.5),
    ('Egypt', 1, 84.0)
])
def test_values_exist(df, country_name, expected_count, expected_points):
    assert df.loc[df['country'] == country_name]['count'].iloc[0] == expected_count, \
        f"Expected {expected_count} for {country_name}, but got {df.loc[df['country'] == country_name]['count'].iloc[0]}"
    assert df.loc[df['country'] == country_name]['points'].iloc[0] == expected_points, \
        f"Expected {expected_points} points for {country_name}, but got {df.loc[df['country'] == country_name]['points'].iloc[0]}"
