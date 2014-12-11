import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def get_pref():
  preferences = {}

  for pref, question in questions.iteritems():
    print question
    preferences[pref] = raw_input().lower() in ['y', 'yes']
    print ""

  return preferences

def build_drink(preferences):
  drink = []
  for ingredient_kind, liked in preferences.iteritems():
    if not liked:
      continue

    drink.append(random.choice(ingredients[ingredient_kind]))
  return drink

def main():
	preferences = get_pref()
	drink = build_drink(preferences)
	print "Here be yer drink, Sailor!"
	print "This here is the concoction:"
	for ingredient in drink:
		print "A {}".format(ingredient)

if __name__ == "__main__":
	main()

