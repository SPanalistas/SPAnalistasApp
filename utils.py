def get_player_stats(player_name):
    # Simulación de partidos con datos ficticios
    return [
        {
            "player1": player_name,
            "player2": "Jugador Test 1",
            "date": "2025-05-29",
            "tournament": "Roland Garros",
            "surface": "Tierra batida",
            "stats1": {"last5": 4, "win_surface": 75},
            "stats2": {"last5": 2, "win_surface": 40}
        },
        {
            "player1": player_name,
            "player2": "Jugador Test 2",
            "date": "2025-06-01",
            "tournament": "Wimbledon",
            "surface": "Hierba",
            "stats1": {"last5": 3, "win_surface": 60},
            "stats2": {"last5": 4, "win_surface": 55}
        },
        {
            "player1": player_name,
            "player2": "Jugador Test 3",
            "date": "2025-06-10",
            "tournament": "US Open",
            "surface": "Dura",
            "stats1": {"last5": 5, "win_surface": 80},
            "stats2": {"last5": 1, "win_surface": 25}
        }
    ]

def estimate_win_probability(match):
    # Cálculo de probabilidad simple
    p1 = (match['stats1']['last5'] * 0.6 + match['stats1']['win_surface'] * 0.4)
    p2 = (match['stats2']['last5'] * 0.6 + match['stats2']['win_surface'] * 0.4)
    total = p1 + p2
    win_prob_1 = round((p1 / total) * 100, 1)
    win_prob_2 = round((p2 / total) * 100, 1)
    return win_prob_1, win_prob_2