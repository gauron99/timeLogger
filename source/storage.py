#storage.py

# this just holds parameters that could be modified by user such as categories
# and keywords


# ------------------- ADD YOUR OWN CATEGORIES AND KEYWORDS ------------------- #
#       -- new category -> add to _categories list
#                       -> create keywords for said category
#       -- new key words-> add them in _keywords list
#                       -> pair categories & keyowrds in (GiveKeyWordGetCategory())
#
# --> can we I add this as config options? :thinking:
# ------------------- ADD YOUR OWN CATEGORIES AND KEYWORDS ------------------- #


_categories = ['gaming','programming','food','outside','inside','hygiene','school','nothing']

# list of all keaywords, they are separated by categories for better visual orientation
# each line represents different category(add your own here & in func GiveKeyWordGetCategory()
# so they can be asigned to given category)
_keywords = ['rocket league','horizon zero dawn','games','gaming',
            'coding','code','testing code','programming',
            'lunch','breakfast','dinner','food','eating',
            'running','exercise','workout','walk','outside',
            'reading','writing',
            'hygiene','shower',
            'studying','school','learning',
            'watching tv','watching twitch','watching youtube','chilling']

