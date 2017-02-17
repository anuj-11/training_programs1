import pickle
my_list = [1,2,3,4,5]
my_dict = {'name':'anuj'}
my_str = 'asm tech'
f = open('file.txt','w')
#pickle.dump(my_list, f)
print pickle.dumps(my_list)
pickle.dump(my_dict, f)



