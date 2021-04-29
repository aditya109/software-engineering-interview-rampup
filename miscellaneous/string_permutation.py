result= []
def permute(data, i, length): 
    if i == length: 
        result.append(''.join(data))
    else: 
        for j in range(i, length): 
            # swap
            data[i], data[j] = data[j], data[i] 
            permute(data, i + 1, length) 
            data[i], data[j] = data[j], data[i]  

permute(list('abc'), 0, len('abc'))
print(result)
