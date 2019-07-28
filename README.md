# Restaurant-Selector

***First project using a fully functional Class object.***

Finds restaurants nearby, user selects what looks good, computer picks the final restaurant.

Uses Google Places API to find nearby restaurants using user's zip code.

Sends the Get request 3 times (max allowed by Google) and compiles the list using 'Name' fields from json. 

Then outputs the list in two columns in the console with numbers.
(The display section was the hardest part and it's still not perfect.)

User selects as many restaurants as they wish by typing the number for their selection followed by 1 space.

Ex: 3 17 22 9 38 16

These selections get added to a dictionary and the computer then uses randint to pick a final place.

