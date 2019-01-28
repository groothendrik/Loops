#break

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'

for dogs in dog_breeds_available_for_adoption:
  print(dogs)
  if dogs == dog_breed_I_want:
    print("They have the dog I want!")
    break