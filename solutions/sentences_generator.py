def sentences_generator(sujets, verbes, complements):
    for s in sujets:
        for v in verbes:
            for c in complements:
                print("{} {} {}.".format(s, v, c))


# Unit Tests API Input
# sentences_generator(lines[0], lines[1], lines[2])


# Tests
sentences_generator(["Le chat", "Ce soir, je", "En vain, il"], ["cherche", "jette", "fume"], ["un raton-laveur", "de l'alcool", "un nuage"])
"""
Must return :

Le chat cherche un raton-laveur.
Le chat cherche de l'alcool.
Le chat cherche un nuage.
Le chat jette un raton-laveur.
Le chat jette de l'alcool.
Le chat jette un nuage.
Le chat fume un raton-laveur.
Le chat fume de l'alcool.
Le chat fume un nuage.
Ce soir, je cherche un raton-laveur.
Ce soir, je cherche de l'alcool.
Ce soir, je cherche un nuage.
Ce soir, je jette un raton-laveur.
Ce soir, je jette de l'alcool.
Ce soir, je jette un nuage.
Ce soir, je fume un raton-laveur.
Ce soir, je fume de l'alcool.
Ce soir, je fume un nuage.
En vain, il cherche un raton-laveur.
En vain, il cherche de l'alcool.
En vain, il cherche un nuage.
En vain, il jette un raton-laveur.
En vain, il jette de l'alcool.
En vain, il jette un nuage.
En vain, il fume un raton-laveur.
En vain, il fume de l'alcool.
En vain, il fume un nuage.
"""

sentences_generator(["The cat", "Tonight, I", "In vain, he"], ["search(es)", "throw(s)", "smoke(s)"], ["a racoon", "a lot of alcohol", "a cloud"])
"""
Must return :

The cat search(es) a racoon.
The cat search(es) a lot of alcohol.
The cat search(es) a cloud.
The cat throw(s) a racoon.
The cat throw(s) a lot of alcohol.
The cat throw(s) a cloud.
The cat smoke(s) a racoon.
The cat smoke(s) a lot of alcohol.
The cat smoke(s) a cloud.
Tonight, I search(es) a racoon.
Tonight, I search(es) a lot of alcohol.
Tonight, I search(es) a cloud.
Tonight, I throw(s) a racoon.
Tonight, I throw(s) a lot of alcohol.
Tonight, I throw(s) a cloud.
Tonight, I smoke(s) a racoon.
Tonight, I smoke(s) a lot of alcohol.
Tonight, I smoke(s) a cloud.
In vain, he search(es) a racoon.
In vain, he search(es) a lot of alcohol.
In vain, he search(es) a cloud.
In vain, he throw(s) a racoon.
In vain, he throw(s) a lot of alcohol.
In vain, he throw(s) a cloud.
In vain, he smoke(s) a racoon.
In vain, he smoke(s) a lot of alcohol.
In vain, he smoke(s) a cloud.
"""

sentences_generator(["Je", "Le chat"], ["mange", "frappe"], ["une souris", "à la fenêtre"])
"""
Must return :
Je mange une souris.
Je mange à la fenêtre.
Je frappe une souris.
Je frappe à la fenêtre.
Le chat mange une souris.
Le chat mange à la fenêtre.
Le chat frappe une souris.
Le chat frappe à la fenêtre.
"""
