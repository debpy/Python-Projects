moms =[
    ("Ned", "Eleanor"),
    ("Max", "Susan"),
    ("Susan", "Shelly")
]

def find_mom(moms, child):
    for child_name, mom_name in moms:
        if child_name == child:
            return mom_name
    return None

#print(find_mom(moms, 'Susan'))


def how_many_grandmothers(moms):
    grandmothers = 0
    for child, mom in moms:
        grandma = find_mom(moms, mom)
        if grandma:
            grandmothers+=1
    return grandmothers

print(how_many_grandmothers(moms))
