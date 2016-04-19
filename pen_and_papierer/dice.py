import random

class DiceException(Exception):
    pass


class Dice():
    def __init__(self):
        pass

    def get_dice_roll(self, dice):
        '''

        :param dice:
        :return:
        '''
        if dice == 'd4':
            dice_roll = self.get_random_element(range=range(1,5))
        elif dice == 'd6':
            dice_roll = self.get_random_element(range=range(1,7))
        elif dice == 'd8':
            dice_roll = self.get_random_element(range=range(1,9))
        elif dice == 'd10':
            dice_roll = self.get_random_element(range=range(1,11))
        elif dice == 'd20':
            dice_roll = self.get_random_element(range=range(1,21))
        elif dice == 'd100':
            dice_roll = self.get_random_element(range=range(1,101))

        return dice_roll

    def get_random_element(self, range):
        '''

        :param range:
        :return:
        '''
        return random.choice(range)

if __name__ == '__main__':
    Dice().get_dice_range('d4')