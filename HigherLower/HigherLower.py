import game_data
import random
import art
def game():
    print(art.logo)
    score = 0
    play=True

    person = random.choice(game_data.data)
    person2 = random.choice(game_data.data)
    while person==person2:
        person2=random.choice(game_data.data)


    while play:
        print(f"Compare A: {person['name']}, a {person['description']} from {person['country']}.")
        print(art.vs)
        print(f"Against B: {person2['name']}, a {person2['description']} from {person2['country']}.")
        a=person['follower_count']
        b=person2['follower_count']
        guess=input("Who has more followers? 'A' or 'B'?").lower()


        if (guess=='a' and a>b) or (guess=='b'and b>a):
            score+=1
            print(f"Your current score= {score}")
            person=person2
            person2 = random.choice(game_data.data)
            while person == person2:
                person2 = random.choice(game_data.data)


        else:
            print("You lost")
            play=False

game()