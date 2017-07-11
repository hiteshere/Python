# result = 2+3
# print result

        # Building strings using sub strings
# color = ['hitesh ', 'hiteshs ', 'hunny ']
# result = ''.join(color)
# print result

    # Variation 1
# color = ['hitesh ', 'hiteshs ', 'hunny ']
# print 'start', ','.join(color)
# print 'start', ',', ' '.join(color)
# print 'start', ',', ' '.join(color[:-1]), color[1]
# print 'start', ',', ' '.join(color[:-1]),'or', color[1]
# print result   Here using a variabe ,aking whole linr tonact as a string making undesirabel output

    # Variation 2
# items = []
# items.append('hitesh')
# items.append('hunny')
# items.append('kataria')
# print ''.join(fn(i) for i in items)

    # Using in
# d = {'name':'hitesh','surname':'kataria'}
# for key in d.keys():
#     print key

    # index and item
# items = 'hunny is hunny to'.split()
# print items

    # using enumerae which is an generator for (index, value)
# l = ['zero','one','two']
# e = enumerate(l)
# print e.next()
# print list(enumerate(l))

    # Here we are using %s interpolation of string
# name = 'hitesh'
# brand = 'lenovo'
# print ('hi im %s and im using %s mobile now'%( name , brand))

    # Working with NameSpaces
# from pprint import pprint
#
# def namespace(first):
#     # dict_1 = {'name': 'Hitesh', 'type': 'human'}
#     name = 'hitesh'
#     type = 'human'
#     age = 22
#     # dict_2 = {'age': 22}
#     print ('Hi my Name is %(name)s and im a %(type)s and my age is %(age)i'%locals())
#     print locals()
#
# # calling the funcionn
# namespace('hello')
# pprint(locals())

    # Creating a look up function which is to find the required value
# banana = ("banana", "a yellow fruit")
# orange = ("orange", "a orange fruit")
# apple = ("apple", "a green fruit")
# my_list = [banana, orange, apple]
#
# def lookup():
#     word = raw_input("Word to lookup: ")
#     print ("\n")
#     for fruit in my_list:
#         if fruit[0] == word:
#             print fruit[0], ":", fruit[1], "\n"
#             return
#     print("That word does not exist in the dictionary")
# lookup()

    # Testing out list comprihension
# one = ['hunny','hunny',0]
# two = ['kabu','kubey',0]
# item = { x + y for x in one for y in two if x != 0 and y!=0 }
# print item

    # Using enumerate fowith ondex from 1
# list1 = ['hello','hunny']
# for i in enumerate(list1):
#     # print (i[0]+1, i[1])
#     result = (i[0]+1,i[1])
#     print result

    # Native sort in python
# list1 = ['hello','apple',123,'$','hunny']
# list1.sort()
# print list1
    # here sorted method is used which is better as it is not constrained to list only as sor()
# list1 = ['hello56','apple','$','hunny5']
# # list1.sort(len)
# result = sorted(list1, key=len)
# print result

    # Generator yield method
# def yield_function():
#     yield 1
#     yield 2
#     yield 3
#
# for i in yield_function():
#     print i
#
# test = yield_function()
# print 'next used here'
# a =next(test)
# print next(test)
# print next(test)

    # testing  dict here
# list11 = ['hunny','hitesh','kataria']
    # here we are using defaultdict for adding tuple in dictionary
# from collections import defaultdict
# """ putting tuple in a dictionary"""
# s = [('im', 'hitesh'), ('ur','my fiend')]
#     # adding d to a defaultdict for making it a dict with value from s
# d = defaultdict(list)
# """ here list is a default_factory which is used here for maping the\
#     value whihc cou;d be list ,int etc"""
# for key, value in s:
#     d[key].append(value)
# print sorted(d.items())

# """ putting int value dictionary using defaultdict foem colections"""
# s = 'hiteshhiteshh'
# d = defaultdict(int)
# for k in s:
#     d[k] += 1
# print d
# """ here item() is extracting the tuple or dict()key, value/
#     else it is showing exact code with types and dictionary"""
# print d.items()


    # Try and except is used here
# c = 'uhfkdsjhd'
# for i in c:
#     try:
#         data = open('ddf')
#         print data
#     except:
#         print 'here except'

    # making python to speak
import pyttsx
# engine = pyttsx.init()
# engine.say('Simba chalo ghumi karne')
# engine.say('Simbha simbha simbha simbha')
# engine.say('1 2 3 4 5 6 7 8 9 10 11 12 baba ji ka thullu')
# engine.runAndWait()

    # different usage of pyttsx for dirrerent output
# engine = pyttsx.init()
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate+50)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

# class here:
#     def __index__(self,x=[]):
#         x.append('data')
# print  here.__init__.__defaults__

# Here we are getting arguments from usier as we take in nodejs
# import argparse
#
# parse = argparse.ArgumentParser(description= "here the values")
# parse.add_argument('-i', type=str, help="hre values", required=True)
#
# data = parse.parse_args()
#
# value_given = data.i
# print value_given

# here we are just getting to know address and port lookup
# import socket
#
# print (socket.gethostbyaddr('8.8.8.8'))
# print socket.gethostbyname('www.google.com')

# import socket
#
# host = 'localhost'
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# addr = (host,9898)
# mysock.connect(addr)
# # mysock.bind(addr) bind can be used here too as bind is for
# # local address and connect is for remote connect
#
# try:
#     msg = "hi this is trial base tutprial fuck u hunny"
#     mysock.sendall(msg)
# except socket.errno as e:
#     print "socket error",e
# finally:
#     mysock.close()

# import socket
#
# size = 512
# host = ''
# port = 9898
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
#
# sock.bind((host, port))
# sock.listen(5)
#
# c, addr= sock.accept()
# data = c.recv(size)
# if data:
#     f = open("storage.dat", "+w")
#     print "connection we have is ",addr[0]
#     f.write(addr[0])
#     f.write(":")
#     f.write(data.decode("utf-8"))
#     f.close()
# sock.close()

# import httplib
#
# h = httplib.HTTPConnection("www.infiniteskills.com")
# h.request("GET","/")
# data = h.getresponse()
# print data.status
# print data.getheaders()
# text = data.read()
# print text
# for t in text:
#     print t.decode('utf-8')


# a= 33             reading of memory addres in python using id()
# print a
# print id(a)
# print hex(id(a))

# list1 = [3, 5, 2, 4]          testing murtation using sorted() and .sort()
# print sorted(list1)
# print list1
# print list1.sort()

# list1 = [3,2,4,45,3,3]
# tuple1 = [(3,'hey'),'ao',.2]
# print sorted(tuple1)


# Solving some net puzzle sample in this code fro first initial to be the len and rest to be added in a sum var
# def summation(numbers):
#     sum = 0
#     for n in range(1, numbers[0]+1):
#         sum = sum + numbers[n]
#     return sum
#
# list0 = [2,12,12]
# stdout = summation(list0)
# print stdout

