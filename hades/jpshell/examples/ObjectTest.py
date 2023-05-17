#import sys
import java.lang

class MyObject (java.lang.Object):

	def __init__(self):
		print "hello, here i am ..."


#obj = MyObject()
#obj_java_class = obj.getClass()
#obj_python_class = obj.__class__
#print "this is my 'java' class:", obj_java_class
#print "and this is my 'python' class:", obj_python_class
#
#try:
#  tmp = obj_java_class.newInstance()
#except:
#  print "here are the exception:\n", sys.exc_type, sys.exc_value
