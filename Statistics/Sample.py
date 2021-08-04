from random import random


def getSample(data, sample_size):
    random_values = random.sample(data, k=100000)
    return random_values
