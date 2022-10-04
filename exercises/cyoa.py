"""Create your own adventure."""
__author__ = "730484416"


points: int = 0
player: str = ""
BED_EMOJI: str = "\U0001F6CF"
CHAIR_EMOJI: str = "\U0001FA91"
CRAB_EMOJI: str = "\U0001F980"
FISH_EMOJI: str = "\U0001F41F"
FROG_EMOJI: str = "\U0001F438"
HERB_EMOJI: str = "\U0001F33F"
OASIS_EMOJI: str = "\U0001F3DD"
SCORPION_EMOJI: str = "\U0001F982"
SEASHELL_EMOJI: str = "\U0001F41A"
SHAMROCK_EMOJI: str = "\U00002618"
STEW_EMOJI: str = "\U0001F372"
WORLD_MAP_EMOJI: str = "\U0001F5FA"


from random import randint


def greet() -> None:
    """Welcoming player and assigning their name."""
    global player
    print("Greetings, traveler! Are you prepared to explore the world?")
    print("Come with me as we traverse different lands, make friends, and make memories!")
    player = input("But wait! How can we travel together if I don't even know your name? Tell me, what do you go by? ")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    print(f"Oh, {player}, what a lovely name! Now, let us start our trek across the world. You'll gain points along the way based on what new experiences you may encounter.")


def forest() -> None:
    """Exploring a forest."""
    global points
    global player
    frog: str = ""
    leafy_plant: str = ""
    edible_or_nah: int = randint(1, 2)
    fishing: str = ""
    print(f"To the forest we go! As we enter, a frog{FROG_EMOJI} hops across the trail.")
    frog = input("Would you like to pet it? Or should we keep walking? (Be specific, either 'pet it' or 'keep walking'). ")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    if frog == "pet it":
        print(f"Congrats, {player}! The frog{FROG_EMOJI} hops up your arm as you pet it and sits on your shoulder. You've made a new friend! You've gained 5 points.")
        points += 5
    else:
        print(f"The frog{FROG_EMOJI} hops out of our way and we continue walking.") 
    print("As we adventure, your stomach grumbles. Luckily, you spot a leafy plant!")
    leafy_plant = input("Do you pick it up to inspect it? ('yes' or 'no'). ")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    if leafy_plant == "yes":
        print("After tearing a leaf from the plant and inspecting it, you find that it is...")
        if edible_or_nah == 1:
            print(f"Edible! You collect multiple leaves{SHAMROCK_EMOJI} and store them in your pack. You gain 3 points!")
            points += 3
            print("Fish would go great with your salad for dinner! You head to the nearby river.")
        else:
            print(f"Poison ivy{HERB_EMOJI}! Ouch! You drop the leaf but scratch your hand with your other hand, spreading the poison ivy. You lose 3 points!")
            points -= 3
            print("To soothe your irritated skin, you run to the nearby river to cool off. However, you're still hungry.")
    else:
        print(f"Probably a smart move. It could've been poison ivy{HERB_EMOJI}! Who knows, but you're still hungry. You see a river nearby and venture to it.")
    print(f"You pull out the fishing rod from your pack. Sending the reel out into the water, you hook a fat, juicy, salmon{FISH_EMOJI}!")
    fishing = input(f"Do you start a fire by the river to cook your fish{FISH_EMOJI}, or go back into the forest? (Be specific, 'by the river' or 'into the forest'). ")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    if fishing == "by the river":
        print("After gathering some wood from nearby, you finally start your fire.")
        print("Once you pierce your fish with a twig to rotate it above the fire though, you spot a bear in the river.")
        print(f"It's hungry, looking for salmon{FISH_EMOJI}, and at the scent of yours, perks up and sees you holding it.")
        print("The bear charges at your campsite and you run! The bear gobbles up your fish and you leave the forest hungry. You lose 5 points.")
        points -= 5
    else:
        print(f"After finding a patch of dirt in the forest, away from anything else that might catch fire, you set up a fire to cook your fish{FISH_EMOJI}.")
        print(f"After thoroughly cooked, you enjoy your dinner; it looks delicious, {player}! You gain 5 points.")
        points += 5
        print("With a full belly, you hit the hay, as we leave the forest the next day.")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")


def desert() -> None:
    """Exploring a desert."""
    global points
    global player
    thirsty_or_nah: str = ""
    oasis_or_mirage: int = randint(1, 10)
    scorpion: str = ""
    treasure: int = randint(1, 30)
    print(f"Geez, you must like it hot, {player}, because I'm sweating! ")
    print(f"Actually, I think I'm so hot that I must be delirious... Is that an oasis{OASIS_EMOJI} over there, or am I just seeing things?")
    thirsty_or_nah = input(f"Well, maybe we can get a closer look. Tell me, {player}, are you thirsty or what? ('yes' or 'no'). ")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    if thirsty_or_nah == "yes":
        print("Yeah? Well, so am I! Let's get closer to see if we can get some water.")
        if oasis_or_mirage % 2 == 0:
            print("Oh no, it looks like we were imagining things, it was all a mirage! You lose 3 points for still being thirsty.")
            points -= 3
        else:
            print("Well, if it isn't our lucky day! It wasn't a mirage after all! Let's take a couple sips to quench our thirst. You gain 3 points!")
            points += 3
    else:
        print("No? Well, I guess there's no need to head that way then. Let's keep going.")
    print(f"While you're walking across the hot sand, you notice a pointy tail sticking out from behind a cactus. It looks like it's a scorpion{SCORPION_EMOJI}!")
    scorpion = input(f"Do you pet the scorpion{SCORPION_EMOJI}? Or keep walking? (Be specific, 'pet the scorpion' or 'keep walking'). ")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    if scorpion == "pet the scorpion":
        print(f"Oh no, it looks like that was a bad idea! The scorpion{SCORPION_EMOJI} didn't appreciate that, so she stings you! You lose 5 points as your hand throbs.")
        points -= 5
    else:
        print(f"Sounds good! But wait, as you walk away, you turn back and notice the scorpion{SCORPION_EMOJI} is following you!")
        print("It... looks enamored by you! You gain 5 points for befriending the scorpion.")
        points += 5
    print("Well, let's keep going. There has to be something interesting in these endless dunes. Wait, do you see what I see? Is that... a temple over there?")
    print("As you approach the temple, you see a door that lets us inside. As we enter, we find...")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    if treasure <= 10:
        print("A handful of treasure! You gain 5 points for each gold!")
        points += 5
    elif 10 < treasure <= 20:
        print("A chest full of treasure! You gain 10 points for each diamond inside!")
        points += 10
    elif 20 < treasure <= 30:
        print("A room full of treasure! You gain 20 points for each chest in the room!")
        points += 20
    print("Wow, the desert can't get much better than this! Let's get out of here before we realize that was a mirage too!")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")


def beach(local_points: int) -> int:
    """Exploring a beach."""
    seashells: int = 0
    crabs: str = ""
    print("Ahh, the beach! It's bright and sunny, the water's clear, and the ocean breeze is nice and cool. It's a lovely day to adventure on the sand!")
    seashells = int(input(f"As we walk along the shore, you start examining seashells{SEASHELL_EMOJI}. You only choose the finest ones; how many do you pick? (1-10) "))
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    print(f"Wow, you picked up {seashells} seashells{SEASHELL_EMOJI}! You gain a point for each one.")
    local_points += seashells
    print("Wait a minute... it looks like one of these shells is moving...")
    crabs = input(f"Woah! That looks like a hermit crab{CRAB_EMOJI}! He's got one big pincher... are you scared of crabs? ('yes' or 'no') ")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    if crabs == "no":
        print(f"No? Well, good thing, because it looks like he wants to be your friend, {player}! You've gained five points for making a new friend.")
        local_points += 5
        print("Now, let's get out of here! Maybe we can take our new friend on another adventure.")
    else:
        print("No worries, I would be too! I'll just let him go. You lose one point for losing one of your shells, though.")
        local_points -= 1
        print("Now, let's get out of here! Who knows how many more of those things could be around...")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    return local_points


def arctic(local_points: int) -> int:
    """Exploring the arctic."""
    polar_bear_cub: str = ""
    igloo: str = ""
    stew: str = ""
    stew_status: int = randint(1, 3)
    beds: str = ""
    bed_status: int = randint(1, 3)
    chairs: str = ""
    print("Burrrr, it sure is cold here! And so bright with the sun shining so strongly on the snow...")
    print("Hey! Watch your step, I think I just saw something move, but I can't tell...")
    print(f"Woah! Is the snow around your feet... cuddling up to you? Wait a minute, that's a polar bear cub!")
    polar_bear_cub = input("Aww, it's so cute! Do you want to pet it? Or should we just go? (Be specific, 'pet it' or 'just go'). ")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    if polar_bear_cub == "pet it":
        print(f"I don't know if that was the best idea, {player}... Look up, I think that's its mom, headed straight for us! Let's bolt!")
        print("Well, it's a good thing we got out of there in time, but that was pretty scary. You lose 3 points since, y'know, you nearly killed us.")
        local_points -= 3
    else:
        print(f"Smart move, {player}, I think I saw a mama bear in the distance, but who knows, everything here is white!")
    print("Let's just keep going. Maybe if we keep walking in this freezing cold we'll walk up on a... hey! Is that an igloo?")
    igloo = input("That's definitely an igloo. Should we go inside? ('yes' or 'no'). ")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    if igloo == "no":
        print("Man, I'm freezing! And I know I see you shivering, don't lie! But alright, if you say so.")
        print("Tell me the truth here though, am I seeing things again or is that a family headed in there? Boy, what a lucky crowd they are!")
        print("Wait a minute, it looks like they've spotted us... I think they're waving -- wait, they're inviting us in!")
        print(f"Good job, {player}, they're welcoming us in for some food{STEW_EMOJI} and warmth. And we're entering without trespassing; you gain 5 points!")
        local_points += 5
    else:
        print("I agree! It's freezing out here, let's head on in.")
        stew = input(f"It looks like there's a few bowls of stew{STEW_EMOJI} on the table, should we split one? ('yes' or 'no'). ")
        print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
        if stew == "no":
            print(f"Man, {player}, I'm so hungry though! If you say so... Let's keep looking around.")
            beds = input(f"Hey, I think I see a few beds{BED_EMOJI}. Should we check one out? ")
            print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
        else:
            print("Alright, let's try this one!")
            if stew_status == 1:
                print(f"Yikes, that stew{STEW_EMOJI} must've been sitting out for a while. You gain 1 point for quenching your hunger, though.")
                local_points += 1
            if stew_status == 2:
                print("Wow, that was delicious! And the perfect temperature. You gain 3 points for quenching your hunger.")
                local_points += 3
            if stew_status == 3:
                print("Yikes! I just burned my tongue! That's wayyy too hot. Looks like you finished your half, though. You gain 1 point for quenching your hunger.")
                local_points += 1
            beds = input(f"Man, after that, I could use a nap. Should we take one of these three beds{BED_EMOJI}? ")
            print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
        if beds == "no":
            print("Y'know, maybe you're right. Who knows, one of them could have lice!")
            chairs = input("Well, at least tell me we can try the chairs in the living room. What do you think, should we? ('yes' or 'no'). ")
            print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
        else:
            print("Great, maybe we try this room?")
            if bed_status == 1:
                print(f"Oh boy, my bad, this bed{BED_EMOJI} is awful! It's sooo soft, horrible on my aging back. Looks like it's fine for you though; you gain one point for being able to rest.")
                local_points += 1
            if bed_status == 2:
                print(f"Geez, this bed{BED_EMOJI} is perfect! The pillows are so nice, this comforter is so soft, this mattress is...") 
                print("Oh, you're sleeping. Well, you gain 5 points when you wake up from the best nap of your life.")
                local_points += 5
            if bed_status == 3:
                print(f"Woah, is this even a bed{BED_EMOJI}? Feels more like bedROCK! Ha, get it? No? Hm, maybe I should've made an ice joke.") 
                print("Well, anyway, if you can sleep on it, you gain one point, and I think I see you drooling already.")
                local_points += 1
            chairs = input(f"Y'know, I think this bed{BED_EMOJI} feels a little too personal. Maybe we try the chairs{CHAIR_EMOJI} in the living room. What do you think, should we? ('yes' or 'no'). ")
            print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
        if chairs == "no":
            print("No? Really? Well, if you say so. Let's get out of here then. The arctic, I mean -- I can't stand this cold!")
        else:
            print(f"Great! Don't mind me, I'll just get reallll comfy in this chair{CHAIR_EMOJI}, feels pretty perfect to me...")
            print("Oh no, do you hear that metaphorical door unlocking? I do! Looks like the family's home, and they caught us trespassing!")
            print("You lose all points earned in this igloo. Now let's bolt before they can catch us; it's probably best if we leave the whole arctic!")
            local_points = 0
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    return local_points
            

def main() -> None:
    """Going through the create-your-own-adventure game."""
    global points
    global player
    where: str = ""
    play_again: str = ""
    greet()
    print(f"Tell me, {player}, where should we go? To the forest, desert, arctic, or beach? Or are we done travelling?") 
    where = input("Type your option exactly (forest, desert, arctic, beach, or done). ")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    if where == "forest":
        forest()
    elif where == "desert":
        desert()
    elif where == "arctic":
        points = arctic(0)
    elif where == "beach":
        points = beach(points)
    elif where == "done":
        print(f"Well, {player}, I sure had a lot of fun, and I hope you did too! That was quite an adventure we went on, and along the way, you accumulated {points} points! Come back soon to travel again!")
        quit()
    play_again = input("Wow, what an adventure! Should we go on another? ('yes' or 'no'). ")
    print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    while play_again == "yes":
        print(f"Tell me, {player}, where should we go next? To the forest, desert, arctic, or beach? Or are we done travelling?")
        where = input("Type your option exactly (forest, desert, arctic, beach, or done). ")
        print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
        if where == "forest":
            forest()
        elif where == "desert":
            desert()
        elif where == "arctic":
            points = arctic(0)
        elif where == "beach":
            points = beach(points)
        elif where == "done":
            print(f"Well, {player}, I sure had a lot of fun, and I hope you did too! That was quite an adventure we went on, and along the way, you accumulated {points} points! Come back soon to travel again!")
            quit()
        play_again = input(f"That was quite the experience you had, {player}! Should we go on another adventure? ('yes' or 'no'). ")
        print(f"{WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI} {WORLD_MAP_EMOJI}")
    print(f"Well, {player}, I sure had a lot of fun, and I hope you did too! That was quite an adventure we went on, and along the way, you accumulated {points} points! Come back soon to travel again!")


if __name__ == "__main__":
    main()