# Processing
def crafting_minecraft(recipeName):
   recipes = {
       "torch": [
           [["air", "air", "air"], ["air", "coal", "air"], ["air", "sticks", "air"]]
       ],
       "slime_ball": [
           [["air", "air", "air"], ["air", "slime_block", "air"], ["air", "air", "air"]]
       ],
       "tnt": [
           [["gunpowder", "sand", "gunpowder"], ["sand", "gunpowder", "sand"], ["gunpowder", "sand", "gunpowder"]],
           [["gunpowder", "red_sand", "gunpowder"], ["red_sand", "gunpowder", "red_sand"], ["gunpowder", "red_sand", "gunpowder"]]
       ],
       "diamond_sword": [
           [["air", "diamond", "air"], ["air", "diamond", "air"], ["air", "sticks", "air"]]
       ]
   }

   if recipeName in recipes:
       if len(recipes[recipeName]) == 1:
           print("{} recette trouvée".format(len(recipes[recipeName])))
       else:
           print("{} recettes trouvées".format(len(recipes[recipeName])))
       for recipe in recipes[recipeName]:
           print(recipe)
   else:
       print("0 recettes trouvées")


# Unit Tests API Input
# crafting_minecraft(lines[0])


# Tests
crafting_minecraft("torch")             # Must return "1 recette trouvée\n[['air', 'air', 'air'], ['air', 'coal', 'air'], ['air', 'sticks', 'air']]"
crafting_minecraft("tnt")               # Must return "2 recettes trouvées\n[['gunpowder', 'sand', 'gunpowder'], ['sand', 'gunpowder', 'sand'], ['gunpowder', 'sand', 'gunpowder']]\n[['gunpowder', 'red_sand', 'gunpowder'], ['red_sand', 'gunpowder', 'red_sand'], ['gunpowder', 'red_sand', 'gunpowder']]"
crafting_minecraft("slime_ball")        # Must return "1 recettes trouvée\n[['air', 'air', 'air'], ['air', 'slime_block', 'air'], ['air', 'air', 'air']]"
crafting_minecraft("diamond_sword")     # Must return "1 recette trouvée\n[['air', 'diamond', 'air'], ['air', 'diamond', 'air'], ['air', 'sticks', 'air']]"
crafting_minecraft("concrete")          # Must return "0 recettes trouvées"