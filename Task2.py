import requests
import os, time

# Help! I'm trying to make this cool bot but my code is too messy :( Please help me organise it into reusable components.

# Define your reusable functions here:
# Make sure each function only does ONE thing!!!!!!!!!!!

def guess_gender(gender_resp,gender)  :
    prob_percent = gender_resp["probability"] * 100
    return [gender, prob_percent]

###########################################

def weird_weather_bot(f,gender,prob_percent,gender_correct,area,joke,weather_degrees,main_weather_desc, second_weather_desc)   :
    print(f.renderText("HEY!"))
    print("Welcome to the weird weather bot :)")
    print("-----------------------------------\n")
    print(f"\nHmmm, I'm {prob_percent}% sure you are a {gender}.")
    if gender_correct.lower() in ["", "yes", "y", "ye"]:
        print("Wooooooh! Computer 1, Human 0.")
    else:
        print("Ahhhh, sorry! :(")
    print(f"Nice! so you live in {area}.\n")
    print("Let me just check the weather there today...\n")
    for i in range(3):
        time.sleep(1)
        print("...")
    
    input("\nWould you like a cat fact while you wait? ")
    print("Doesn't matter what you think, I'm going to give you one anyway :)")
    time.sleep(3)
    print("\n###########################")
    print("CAT FACT:")
    print(f"\n{joke}\n")
    print("So interesting isn't it!")
    print("###########################")
    print("\nWaiting 5 seconds for you to read the fact...")
    time.sleep(5)
    print("\nNow, back to getting the weather...")
    for i in range(3):
        time.sleep(1)
        print("...")

    
    # convert to degrees
    print(f"\nThe weather in {area}:\n")
    print(str(weather_degrees) + "℃")
    print(f"{main_weather_desc} - {second_weather_desc}")
    print("\nThank you! Bye.")



# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
#ALl of the aforementioned variables that the function is defined by must have a value.
# 2. Validate the user's input based on your preconditions.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
    #It saved a lot of space when coding for the weather bot and any changes to the reusable components for example (weather_degrees)would be made easily.
# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. Make sure all of your functions (except the main one) only do ONE thing or process.
# 3. Add your own twist to the code.

# Extension:
# Add the following apis as reusable components and use them in your code:
# https://www.exchangerate-api.com/docs/overview
