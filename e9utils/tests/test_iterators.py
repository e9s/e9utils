# -*- coding: UTF-8 -*-
import unittest, doctest

from e9utils.iterators import sliding_tuples


class TestIterators(unittest.TestCase):

	def test_sliding_tuples(self):
		testcases = [
			(
				('abc', 1),
				[('a',), ('b',),('c',)]
			),
			(
				('abc', 1, None, False, False),
				[('a',), ('b',),('c',)]
			),
			(
				('abc', 2),
				[(None,'a'),('a','b'),('b','c'),('c',None)]
			),
			(
				('abc', 2, None, True, True),
				[(None,'a'),('a','b'),('b','c'),('c',None)]
			),
			(
				('abc', 2, None, False, False),
				[('a','b'),('b','c')]
			),
			(
				('abc', 2, None, True, False),
				[(None,'a'),('a','b'),('b','c')]
			),
			(
				('abc', 2, None, False, True),
				[('a','b'),('b','c'),('c',None)]
			),
			(
				('abc', 3, None, False, True),
				[('a','b','c'), ('b','c',None),('c',None,None)]
			),
			(
				('abc', 3, None, True),
				[(None,None,'a'), (None,'a','b'), ('a','b','c'), ('b','c',None), ('c',None,None)]
			),
			(
				('abc', 4, None, False, True),
				[('a','b','c',None), ('b','c',None,None),('c',None,None,None)]
			),
			(
				('abc', 4, None, True, True),
				[(None,None,None,'a'), (None,None,'a','b'), (None,'a','b','c'), ('a','b','c',None), ('b','c',None,None),('c',None,None,None)]
			),
			# test fillvalue
			(
				('abc', 2, 'x'),
				[('x','a'), ('a','b'), ('b','c'),('c','x')]
			),
			# test with an iterator
			(
				(range(4), 2),
				[(None,0),(0,1),(1,2),(2,3),(3,None)]
			),
		]
		for (i,e) in testcases:
			self.assertEqual(e, list(sliding_tuples(*i)))



if __name__ == '__main__':
	unittest.main()