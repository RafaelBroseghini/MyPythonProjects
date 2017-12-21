from collections import Counter
class Finals():
    def __init__(self, year, winner, loser, winscore, losescore):
        self._winner = winner
        self._year = year
        self._loser = loser
        self._winscore = winscore
        self._losescore = losescore
    
    @property
    def winner(self):
        return self._winner
    
    @property
    def loser(self):
        return str(self._loser)
    
    @property
    def year(self):
        return self._year
    
    @property
    def winscore(self):
        return self._winscore
    
    @property
    def margin(self):
        return int(self._winscore) - int(self._losescore) 
     
    def __str__(self):
        return 'The ' + self._winner + ' won in ' + self.year + ' against the ' + self._loser + ' by ' + str(self._winscore) + '-' + str(self._losescore)

champions = dict()
champions_mlb = dict()
champions_nfl = dict()
champions_nhl = dict()
all_games = list()
all_games_mlb = list()
all_games_nfl = list()
all_games_nhl = list()
losers = list()
losers_list = list()
more_losers = list()
even_more_losers = list()
print()

with open('nba.txt', 'r') as sport:
    print('Winning NBA teams are: ')
    only_winners = list()
    sport.readline()
    my_team = {}
    for line in sport:
        line_item = line.rstrip().split('\t')
        only_winners.append(line_item[1])
        line_item[2] = line_item[2].split('-')
        b = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
        all_games.append(b)
        champions[b.winner] = champions.get(b.winner, 0) + 1
    new_set = set(only_winners)
    print(', '.join(str(i) for i in new_set))
    print()
    most_successful = Counter(champions).most_common(1)[0]
    print("{} is the most successful team with {} titles.".format(*most_successful))
    print()
    most_successful_str = str(most_successful[0])

with open('nba.txt', 'r') as sport:
    sport.readline()
    my_team = {}
    for line in sport:
        line_item = line.rstrip().split('\t')
        line_item[2] = line_item[2].split('-')
        b = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
        if b.winner in my_team:
            my_team[b.winner].append(b)
        else:
            my_team[b.winner] = [b]
    for i in my_team[most_successful_str]:
        print(str(i))
print()
with open('nba.txt', 'r') as sport:
    only_winners = list()
    sport.readline()
    most = {}
    for line in sport:
        line_item = line.rstrip().split('\t')
        line_item[2] = line_item[2].split('-')
        b = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
        losers.append(b.loser)
    losers_to_count = (i for i in losers if i[:1].isupper())
    a = Counter(losers_to_count)
    print('The {} is the team that has been to the final most times without ever winning: '.format(a.most_common(1)[0][0]))
print()
        
with open('nba.txt', 'r') as sport:
    print('These are years by which a team won by the largest margin: ')
    only_winners = list()
    sport.readline()
    my_margin = {}
    for line in sport:
        line_item = line.rstrip().split('\t')
        line_item[2] = line_item[2].split('-')
        b = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
        my_margin[b.year] = b.margin
    margin_list = sorted(my_margin, key = my_margin.get, reverse = True)
    max = my_margin[margin_list[0]]
    for i in range(len(margin_list)):
        if my_margin[margin_list[i]] == max:
            print(margin_list[i], end = ', ')
    print()
    print()

with open('mlb.txt', 'r') as sport:
    print('Winning MLB teams are: ')
    only_winners = list()
    sport.readline()
    my_team = {}
    for line in sport:
        line_item = line.rstrip().split('\t')
        only_winners.append(line_item[1])
        line_item[2] = line_item[2].split('-')
        c = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
        all_games_mlb.append(c)
        champions_mlb[c.winner] = champions_mlb.get(c.winner, 0) + 1
    new_set = set(only_winners)
    print(', '.join(str(i) for i in new_set))
    print()
    most_successful = Counter(champions_mlb).most_common(1)[0]
    print("{} is the most successful team with {} titles".format(*most_successful))
    print()
    most_successful_str = str(most_successful[0])
    
with open('mlb.txt', 'r') as sport:
    sport.readline()
    my_team = {}
    for line in sport:
        line_item = line.rstrip().split('\t')
        line_item[2] = line_item[2].split('-')
        c = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
        if c.winner in my_team:
            my_team[c.winner].append(c)
        else:
            my_team[c.winner] = [c]
    for i in my_team[most_successful_str]:
        print(str(i))
    print()
    
with open('mlb.txt', 'r') as sport:
        sport.readline()
        most = {}
        for line in sport:
            line_item = line.rstrip().split('\t')
            line_item[2] = line_item[2].split('-')
            c = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
            losers_list.append(c.loser)
        losers_to_count = (i for i in losers_list if i[:1].isupper())
        a = Counter(losers_to_count)
        print('The {} is the team that has been to the final most times without ever winning.'.format(a.most_common(1)[0][0]))
        print()
        
with open('mlb.txt', 'r') as sport:
    print('These are years by which a team won by the largest margin: ')
    only_winners = list()
    sport.readline()
    my_margin = {}
    for line in sport:
        line_item = line.rstrip().split('\t')
        line_item[2] = line_item[2].split('-')
        c = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
        my_margin[c.year] = c.margin
    margin_list = sorted(my_margin, key = my_margin.get, reverse = True)
    max = my_margin[margin_list[0]]
    for i in range(len(margin_list)):
        if my_margin[margin_list[i]] == max:
            print(margin_list[i], end = ', ')
    print()
    print()
with open('nfl.txt', 'r') as sport:
    print('Winning NFL teams are: ')
    only_winners = list()
    sport.readline()
    my_team = {}
    for line in sport:
        line_item = line.rstrip().split('\t')
        only_winners.append(line_item[1])
        line_item[2] = line_item[2].split('-')
        d = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
        all_games_nfl.append(d)
        champions_nfl[d.winner] = champions_nfl.get(d.winner, 0) + 1
    new_set = set(only_winners)
    print(', '.join(str(i) for i in new_set))
    print()
    most_successful = Counter(champions_nfl).most_common(1)[0]
    print("{} is the most successful team with {} titles".format(*most_successful))
    print()
    most_successful_str = str(most_successful[0])
    
with open('nfl.txt', 'r') as sport:
    sport.readline()
    my_team = {}
    for line in sport:
        line_item = line.rstrip().split('\t')
        line_item[2] = line_item[2].split('-')
        d = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
        if d.winner in my_team:
            my_team[d.winner].append(d)
        else:
            my_team[d.winner] = [d]
    for i in my_team[most_successful_str]:
        print(str(i))
    print()
with open('nfl.txt', 'r') as sport:
        sport.readline()
        most = {}
        for line in sport:
            line_item = line.rstrip().split('\t')
            line_item[2] = line_item[2].split('-')
            d = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
            more_losers.append(d.loser)
        losers_to_count = (i for i in more_losers if i[:1].isupper())
        a = Counter(losers_to_count)
        print('The {} is the team that has been to the final most times without ever winning.'.format(a.most_common(1)[0][0]))
        print()
with open('nfl.txt', 'r') as sport:
        print('These are years by which a team won by the largest margin: ')
        only_winners = list()
        sport.readline()
        my_margin = {}
        for line in sport:
            line_item = line.rstrip().split('\t')
            line_item[2] = line_item[2].split('-')
            d = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
            my_margin[d.year] = d.margin
        margin_list = sorted(my_margin, key = my_margin.get, reverse = True)
        max = my_margin[margin_list[0]]
        for i in range(len(margin_list)):
            if my_margin[margin_list[i]] == max:
                print(margin_list[i], end = ' ')
        print()
        print()
    
with open('nhl.txt', 'r') as sport:
    print('Winning NHL teams are: ')
    only_winners = list()
    sport.readline()
    my_team = {}
    for line in sport:
        line_item = line.rstrip().split('\t')
        only_winners.append(line_item[1])
        line_item[2] = line_item[2].split('-')
        e = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
        all_games_nhl.append(e)
        champions_nhl[e.winner] = champions_nhl.get(e.winner, 0) + 1
    new_set = set(only_winners)
    print(', '.join(str(i) for i in new_set))
    print()
    most_successful = Counter(champions_nhl).most_common(1)[0]
    print("The {} is the most successful team with {} titles.".format(*most_successful))
    print()
    most_successful_str = str(most_successful[0])

with open('nhl.txt', 'r') as sport:
    sport.readline()
    my_team = {}
    for line in sport:
        line_item = line.rstrip().split('\t')
        line_item[2] = line_item[2].split('-')
        e = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
        if e.winner in my_team:
            my_team[e.winner].append(e)
        else:
            my_team[e.winner] = [e]
    for i in my_team[most_successful_str]:
        print(str(i))
    print()
        
with open('nhl.txt', 'r') as sport:
        sport.readline()
        most = {}
        for line in sport:
            line_item = line.rstrip().split('\t')
            line_item[2] = line_item[2].split('-')
            e = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
            even_more_losers.append(e.loser)
        losers_to_count = (i for i in even_more_losers if i[:1].isupper())
        a = Counter(losers_to_count)
        print('The {} is the team that has been to the final most times without ever winning.'.format(a.most_common(1)[0][0]))
        print()
        
with open('nhl.txt', 'r') as sport:
        print('These are years by which a team won by the largest margin: ')
        only_winners = list()
        sport.readline()
        my_margin = {}
        for line in sport:
            line_item = line.rstrip().split('\t')
            line_item[2] = line_item[2].split('-')
            e = Finals(line_item[0], line_item[1], line_item[3], line_item[2][0], line_item[2][1])
            my_margin[e.year] = e.margin
        margin_list = sorted(my_margin, key = my_margin.get, reverse = True)
        max = my_margin[margin_list[0]]
        for i in range(len(margin_list)):
            if my_margin[margin_list[i]] == max:
                print(margin_list[i], end = ', ')
        print()
        print()