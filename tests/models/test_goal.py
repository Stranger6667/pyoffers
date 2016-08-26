# coding: utf-8
from pyoffers.models import Goal


CASSETTE_NAME = 'goal'


def test_create_success(goal):
    assert isinstance(goal, Goal)
    assert goal['description'] == 'String'


def test_get_by_id_success(api, goal):
    instance = api.goals.find_by_id(goal['id'])
    assert isinstance(instance, Goal)
    assert instance['description'] == goal['description']


def test_get_by_id_fail(api):
    assert api.goals.find_by_id(1000) is None


def test_update_success(goal):
    goal['description'] = 'Another'
    new_instance = goal.update()
    assert new_instance['description'] == 'Another'
    assert new_instance == goal
