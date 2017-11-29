import copy
import unittest
from mongoengine.errors import ValidationError

from user.models import User
from tests import MongoTestCase


class UserModelTestCase(MongoTestCase):
    
    def setUp(self):
        super(UserModelTestCase, self).setUp()
        self.user_params = {
            'username': 'user1',
            'password': 'pass1',
            'email': 'user1@test.com',
            'first_name': 'User',
            'last_name': 'One',
            'bio': 'I am a user of this system!'
        }
        
        self.required_params = ['username', 'password', 'email']
        self.optional_params = self.user_params.keys() - self.required_params
        self.unique_params = ['username', 'email']
    
    def test_create_with_all_params_succeeds(self):
        user = User(**self.user_params)
        self.assertIsNone(user.id)
        user.save()
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created)
    
    def test_create_missing_optional_params_succeeds(self):
        for param in self.optional_params:
            user_params = copy.deepcopy(self.user_params)
            user_params.pop(param)
            user = User(**user_params)
            self.assertIsNone(user.id)
            user.save()
            self.assertIsNotNone(user.id)
            user.delete()
    
    def test_create_without_required_params_fails(self):
        for param in self.required_params:
            user_params = copy.deepcopy(self.user_params)
            user_params.pop(param)
            user = User(**user_params)
            with self.assertRaises(ValidationError) as err:
                user.save()
            err = err.exception.to_dict()
            self.assertTrue(param in err.keys())

    def test_create_without_unique_username(self):
        user = User(**self.user_params)
        user.save()
        other_user_params = copy.deepcopy(self.user_params)
        #unique email, same username
        other_user_params['email'] = 'different@email.com'
        other_user = User(other_user_params)
        with self.assertRaises(ValidationError) as err:
            other_user.save()
        err = err.exception.to_dict()
        self.assertTrue('username' in err.keys())
    
    def test_create_without_unique_email(self):
        user = User(**self.user_params)
        user.save()
        self.assertIsNotNone(user.id)
        other_user_params = copy.deepcopy(self.user_params)
        #unique username, same email
        other_user_params['username'] = 'differentUsername'
        other_user = User(other_user_params)
        with self.assertRaises(ValidationError) as err:
            other_user.save()
        err = err.exception.to_dict()
        self.assertTrue('email' in err.keys())
        
    def test_over_max_length_fails(self):
        for param, max_length in [('first_name', 75), ('last_name', 50), ('bio', 50)]:
            user_params = copy.deepcopy(self.user_params)
            user_params[param] = "x"*(max_length+1)
            user = User(**user_params)
            with self.assertRaises(ValidationError) as err:
                user.save()
            err = err.exception.to_dict()
            self.assertTrue(param in err.keys())
