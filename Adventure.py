name = input("Enter Your Name: ")
print(f"\n~|| Let's Start The Adventure {name} ||~\n")

character = input("Choose your Character Name (Arthur/Kirito/Daniel): ").lower()

if character == "arthur":
    print("\nYou are an 18-year-old boy in the world of swords and war!\n")
    weapon = input("Choose your weapon (Sword/Axe): ").lower()
    
    if weapon == "sword":
        print("You are an E-rank Warrior with a specialty in Sword Art.\n")
    elif weapon == "axe":
        print("You are an E-rank Warrior with a specialty in Axe as a weapon.\n")
    else:
        print("Invalid input. You lose the game.")
        exit()

    # First Challenge
    help_village = input("A village is under attack. Do you help? (yes/no): ").lower()
    if help_village == "yes":
        print("\nYou gain allies and respect.")
        treasure_hunt = input("You are invited to a feast and learn about a hidden treasure. Do you search for it? (yes/no): ").lower()
        if treasure_hunt == "yes":
            print("You find a magical artifact that boosts your power.\n")
        else:
            print("You gain more time to train and improve your skills.\n")
    else:
        print("\nYou continue your journey but gain a reputation for being selfish.")
        bandit_encounter = input("You encounter a bandit ambush. Do you fight or flee? (fight/flee): ").lower()
        if bandit_encounter == "fight":
            print("You defeat the bandits and gain their loot.\n")
        else:
            print("You escape but lose valuable time.\n")

    # Additional Subplot
    mysterious_stranger = input("You meet a mysterious stranger who offers a quest. Do you accept? (yes/no): ").lower()
    if mysterious_stranger == "yes":
        print("You embark on a quest that leads to unexpected adventures.\n")
    else:
        print("You decline and continue on your path.\n")

    # Betrayal
    pursue_traitor = input("A trusted companion betrays you. Do you pursue the traitor? (yes/no): ").lower()
    if pursue_traitor == "yes":
        print("You confront the traitor and recover the artifact.")
        conspiracy = input("You learn of a conspiracy against the kingdom. Do you expose it? (yes/no): ").lower()
        if conspiracy == "yes":
            print("You gain the king's favor and new allies.\n")
        else:
            print("You use the information for personal gain.\n")
    else:
        print("You focus on your mission, gaining valuable experience.")
        mentor_offer = input("A mysterious mentor offers to teach you forbidden techniques. Do you learn them? (yes/no): ").lower()
        if mentor_offer == "yes":
            print("You gain powerful skills but risk corruption.\n")
        else:
            print("You maintain integrity and gain a loyal friend.\n")

    # Climax
    save_kingdom = input("Do you save the kingdom or pursue revenge? (save/revenge): ").lower()
    if save_kingdom == "save":
        print("You lead a successful defense and become a hero.")
        advisor_offer = input("You are offered a position as a royal advisor. Do you accept? (yes/no): ").lower()
        if advisor_offer == "yes":
            print("You live a life of honor and influence.\n")
        else:
            print("You continue adventuring and gain legendary status.\n")
    else:
        print("You risk everything for personal satisfaction.")
        final_duel = input("You face your nemesis in a final duel. Do you spare them? (yes/no): ").lower()
        if final_duel == "yes":
            print("You gain redemption and a new ally.\n")
        else:
            print("You achieve revenge but lose your way.\n")

elif character == "kirito":
    print("\nYou are a 19-year-old hacker in a highly evolved future world!\n")
    network_infiltration = input("Do you infiltrate the network or avoid detection? (infiltrate/avoid): ").lower()
    if network_infiltration == "infiltrate":
        print("You gather intelligence on the organization's plans.\n")
    else:
        print("You remain undetected but miss crucial information.\n")

    rogue_ai = input("You encounter a rogue AI. Do you trust it? (yes/no): ").lower()
    if rogue_ai == "yes":
        print("You gain a powerful ally but risk betrayal.\n")
    else:
        print("You miss out on valuable assistance but remain safe.\n")

    friend_danger = input("A friend is in danger. Do you save them? (yes/no): ").lower()
    if friend_danger == "yes":
        print("You risk exposure but gain loyalty and support.\n")
    else:
        print("You prioritize the mission but lose a potential ally.\n")

    # Additional Subplot
    rival_hacker = input("A rival hacker tries to sabotage you. Do you confront them? (yes/no): ").lower()
    if rival_hacker == "yes":
        print("You outsmart the rival and gain an advantage.\n")
    else:
        print("You avoid confrontation but miss an opportunity.\n")

    final_boss = input("Do you confront the final boss directly or use strategy? (direct/strategy): ").lower()
    if final_boss == "direct":
        print("You face the final boss, Sosuke, head-on.\n")
    else:
        print("You use cunning and strategy to outsmart the boss.\n")

elif character == "daniel":
    print("\nYou are a 21-year-old high schooler with a knack for solving mysteries!\n")
    strange_occurrences = input("Do you investigate strange occurrences or ignore them? (investigate/ignore): ").lower()
    if strange_occurrences == "investigate":
        print("You discover clues about a secret society.\n")
    else:
        print("You miss early warning signs but avoid initial danger.\n")

    secret_society = input("Do you confront the secret society or gather evidence? (confront/gather): ").lower()
    if secret_society == "confront":
        print("You gain valuable information but risk exposure.\n")
    else:
        print("You remain hidden but take longer to uncover the truth.\n")

    friend_involvement = input("A friend is involved. Do you expose them or protect them? (expose/protect): ").lower()
    if friend_involvement == "expose":
        print("You risk losing a friendship but gain credibility.\n")
    else:
        print("You maintain friendship but lose trust from others.\n")

    # Additional Subplot
    school_election = input("A school election is happening. Do you get involved? (yes/no): ").lower()
    if school_election == "yes":
        print("You influence the election and gain new allies.\n")
    else:
        print("You stay out of it but miss a chance to make a difference.\n")

    school_event = input("Do you reveal the truth at a school event or stay silent? (reveal/silent): ").lower()
    if school_event == "reveal":
        print("You expose the society at a school event.\n")
    else:
        print("You keep the secret but gain leverage for future use.\n")

else:
    print("Invalid character choice. You lose the game.\n")

print(f"Thank you for trying, {name}.\n")