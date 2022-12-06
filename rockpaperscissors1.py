import random
def play():
    user=input('Enter rock(r),scissors(s) or paper(p) :)').lower()
    computer=random.choice(['r','s','p'])
    if user==computer:
        return 'its a tie'
    if is_win(user,computer):
        return 'you won!!'
    return 'you lost!!!'
def is_win(player,opponent):
    #r>S,s>p,p>r
    if (player=='r'and opponent=='s') or (player=='s'and opponent=='p') \
    or (player=='p'and opponent=='r'):
       return True 
print(play())