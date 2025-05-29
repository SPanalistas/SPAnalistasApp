import streamlit as st
from utils import get_player_stats, estimate_win_probability

st.set_page_config(page_title="SP Analistas - Predicciones de Tenis", layout="centered")
st.markdown("## 🎾 SP Analistas - Analiza un partido de tenis")

player_name = st.text_input("🔍 Escribe el nombre del jugador", "")

if player_name:
    st.write(f"Buscando partidos de {player_name}...")
    matches = get_player_stats(player_name)

    if matches:
        for match in matches:
            st.markdown("---")
            st.markdown(f"### {match['player1']} vs {match['player2']}")
            st.markdown(f"🗓️ {match['date']} — 🏟️ {match['tournament']} — 🧱 {match['surface']}")

            win_prob_1, win_prob_2 = estimate_win_probability(match)

            st.progress(win_prob_1 / 100, text=f"{match['player1']}: {win_prob_1:.1f}%")
            st.progress(win_prob_2 / 100, text=f"{match['player2']}: {win_prob_2:.1f}%")

            recommended = match['player1'] if win_prob_1 > win_prob_2 else match['player2']
            st.success(f"✅ Recomendación: Victoria de {recommended}")

    else:
        st.warning("No se encontraron partidos para ese jugador.")