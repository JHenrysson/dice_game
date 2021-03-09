import random


class AI():
    """computer player class. """

    def __init__(self):
        def.AI_score = 0
        def.list_AI_score = [0]

    def get_AI_score(self):
        return self.AI_score

    def set_AI_score(self, score):
        self.AI_score += score

    def add_score_list(self, score):
        self.list_AI_score.append(score)

    def get_last_score(self):
        return self.list_AI_score[-1]

    def get_total_score(self):
        return self.sum(list_AI_score)

    def easy_difficulty(self):
    while get_total_score < 100:
        rolled = random.randint(1, 6)
        print('  Rolled %i' % rolled))
           if rolled == 1:
               print('Oop I roll 1, I loose %i this round, my score now is %i' %(get_AI_score, get_last_score))
               set_AI_score(get_AI_score * -1)
               break
            else:
                set_AI_score(rolled)
        if 15 <= get_AI_score <= 20:
            add_score_list(get_AI_score)
            print(f'I\'ll hold and retain my {get_last_score} from this round')
            break


    def hard_difficulty(self):
    while get_total_score < 100:
        automatic_decision = should_roll(get_AI_score, get_total_score, player1_total)
        if automatic_decision :
            rolled = random.randint(1,6)
           print('  Rolled %i' % rolled))
           if rolled == 1:
               print('Oop I roll 1, I loose %i this round, my score now is %i' %(get_AI_score, get_last_score))
               set_AI_score(get_AI_score * -1)
               break
            else:
                set_AI_score(rolled)
        else:
            add_score_list(get_AI_score)
            print(f'I\'ll hold and retain my {get_last_score} from this round')
            break


    def should_roll(accumulated_score, AI_score, player_score)
        AILead = AI_score - player_score
        if player_score + AI_score >= 100:
            return False
        elif player_score >= 80 and AI_score < 80:
            if accumulated_score <= 30:
                return True
            else:
                return False
        elif AI_score >= 80 and (0 < AILead and AILead <= 10):
            if accumulated_score <= 15:
                return True
            else:
                return False
        else:
            if accumulated_score <= 20:
                return True
            else:
                return False
        





