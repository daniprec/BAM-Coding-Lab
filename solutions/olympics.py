import pandas as pd


def split_event_gender(event: str) -> tuple:
    if "women" in event.lower():
        return event.split(", ")[0], "Women"
    elif "men" in event.lower():
        return event.split(", ")[0], "Men"
    else:
        return event, "Unknown"


def load_and_preprocess(
    path_csv: str = "../data/olympics/olympics_medals.csv",
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
