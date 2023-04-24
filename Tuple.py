'''
1.Tuples are immutable object type
2.We can use index to search the tuple
3.Python allows to negative indexing tuples
4.doing slicing make a another tuple
'''
tuple_1=(1,2,3,4,5);
print(type (tuple_1));
print(tuple_1[0])

tuple_2=(1,2,3,['a','b','c']);
print(tuple_2[3][0])
print(tuple_2[-2]);
print(tuple_2[:3]);

tuple_3=(1,2,3,4,5,['a','b','c','d']);

##Memory address
print(id(tuple_3));
tuple_4=tuple_3[5][3]='e'
print(tuple_3);

##Concating new Tuple
tupleIs=tuple_1+tuple_2+tuple_3;
print(tupleIs);

##functions in tuple
'''
1.all()
2.any()
3.len()
4.max()
5.min()
6.sum()
7.tuple()
8.index()
9.count()
'''
tuple_5=()
tuple_6_str='Abu Al Shahriar Rifat';
print(all (tuple_1));
print(all(tuple_4));
print(all(tuple_5));
print(any(tuple_5));
print(len(tuple_5));
print(max(tuple_1));
print(min(tuple_1));
print(sum(tuple_1));
print(tuple(tuple_1));
print(list(tuple_1));
print(tuple(tuple_6_str));
print(tuple_1.index(2));
print(tuple_1.index(3));
print(tuple_1.count(2));

'''Packing and Unpacking Tuples'''

a='Jhon',7,'3fet','20 kilos';
(Name,age,Height,weight)=('Rifat',25,'5.5 fet',65);
print(Name);
print(age);
print(Height);
print(weight);
x=2;
y=4;
x,y=y,x;
print(x,y)
##Iterating a tuple and operation on tuples
b=(1,2,3,4,5)
print(2 in b);
print(3 not in b);
print((1,3)>b);
print((1,2,3,4,5,6,7) is b);
print(id(b));





