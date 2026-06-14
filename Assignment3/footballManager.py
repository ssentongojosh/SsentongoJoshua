import random

state = {
    "morale": 70,
    "fitness": 75,
    "phaseNum": 1,
    "result": "",
    "lastMatchPhase": 0,
    "lastMatchScore": "",
    "totalPoints": 0,
    "eliminated": False,
    "injuryCount": 0,
}


phases = {
    "Phase 1": {
        "label": "Training Camp",
        "description": "3 weeks before tournament, choose camp emphasis",
        "choices": [
            {
                "choice": "1. High intensity fitness block (fitness spike, morale dip)",
                "morale": -5,
                "fitness": 15,
            },
            {
                "choice": "2. Tactical Drills plus set pieces (balanced gain)",
                "morale": 5,
                "fitness": 5,
            },
            {
                "choice": "3. Rest and recovery sessions (High morale, fitness Risk)",
                "morale": 15,
                "fitness": -5,
            },
        ],
    },
    "Phase 2": {
        "label": "Friendly match selection",
        "description": "Two friendlies available, opponents affect team quality",
        "choices": [
            {
                "choice": "1. Two top 10 ranked nations (tough test, injury risk)",
                "morale": -5,
                "fitness": -5,
            },
            {
                "choice": "2. One strong, one medium ranked (balanced workload)",
                "morale": 5,
                "fitness": 0,
            },
            {
                "choice": "3. Two weaker oppostion teams (confidence, limited learning)",
                "morale": 10,
                "fitness": 5,
            },
        ],
    },
    "Phase 3": {
        "label": "Group stage game 1 - formation",
        "description": "Your first group match, pick your tactical setup",
        "choices": [
            {
                "choice": "1. 4-3-3 - Attack minded (Higher Scoring chance)",
                "matchMod": 1.3,
                "morale": 5,
                "fitness": -5,
            },
            {
                "choice": "2. 4-2-3-1 - Balanced (Default balance)",
                "matchMod": 1.0,
                "morale": 0,
                "fitness": 0,
            },
            {
                "choice": "3. 5-4-1 - Defensive Block (Protects Fitness, limits goals)",
                "matchMod": 0.7,
                "morale": -5,
                "fitness": 5,
            },
        ],
    },
    "Phase 4": {
        "label": "Group stage game 2 - squad rotation",
        "description": "3 days rest before match 2 - your players are tired",
        "choices": [
            {
                "choice": "1. Full first team again (Best lineup, fitness cost)",
                "matchMod": 1.2,
                "morale": 5,
                "fitness": -15,
                "aggressive": True,
            },
            {
                "choice": "2. Rotate 3-4 key players (Managed load)",
                "matchMod": 0.9,
                "morale": 5,
                "fitness": 5,
            },
            {
                "choice": "3. Heavy rotation - 7 plus changes (fresh legs, weaker XI)",
                "matchMod": 0.6,
                "morale": -10,
                "fitness": 15,
            },
        ],
    },
    "Phase 5": {
        "label": "Group Stage game 3 - win or draw enough?",
        "description": "Final group match, current standing affects approach",
        "choices": [
            {
                "choice": "1. Attack - need the win (All-out attack)",
                "matchMod": 1.4,
                "morale": 5,
                "fitness": -10,
                "aggressive": True,
            },
            {
                "choice": "2. Draw is fine - hold shape (Controlled)",
                "matchMod": 0.8,
                "morale": 0,
                "fitness": -5,
            },
            {
                "choice": "3. Press high from kickoff (intense, Risky)",
                "matchMod": 1.1,
                "morale": 10,
                "fitness": -10,
                "aggressive": True,
            },
        ],
    },
    "Phase 6": {
        "label": "Round of 16 - half time adjustments",
        "description": "You are level at half time, what do you tell team",
        "choices": [
            {
                "choice": "1. demand more intensity, push forward (High risk/Reward)",
                "matchMod": 1.3,
                "morale": 5,
                "fitness": -10,
                "aggressive": True,
            },
            {
                "choice": "2. Keep structure, one chance is enough (clinical approach)",
                "matchMod": 1.0,
                "morale": 5,
                "fitness": 0,
            },
            {
                "choice": "3. Defensive discipline, win in pens (penalty lottery)",
                "matchMod": 0.6,
                "morale": -5,
                "fitness": 10,
            },
        ],
    },
    "Phase 7": {
        "label": "Quarter Final - dealing with a red card",
        "description": "Your central midfielder is sent off in the 65th minute, you are level",
        "choices": [
            {
                "choice": "1. Defensive sub, park the bag (Damage control)",
                "matchMod": 0.7,
                "morale": -5,
                "fitness": 5,
            },
            {
                "choice": "2. Attacking sub, go for it 10 vs 11 (Heroic or Reckless)",
                "matchMod": 1.1,
                "morale": 10,
                "fitness": -10,
                "aggressive": True,
            },
            {
                "choice": "3. Reorganize shape, no sub yet (Tactical Discipline) ",
                "matchMod": 0.9,
                "morale": 5,
                "fitness": 0,
            },
        ],
    },
    "Phase 8": {
        "label": "semi-finals - fatigue is a factor",
        "description": "Five matches played, your squad is tired. two players in injury risk",
        "choices": [
            {
                "choice": "1. play te risk player - too important to rest (risk injury) ",
                "matchMod": 1.2,
                "morale": 5,
                "fitness": -15,
                "aggressive": True,
            },
            {
                "choice": "2. Rest them and trust the squad (safer but weaker XI)",
                "matchMod": 0.85,
                "morale": 5,
                "fitness": 5,
            },
            {
                "choice": "3. Start one, bench the other (compromise)",
                "matchMod": 1.0,
                "morale": 5,
                "fitness": -5,
            },
        ],
    },
    "Phase 9": {
        "label": "World Cup finals, extra time - penalties looming",
        "description": "60 minutes 1-1, do you play extra time or go for the winner",
        "choices": [
            {
                "choice": "1. push for a winner  (win it or lose it here)",
                "matchMod": 1.35,
                "morale": 15,
                "fitness": -10,
                "aggressive": True,
            },
            {
                "choice": "2. manage extra time, take pens (penalty shootouts)",
                "matchMod": 0.9,
                "morale": 0,
                "fitness": 0,
            },
            {
                "choice": "3. Concede possesion, hit on counter (disciplined counter)",
                "matchMod": 1.05,
                "morale": 5,
                "fitness": 5,
            },
        ],
    },
}


print("#" * 80)
print("")
print("#" * 10 + "    Welcome to the football Manager    " + "#" * 10)
print("")
print(
    """Your choices for each pre-tournament phase and match phase
    affects your players and hence your teams chance to win the world cup
    """
)
print("Choose wisely!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("#" * 80)
print("\n\n")


def clamp(value, min, max):
    if value > max:
        return max
    elif value < min:
        return min
    return value


def processNonMatchPhaseDecision(phaseNum, choice):
    phase = f"Phase {phaseNum}"
    state["morale"] = clamp(
        state["morale"] + phases[phase]["choices"][choice - 1]["morale"], 0, 100
    )
    state["fitness"] = clamp(
        state["fitness"] + phases[phase]["choices"][choice - 1]["fitness"], 0, 100
    )
    state["phaseNum"] += 1
    displayPhaseChoices(state["phaseNum"])


def processMatchPhaseDecision(phaseNum, choice):
    phase = f"Phase {phaseNum}"
    state["morale"] = clamp(
        state["morale"] + phases[phase]["choices"][choice - 1]["morale"], 0, 100
    )
    state["fitness"] = clamp(
        state["fitness"] + phases[phase]["choices"][choice - 1]["fitness"], 0, 100
    )

    if state["fitness"] < 40:
        state["morale"] -= 5

    effectiveMod = phases[phase]["choices"][choice - 1]["matchMod"]
    if state["fitness"] < 30:
        effectiveMod = min(effectiveMod, 0.85)

    base = (state["fitness"] / 100) * (state["morale"] / 100)
    threshold = effectiveMod * base
    roll = random.randint(0, 1)

    if roll < threshold * 0.55:
        state["totalPoints"] += 3
        state["result"] = "WIN"
    elif roll < threshold * 0.88:
        state["totalPoints"] += 1
        state["result"] = "DRAW"
    else:
        state["totalPoints"] += 0
        state["result"] = "LOSS"

    if state["result"] == "WIN":
        state["lastMatchScore"] = str(random.randint(1, 3)) + " - " + str(random.randint(0, 1))
    elif state["result"] == "DRAW":
        state["lastMatchScore"] = str(random.randint(0, 2)) + " - " + str(random.randint(0, 2))
    else:
        state["lastMatchScore"] = str(random.randint(0, 1)) + " - " + str(random.randint(1, 3))
    state["lastMatchPhase"] = phaseNum

    if state["fitness"] < 50 and phases[phase]["choices"][choice - 1].get("aggressive"):
        injuryChance = 0.4
    elif state["fitness"] < 50:
        injuryChance = 0.2
    else:
        injuryChance = 0.1
    if random.randint(0, 1) < injuryChance:
        state["fitness"] -= 15
        state["fitness"] = clamp(state["fitness"], 0, 100)
        state["injuryCount"] += 1

    if phaseNum == 5 and state["totalPoints"] < 3:
        state["eliminated"] = True
        printCampaignOver(phaseNum)
        return
    if phaseNum >= 6 and state["result"] == "LOSS":
        state["eliminated"] = True
        printCampaignOver(phaseNum)
        return
    state["phaseNum"] += 1
    displayPhaseChoices(state["phaseNum"])


def displayPhaseChoices(phaseNum):
    phase = f"Phase {phaseNum}"
    phaseLabel = phases[phase]["label"]
    phaseDescription = phases[phase]["description"]
    phaseChoices = phases[phase]["choices"]
    print(f"{phase} : {phaseLabel}")
    print(phaseDescription)
    print("")
    for choice in phaseChoices:
        print(choice["choice"])
    print("\n")
    displayState(phaseNum)
    selectChoice(state["phaseNum"])


def displayState(phaseNum):
    print(
        "morale : " + "#" * int((state["morale"] / 10)) + "   " + str(state["morale"])
    )
    print(
        "fitness: " + "#" * int((state["fitness"] / 10)) + "   " + str(state["fitness"])
    )
    print("\n")
    if phaseNum >= 4 and state["lastMatchPhase"] >= 3:
        previousPhase = f"Phase {state['lastMatchPhase']}"
        print("############## Match Log ################")
        print(phases[previousPhase]["label"].split("-")[0])
        print(f"{state['lastMatchScore']} : {state['result']}")
        
        
def manage():
    pass


def printCampaignOver(phaseNum):
    phase = f"Phase {phaseNum}"
    phaseTitle = phases[phase]["label"].split("-")[0]
    print("")
    print("Your campaign is over.")
    print(
        f"You went out at the {phaseTitle} ({state['lastMatchScore']}). Total points in group: {state['totalPoints']}."
    )


def selectChoice(phaseNum):
    while True:
        rawChoice = input("Enter your choice : ").strip()
        if not rawChoice.isdigit():
            print("")
            print("Invalid choice, Try again. (Enter 1,2 or 3) ")
            continue

        choice = int(rawChoice)

        print("")
        match choice:
            case n if 1 <= n <= 3:
                if phaseNum <= 2:
                    processNonMatchPhaseDecision(phaseNum, choice)
                else:
                    processMatchPhaseDecision(phaseNum, choice)
                break
            case _:
                print("Invalid choice, Try again. (Enter 1,2 or 3) ")


displayPhaseChoices(1)
