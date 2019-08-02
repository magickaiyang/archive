import pandas as pd


def build(gps, game_id):
    players = []

    for i in gps.PlayerID.unique():
        counter = 0
        prev_a = 0.0

        for j in range(1, 3):
            for k in gps[(gps.PlayerID == i) & (gps.Half == j)].FrameID.values:  # first half second half
                ax = list(gps[(gps.PlayerID == i) & (gps.FrameID == k) & (gps.Half == j)].AccelX)[0]
                ay = list(gps[(gps.PlayerID == i) & (gps.FrameID == k) & (gps.Half == j)].AccelY)[0]
                az = list(gps[(gps.PlayerID == i) & (gps.FrameID == k) & (gps.Half == j)].AccelZ)[0]
                a = ax ** 2 + ay ** 2 + az ** 2

                if (prev_a > 5.0 and a < 5.0) or (prev_a < 5.0 and a > 5.0):
                    counter += 1
                prev_a = a

        players.append({'GameID': game_id, 'PlayerID': i, 'IntenseEvents': counter})

    return players


if __name__ == '__main__':
    df = pd.read_csv('gps.csv')
    for i in df.GameID.unique():
        if i > 3:
            print('game{0}.csv'.format(i))
            game_df = df[df.GameID == i]
            count_df = pd.DataFrame(build(game_df, i))
            count_df.to_csv('game{0}.csv'.format(i))
