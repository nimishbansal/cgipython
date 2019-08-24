import pandas as pd

YES = 'Y'
NO = 'N'

EditorChoices = (
    (YES, 'Yes'),
    (NO, 'No'),
)


def populate_data_from_csv(csv_file_path='./main_app/games_data.csv'):
    from main_app.models import GameGenre, GamePlatform, Game
    dataframe = pd.read_csv(csv_file_path)
    print("populating", len(dataframe), "records")
    for i in range(len(dataframe)):
        print("record no", i)
        title = dataframe.iloc[i].title
        platform_name = dataframe.iloc[i].platform
        score = dataframe.iloc[i].score
        genre_name = dataframe.iloc[i].genre
        editors_choice = dataframe.iloc[i].editors_choice

        genre = GameGenre.objects.get_or_create(name=genre_name)[0]
        platform = GamePlatform.objects.get_or_create(name=platform_name)[0]

        Game.objects.get_or_create(title=title, platform=platform, score=score, genre=genre,
                                   editors_choice=editors_choice)
