def budgeting(budget, products, wishlist):
    cost = ()
    for key in products:
        cost += ((key, products[key]), )
    cost = tuple(sorted(cost, key=lambda elem: elem[1]))

    spending = 0
    for key in wishlist:
        spending += products[key] * wishlist[key]

    i = 0
    while spending > budget:
        if wishlist.get(cost[i][0], 0) > 0:
            print(cost[i][0])
            wishlist[cost[i][0]] -= 1
            spending -= cost[i][1]
            if wishlist[cost[i][0]] == 0:
                del wishlist[cost[i][0]]
        else:
            i += 1
    return wishlist


#print(budgeting(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40, 'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))
#print(budgeting(1500, {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100}, {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox':1}))
#print(budgeting(1200, {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100}, {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox':1}))
#print(budgeting(750, {'nintendo': 100, 'mouse': 20, 'hoodie': 45, 'backpack': 30, 'tv': 300}, {'nintendo': 1, 'mouse': 1, 'hoodie': 4, 'tv': 2}))
