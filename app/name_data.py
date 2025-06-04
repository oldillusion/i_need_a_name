import json
import random

class NameData:
    def __init__(self, noun_file, adjective_file):
        self.nouns = self.load_json(noun_file)
        self.adjectives = self.load_json(adjective_file)

    @staticmethod
    def load_json(file_path):
        with open(file_path) as f:
            return json.load(f)

    def generate_random_name(self):
        noun = random.choice(self.nouns)
        adjective = random.choice(self.adjectives)
        return f"{adjective.capitalize()}{noun.capitalize()}"