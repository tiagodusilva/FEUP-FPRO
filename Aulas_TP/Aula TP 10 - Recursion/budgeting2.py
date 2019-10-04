def budgeting2(budget, products, wishlist):

    def test_Value(total, combination):
        if total > budget:
            return -1, {}
        best = (total, combination.copy())
        #print("Inicial " + str(combination))
        for key in combination:
            if combination[key] < wishlist[key]:
                combination[key] += 1
                aux, comb1 = test_Value(total + products[key], combination)
                if aux > best[0]:
                    best = (aux, comb1.copy())
                    #print("Updated best: " + str(best))
                combination[key] -= 1
        return best

    dic = {}
    for key in wishlist:
        dic[key] = 0

    bestValue, dic = test_Value(0, dic)

    #Tratar o resultado
    result = {}
    for key in dic:
        if dic[key] != 0:
            result[key] = dic[key]

    return result


#print(budgeting2(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40, 'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))
#print(budgeting2(1500, {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100}, {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox': 1}))
print(budgeting2(1200, {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100}, {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox': 1}))
#print(budgeting2(1000, {'laptop': 2000, 'jeans': 50}, {'laptop': 2, 'jeans': 3}))
