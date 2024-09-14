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
