# To be able to access my code in another file, I transformed the preprocessing function into an accessible function. 

import pandas as pd

def load_and_preprocess(filepath):
    '''
    Loads the raw survey data from the specified file path and applies all necessary preprocessing steps 
    to prepare the dataset for analysis.

    This includes:
        - Renaming variables for clarity and consistency
        - Replacing numeric codes with human-readable labels (e.g., gender, age, voting experience)
        - Constructing composite variables (e.g., trustworthiness, credibility)
        - Filtering out incomplete responses

    Parameters:
        filepath (str): The path to the CSV file containing the raw survey data.

    Returns:
        pandas.DataFrame: A cleaned and fully preprocessed DataFrame ready for analysis.
    '''
    df = pd.read_csv(filepath)

    # REMOVE UNFINISED SURVEYS OR PARTICIPANTS THAT DID NOT CONSENT
    # Note: Personally identifying information (e.g., data for receiving VP hours) was excluded earlier for privacy and data protection reasons
    df = df[(df["FINISHED"] == 1) & (df["AC01"] == 2)]
    df = df.drop(columns=["FINISHED", "AC01"])

    # DEMOGRAPHIC INFORMATION
    df = df.rename(columns={"AD01": "gender"}).replace({"gender": {1: "female", 2: "male", 3: "non-binary", 4: "prefer not to say"}})
    df = df.rename(columns={"AD03": "age"}).replace({"age": {5: "over 30", 2: "under 20", 3: "under 25", 4: "under 30"}})
    df = df.rename(columns={"AD11": "voting_experience"}).replace({"voting_experience": {1: "None", 2: "Voted once", 3: "Voted multiple times"}})
    df = df.rename(columns={"AD10": "education_level"}).replace({"education_level": {1: "student", 2: "Hauptschule", 3: "Realschule", 4: "Hochschulreife", 8: "University degree", 9: "other"}})

    # POLITICAL INFORMATION
    df = df.rename(columns={"BP04": "spectrum_assessment01"}).replace({"spectrum_assessment01": {1: "Very conservative", 2: "Conservative", 3: "Moderate", 4: "Progressive", 5: "Very progressive"}})
    df = df.rename(columns={"FS08": "spectrum_assessment02"}).replace({"spectrum_assessment02": {1: "Very conservative", 2: "Conservative", 3: "Moderate", 4: "Progressive", 5: "Very progressive"}})
    df = df.rename(columns={"BP05": "political_engagement1"}).replace({"political_engagement1": {1: "Never", 2: "Rarely", 3: "Occasionaly", 4: "Weekly", 5: "Daily"}})
    df = df.rename(columns={"BP06": "political_engagement2"}).replace({"political_engagement2": {1: "very active", 2: "somewhat active", 3: "neutral", 4: "not very active", 5: "not active at all"}})
    df = df.rename(columns={"BP07": "political_interest"}).replace({"political_interest": {1: "not at all", 2: "slightly", 3: "moderately", 4: "very", 5: "extremely"}})
    df = df.rename(columns={"BP08": "political_familarity"}).replace({"political_familarity": {1: "not at all", 2: "slightly", 3: "moderately", 4: "very", 5: "extremely"}})

    # EXAMPLE VARIABLES
    df = df.rename(columns={"DI02": "source_guessing01"}).replace({"source_guessing01": {1: "Human", 2: "AI", 3: "Unsure"}})
    df = df.rename(columns={"DJ01": "source_guessing02"}).replace({"source_guessing02": {1: "Human", 2: "AI", 3: "Unsure"}})
    df = df.rename(columns={"DK01": "source_guessing03"}).replace({"source_guessing03": {1: "Human", 2: "AI", 3: "Unsure"}})
    df = df.rename(columns={"DL01": "source_guessing04"}).replace({"source_guessing04": {1: "Human", 2: "AI", 3: "Unsure"}})
    df = df.rename(columns={"DM01": "source_guessing05"}).replace({"source_guessing05": {1: "Human", 2: "AI", 3: "Unsure"}})
    df = df.rename(columns={"DN01": "source_guessing06"}).replace({"source_guessing06": {1: "Human", 2: "AI", 3: "Unsure"}})

    df = df.rename(columns={"DI03": "source_perception01"}).replace({"source_perception01": {1: "not at all", 2: "slightly", 3: "neutral", 4: "somewhat", 5: "very much"}})
    df = df.rename(columns={"DJ02": "source_perception02"}).replace({"source_perception02": {1: "not at all", 2: "slightly", 3: "neutral", 4: "somewhat", 5: "very much"}})
    df = df.rename(columns={"DK02": "source_perception03"}).replace({"source_perception03": {1: "not at all", 2: "slightly", 3: "neutral", 4: "somewhat", 5: "very much"}})
    df = df.rename(columns={"DL02": "source_perception04"}).replace({"source_perception04": {1: "not at all", 2: "slightly", 3: "neutral", 4: "somewhat", 5: "very much"}})
    df = df.rename(columns={"DM02": "source_perception05"}).replace({"source_perception05": {1: "not at all", 2: "slightly", 3: "neutral", 4: "somewhat", 5: "very much"}})
    df = df.rename(columns={"DN02": "source_perception06"}).replace({"source_perception06": {1: "not at all", 2: "slightly", 3: "neutral", 4: "somewhat", 5: "very much"}})

    df= df.rename(columns={"DI04": "credibility01"})
    df= df.rename(columns={"DJ03": "credibility02"})
    df= df.rename(columns={"DK03": "credibility03"})
    df= df.rename(columns={"DL03": "credibility04"})
    df= df.rename(columns={"DM03": "credibility05"})
    df= df.rename(columns={"DN03": "credibility06"})

    df= df.rename(columns={"DI05": "trustworthiness01"})
    df= df.rename(columns={"DJ04": "trustworthiness02"})
    df= df.rename(columns={"DK05": "trustworthiness03"})
    df= df.rename(columns={"DL04": "trustworthiness04"})
    df= df.rename(columns={"DM04": "trustworthiness05"})
    df= df.rename(columns={"DN04": "trustworthiness06"})

    df= df.rename(columns={"DI06": "accuracy01"})
    df= df.rename(columns={"DJ05": "accuracy02"})
    df= df.rename(columns={"DK06": "accuracy03"})
    df= df.rename(columns={"DL05": "accuracy04"})
    df= df.rename(columns={"DM05": "accuracy05"})
    df= df.rename(columns={"DN05": "accuracy06"})

    df= df.rename(columns={"DI07": "agreement01"})
    df= df.rename(columns={"DJ06": "agreement02"})
    df= df.rename(columns={"DK07": "agreement03"})
    df= df.rename(columns={"DL06": "agreement04"})
    df= df.rename(columns={"DM06": "agreement05"})
    df= df.rename(columns={"DN06": "agreement06"})

    df= df.rename(columns={"DI08": "alignment01"})
    df= df.rename(columns={"DJ07": "alignment02"})
    df= df.rename(columns={"DK10": "alignment03"})
    df= df.rename(columns={"DL09": "alignment04"})
    df= df.rename(columns={"DM09": "alignment05"})
    df= df.rename(columns={"DN09": "alignment06"})

    df= df.rename(columns={"DI08": "perspective_change01"})
    df= df.rename(columns={"DJ07": "perspective_change02"})
    df= df.rename(columns={"DK09": "perspective_change03"})
    df= df.rename(columns={"DL08": "perspective_change04"})
    df= df.rename(columns={"DM08": "perspective_change05"})
    df= df.rename(columns={"DN08": "perspective_change06"})

    # CONTENT TYPE
    df = df.rename(columns={"EE01": "content_type"}).replace({"content_type": {1: "Human", 2: "AI"}})

    return df