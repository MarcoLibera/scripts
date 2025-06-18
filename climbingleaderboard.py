# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

def climbingLeaderboard(ranked, player):
    ranked.sort(reverse=True) # Sort in descending order
    ranks = [] # [(score, rank), ...]

    for score in ranked:
        if ranks == []:
            ranks.append((score, 1))
            continue
        if score == ranks[-1][0]:
            continue
        else:
            ranks.append((score, ranks[-1][1] + 1))
    
    print(ranks)
    
    result = []
    for playerScore in player:
        for score, rank in ranks:
            if playerScore == score or playerScore > score:
                result.append(rank)
                print(f"a\tplayerscore: {playerScore}, score: {score}, rank: {rank}")
                break
            # Handle case where player score is less than any ranked score
            elif playerScore < ranks[-1][0]:
                result.append(ranks[-1][1] + 1)
                print(f"c\tplayerscore: {playerScore}, score: {score}, rank: {ranks[-1][1] + 1}")
                break
    return result

ranked = [100, 90, 90, 80]
player = [70, 80, 105]
expectedOutput = [4, 3, 1]

# ranked = [100, 100, 50, 40, 40, 20, 10]
# player = [5, 25, 50, 120]

# ranked = [100, 90, 90, 80, 75, 60]
# player = [50, 65, 77, 90, 102]

print(climbingLeaderboard(ranked, player))
assert(expectedOutput == climbingLeaderboard(ranked, player))
