from django.shortcuts import render
from .main_agent import Main_Agent

# Create your views here.

def generate(request):
    agent = Main_Agent(request.POST["query"])
    final_state = agent.run()
    print(final_state["collected"])
    return render(request, "game_recommendation.html", {"t": final_state["html"]})
