import requests

class JokeGenerator:
    def __init__(self):
        self.api_url = 'https://official-joke-api.appspot.com/random_joke'

    def fetch_joke(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            joke = response.json()
            return f"{joke['setup']} - {joke['punchline']}"
        else:
            return 'Failed to fetch a joke.'

if __name__ == '__main__':
    generator = JokeGenerator()
    print(generator.fetch_joke())