def get_probabilities(score):
    if score==21:
        return 1
    if score==20:
        return 0.92
    if score==19:
        return 0.85
    if score==18:
        return 0.77
    if score==17:
        return 0.69
    if score==16:
        return 0.62
    if score==15:
        return 0.58
    if score==14:
        return 0.56
    if score==13:
        return 0.39
    if score==12:
        return 0.31
    return 0
def kelly_criterion(p,b):
    return (p*(b+1)-1)/b

if __name__ == "__main__":
    print(kelly_criterion(1-get_probabilities(16),2))