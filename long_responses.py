import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_HELP= "What can i help you with today!"
R_JOKE="Your mom"
R_GENDER="Go get your sight checked! , i'm a bot "

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?",
                "Happy now","good day"][
        random.randrange(6)]
    return response