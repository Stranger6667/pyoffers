# coding: utf-8
from .core import Model, ModelManager


class Goal(Model):
    """
    A Goal for an Offer.
    """
    generic_methods = ('update',)


class GoalManager(ModelManager):
    model = Goal
    name = 'goals'
    generic_methods = (
        'create',
        'update',
        'find_by_id',
        'find_all',
    )
