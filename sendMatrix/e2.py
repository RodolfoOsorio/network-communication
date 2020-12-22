import json
import numpy
import sys

matrix= numpy.array( [ [52,55,61,66,70,61,64,73]]);
matrix= numpy.append(matrix, [ [63,59,55,90,109,85,69,72]],0)
matrix= numpy.append(matrix, [ [62,59,68,113,144,104,66,73]],0)
matrix= numpy.append(matrix, [ [63,58,71,122,154,106,70,69]],0)
matrix= numpy.append(matrix, [ [67,61,68,104,126,88,68,70]],0)
matrix= numpy.append(matrix, [ [79,65,60,70,77,68,58,75]],0)
matrix= numpy.append(matrix, [ [85,71,64,59,55,61,65,83]],0)
matrix= numpy.append(matrix, [ [87,79,69,68,65,76,78,94]],0)

#matrix = matrix.astype(numpy.uint8)
size = sys.getsizeof(matrix)
print("Matriz:\n",matrix)
print("Tamaño:",size)

a = matrix.tolist()
print("Conversion a lista: \n",a)
str = json.dumps(a)
print("Conversion a texto:\n",str)
tam_str = sys.getsizeof(str)
print("Tamaño final: ", tam_str)
