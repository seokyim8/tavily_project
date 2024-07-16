from langchain_openai import ChatOpenAI
from .state import AgentState
from dotenv import load_dotenv
from langchain_community.adapters.openai import convert_openai_messages
from .env import OPENAI_API_KEY
import os

_ = load_dotenv(".env")

class SelectorAgent:
    def __init__(self):
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    def make_reviews(self, sources: list):
        """
        Select and make a review for the selected game.
        """

        review_list = []
        games = list(map(lambda x: x["content"], sources))

        for game in games:
            prompt = [{
                "role": "system",
                "content": '''You are a professional game reviewer. Your goal is to return a game review.
                Each review should be in the format below:

                [Game Title]

                [Brief Summary]

                [Rating from 1 to 5. Only include number, no text.]


                Only return the above, nothing else.
                '''
            }, {
                "role": "user",
                "content": f"Here is the information related to the game:\n {game}\n From here, generate a review."
            }]

            message = convert_openai_messages(prompt)
            review_list.append(ChatOpenAI(model='gpt-3.5-turbo', max_retries=5).invoke(message).content)
        return review_list
    
    def parse_reviews(self, review: str):
        '''
        Parses the review and returns a dictionary.
        '''
        parsed = {}
        lines = review.splitlines()
        parsed["title"] = lines[0]
        parsed["rating"] = lines[len(lines)-1]
        content = ""
        for i in range(1,len(lines)-1):
            content += lines[i]
        parsed["content"] = content

        return parsed
            
    def run(self, state: AgentState):
        '''
        Creates and returns reviews for the provided games. Returns a list of reviews, where each review is a dictionary.
        '''
        reviews = []
        resulting_list = self.make_reviews(state["collected"])
        for review in resulting_list:
            reviews.append(self.parse_reviews(review))
        return {"reviews": reviews}
    