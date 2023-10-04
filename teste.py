from math import log
number = int('11111111011000010110001001100011', 2)
result_ones = list()
count_ones = int(log(number, 2))
number_reduced = int(number)
while count_ones >= 0 and number_reduced > 0: ## Colocar aqui um timer remaining
  ones = list()
  while len(ones) < 131072 -1 and count_ones >= 0 and number_reduced > 0:
    if number_reduced & 1 == 1:
      ones.append(count_ones)
      print ("TESTE count_ones: ", count_ones, "number_reduced: ", number_reduced)
    print ("TESTE2 count_ones: ", count_ones, "number_reduced: ", number_reduced, 'number_reduced & 1 == 1:', number_reduced & 1 == 1, 'number_reduced & 1: ', number_reduced & 1, bin(number_reduced))
    count_ones-=1
    number_reduced = number_reduced >> 1
  result_ones.append(ones)
print(result_ones)