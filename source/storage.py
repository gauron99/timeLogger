#storage.py

# this just holds parameters that could be modified by user such as categories
# and keywords


# ------------------- ADD YOUR OWN CATEGORIES AND KEYWORDS ------------------- #
#       -- new category -> add new key
#                       -> create keywords (values) for said category
#
#       -- new key words-> add them in list (values of category key)
#
# --> can we I add this as config options? :thinking:
# ------------------- ADD YOUR OWN CATEGORIES AND KEYWORDS ------------------- #

_categories_keywords = \
  {
  'gaming'      : ['rocket league','horizon zero dawn','games','gaming'],
  'programming' : ['coding','code','testing code','programming'],
  'food'        : ['lunch','breakfast','dinner','food','eating'],
  'outside'     : ['running','exercise','workout','walk','outside','Max walk'],
  'inside'      : ['reading','writing','board games'],
  'hygiene'     : ['hygiene','shower'],
  'school'      : ['studying','school','learning'],
  'nothing'     : ['watching tv','watching twitch','watching youtube','chilling',
                  'chillin'],
  'other'       : []
  }