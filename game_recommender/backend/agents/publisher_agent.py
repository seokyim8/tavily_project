from .state import AgentState

class PublisherAgent:
    def __init__(self):
       pass
    def run(self, state: AgentState):
        '''
        Creates the html page consisting of game recommendations. Returns path to the html page.
        '''
        html = f'''
        <ul>
            <li>
                <h1>{state["reviews"][0]["title"]}</h1>
                <p>{state["reviews"][0]["content"]}</p>
                <p>Rating: {state["reviews"][0]["rating"]}</p>
                <img src={state["images"][0]} />
            </li>
            <li>
                <h1>{state["reviews"][1]["title"]}</h1>
                <p>{state["reviews"][1]["content"]}</p>
                <p>Rating: {state["reviews"][1]["rating"]}</p>
                <img src={state["images"][1]} />
            </li>
            <li>
                <h1>{state["reviews"][2]["title"]}</h1>
                <p>{state["reviews"][2]["content"]}</p>
                <p>Rating: {state["reviews"][2]["rating"]}</p>
                <img src={state["images"][2]} />
            </li>
        </ul>
        '''
        return {"html": html}

