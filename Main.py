from Files.GetRestaurants import RestaurantList
import time, sys, os
from random import randint

rest_dict = {}
final_options = []


def select_restaurants():

    x = list(map(int, input("Make your selections: ").split()))
    print('\n')
    for i in x:
        print(rest_dict[i])
        final_options.append(rest_dict[i])
    print('\n')


def display_list_onscreen():
    RestaurantList.results.sort()                                       # Alphabetize lists for display
    all_restaurants_even = RestaurantList.results[0:][::2]
    all_restaurants_odd = RestaurantList.results[1:][::2]
    if len(RestaurantList.results) % 2 == 0:
        a = 0
        while a < len(all_restaurants_even):
            for r_item in all_restaurants_even:
                item_index = all_restaurants_even.index(r_item)
                right_column = item_index + len(all_restaurants_even) + 1
                line = '{:<3}{:<35} {:>35} {:>3}'.format(str(item_index + 1), r_item,
                                                         right_column, all_restaurants_odd[item_index])
                try:
                    print(line)
                    rest_dict.update({item_index + 1: r_item})
                    rest_dict.update({right_column: all_restaurants_odd[item_index]})
                    a += 1
                except IndexError:
                    pass
    else:
        a = 0
        last = len(all_restaurants_even) - 1
        while a < len(all_restaurants_even) - 1:
            for r_item in all_restaurants_even:
                item_index = all_restaurants_even.index(r_item)
                right_column = item_index + len(all_restaurants_even) + 1
                line = '{:<3}{:<35} {:>35} {:>3}'.format(item_index + 1, r_item,
                                                         right_column, all_restaurants_odd[item_index])
                try:
                    print(line)
                    rest_dict.update({item_index + 1: r_item})
                    rest_dict.update({right_column: all_restaurants_odd[item_index]})
                    a += 1
                except IndexError:
                    pass
        print(str(last + 1), all_restaurants_even[last])
        rest_dict.update({last: all_restaurants_even[last]})
    print('\n')


def main_program_flow():

    # Begin building the list using calls to the RestaurantList class.
    # This section sends API requests and assembles the list.
    # It then removes duplicates and sets the list as global for use in the next section.

    print("Starting 5-2-1...", "\n")
    time.sleep(1.25)
    getzip = input("Enter your zip code: ")                         # Take zip code from user

    try:
        r_list = RestaurantList(getzip)                             # Create instance of RestaurantList
        print("\n", "Getting list of nearby restaurants...", "\n")
        r_list.get_request(r_list.query)                            # Send GET request for json data
        r_list.build_list(r_list.y)                                 # Begin assembling restaurant list
        w = 0
        if len(RestaurantList.results) > 0:                         # Check for multiple pages (20 per. 3 total)
            while w < 2:
                if len(RestaurantList.results) > 39:
                    r_list.next_page(r_list.n)
                    time.sleep(1)
                    r_list.get_request(r_list.next)
                    r_list.build_list(r_list.y)
                    w = 2
                elif len(RestaurantList.results) == 20:
                    r_list.next_page(r_list.n)
                    time.sleep(1)
                    r_list.get_request(r_list.next)
                    r_list.build_list(r_list.y)
                    w += 1
                else:
                    w = 2
        else:
            print('No restaurants found...')
            main_program_flow()
    except ValueError:
        print("\n", "Not a valid zip code. Try again...", "\n")
        main_program_flow()

    # Print out the list with numbers so the user can select restaurants.
    # User must type numbers followed by space. Ex: 3 12 6 24 47 9...
    # The selections are appended to a new list where the computer will select the final pick.

    display_list_onscreen()                                  # Display restaurants on screen in 2 columns with numbers

    select_restaurants()                                     # Prompt to select all that apply

    end = len(final_options) - 1                             # Computer selects final place
    final_pick = final_options[randint(0, end)]
    ending = ["The choice is", ".", ".", "."]
    for i in ending:
        print(i, end="")
        sys.stdout.flush()
        time.sleep(1)
    print('\n')
    print(final_pick)
    input()


os.system("mode con cols=160 lines=50")
main_program_flow()
