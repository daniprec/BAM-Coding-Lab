import pandas as pd


def split_event_gender(event: str) -> tuple:
    if "women" in event.lower():
        return event.split(", ")[0], "Women"
    elif "men" in event.lower():
        return event.split(", ")[0], "Men"
    else:
        return event, "Unknown"


def load_and_preprocess(
    path_csv: str = "../data/olympics_medals.csv",
) -> pd.DataFrame:

    # We use "read_csv" to load a "csv" file
    df = pd.read_csv(path_csv)

    # We add a "year" column by extracting the first part of the "edition" column
    df["year"] = df["edition"].apply(lambda x: int(x.split()[0]))
    # We add a "season" column by extracting the second part of the "edition" column
    df["season"] = df["edition"].apply(lambda x: x.split()[1])

    # We fill the "medal" column with "No" where it is "NaN"
    df["medal"].fillna("No", inplace=True)

    # We split the "event" column into "event_simple" and "gender"
    df[["event_simple", "gender"]] = (
        df["event"].apply(split_event_gender).apply(pd.Series)
    )

    return df


def count_medals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Count the number of medals per country and year.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with the Olympic data, as returned by `load_and_preprocess`.

    Returns
    -------
    pd.DataFrame
        DataFrame with the number of medals per country and year.
    """
    # Mask non-medal rows
    mask_medal = df["medal"] != "No"

    # Count unique events per country and year
    df_country = (
        df[mask_medal]
        .groupby(["year", "country_noc", "medal"], as_index=False)["event"]
        .nunique()
    )
    # Rename "event_simple" to "medals"
    df_country: pd.DataFrame = df_country.rename(columns={"event": "medals"})

    # Now we can add all kind of medals together
    df_country = df_country.groupby(["year", "country_noc"], as_index=False)[
        "medals"
    ].sum()

    return df_country


def add_gdp(df_medals: pd.DataFrame, path_csv: str = "../data/gdp.csv") -> pd.DataFrame:
    """
    Add GDP data to the DataFrame.

    Parameters
    ----------
    df_medals : pd.DataFrame
        DataFrame with the number of medals per country and year, as returned by `count_medals`.
    path_csv : str, optional
        Path to the CSV file with the GDP data per capita, by default "../data/gdp.csv".

    Returns
    -------
    pd.DataFrame
        DataFrame with the number of medals per country and year, and the GDP data.
    """

    df_gdp = pd.read_csv(path_csv)

    # Rename columns (we want to match our other dataframe)
    df_gdp = df_gdp.rename(
        columns={
            "Code": "country_noc",
            "Year": "year",
            "GDP per capita, PPP (constant 2017 international $)": "GDP",
        }
    )

    # Drop "Entity" column (optional)
    df_gdp = df_gdp.drop(columns=["Entity"])
    # Fill the missing values of "GDP", applying a linear interpolation by "Code" and "Year"
    df_gdp["GDP"] = df_gdp.groupby("country_noc")["GDP"].transform(
        lambda x: x.interpolate()
    )

    # Merge by country code and year
    df = pd.merge(df_medals, df_gdp, on=["country_noc", "year"])
    return df


def main(
    path_medals: str = "data/olympics_medals.csv",
    path_gdp: str = "data/gdp.csv",
    path_output: str = "data/medals_gdp.csv",
) -> pd.DataFrame:
    """
    Main function to process the Olympic data.

    Parameters
    ----------
    path_medals : str, optional
        Path to the CSV file with the Olympic data, by default "../data/olympics_medals.csv".
    path_gdp : str, optional
        Path to the CSV file with the GDP per capita data, by default "../data/gdp.csv".
    path_output : str, optional
        Path to save the output CSV file, by default "../data/medals_gdp.csv".
    """
    df = load_and_preprocess(path_csv=path_medals)
    df_medals = count_medals(df)
    df = add_gdp(df_medals, path_csv=path_gdp)
    df.to_csv(path_output, index=False)


if __name__ == "__main__":
    main()
