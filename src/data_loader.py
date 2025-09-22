import pandas as pd

class MovieDataLoader:
    def __init__(self, ori_csv: str, processed_csv: str):
        self.ori_csv = ori_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df = pd.read_csv(self.ori_csv, encoding='utf-8', on_bad_lines="skip").dropna()

        required_columns = ['title', 'vote_average', 'genres', 'overview']

        missing = set(required_columns) - set(df.columns)

        if missing:
            raise ValueError(f"Missing required columns: {missing}")
        
        df['combined_info'] = (
            "Title: " + df['title'].astype(str) +
            " Overview: " + df['overview'].astype(str) +
            " Genres: " + df['genres'].astype(str) +
            " Rating: " + df['vote_average'].astype(str)
        )


        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')

        return self.processed_csv