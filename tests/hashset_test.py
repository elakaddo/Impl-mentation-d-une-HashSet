import unittest, sys
from hamcrest import *
sys.path.append("samples/")
from hashset import HashSet


class HashSetTest(unittest.TestCase) :
    def test_hashCode(self):
        my_hash_set = HashSet()
        assert_that(False, equal_to(my_hash_set.hashCode('')))
        assert_that(5, equal_to(my_hash_set.hashCode(' ')))
        assert_that(24, equal_to(my_hash_set.hashCode('Mohamed')))
        assert_that(20, equal_to(my_hash_set.hashCode('Magali')))
    
    def test_add(self) : 
        my_hash_set = HashSet()
        assert_that(24, equal_to(my_hash_set.add("Mohamed")))
    
    def test_get(self) : 
        my_hash_set = HashSet()
        my_hash_set.add("Mohamed")
        assert_that("Mohamed", equal_to(my_hash_set.get(24)))
        
        assert_that(False, equal_to(my_hash_set.get(100)))
        assert_that(False, equal_to(my_hash_set.get(-1)))
        assert_that(False, equal_to(my_hash_set.get("Hello")))
    
    def test_collision(self):
        my_hash_set = HashSet()
        my_hash_set.add("Mohamed")
        assert_that(False, equal_to(my_hash_set.add("Magali")))

        assert_that("Mohamed", equal_to(my_hash_set.get(23)))


