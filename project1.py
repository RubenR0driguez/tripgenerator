import random
trip_destinations = ['bridgeport', 'milford','stratford', 'waterbury']
connecticut_restaurants =['the station', "santo's restaurant", 'anvenue bar and grill','brass city bistro']
transport_options = ['car rental', 'walking', 'bike','uber']
connecticut_entertainment= ['mystice aquarium', 'lake compounce', 'yale peabody museum', 'sleeping giant']

def travel_day():
    

    entertain=random.choice(connecticut_entertainment)
    transpo=random.choice(transport_options)
    restaurants=random.choice(connecticut_restaurants)
    destination=random.choice(trip_destinations)

    user_input='no'
    while user_input == 'no':
        print(f'is {destination} your  destination? ')
        user_input = input ('yes or no')
        if user_input == 'no':
            destination=random.choice(trip_destinations)

    
        
    user_input='no'
    while user_input == 'no':
        print(f'would you like to use {transpo} as transportation?') 
        user_input= input('yes or no')
        if user_input=='no':
            transpo=random.choice(transport_options)
    user_input='no'
    while user_input =='no':
        print(f'is {restaurants} your for food? ')
        user_input= input('yes or no')
        restaurants=random.choice(connecticut_restaurants)

    user_input='no'
    while user_input =='no':
        print(f'is {entertain} your entertainment today? ')
        user_input= input('yes or no')
        if user_input=='no':
            entertain=random.choice(connecticut_entertainment)

    print(entertain)
    print(transpo)
    print(restaurants)
    print(destination)
    
    print(f'these are your slecections {destination},{transpo},{restaurants},{entertain} hope you enjoy your day and have fun!')





travel_day()
