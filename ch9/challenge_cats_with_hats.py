num_cats = 100
num_laps = 100
cats_with_hats = []

for lap in range(1,num_laps+1):
    for cat in range(1,num_cats+1):
        if cat % lap == 0:
            if cat in cats_with_hats:
                cats_with_hats.remove(cat)
            else:
                cats_with_hats.append(cat)


print(cats_with_hats)