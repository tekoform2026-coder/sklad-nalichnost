import streamlit as st

# Настройка на страницата на пълен екран
st.set_page_config(
    page_title="Складова Наличност", page_icon="📦", layout="wide"
)

st.title("📦 Онлайн Складова Наличност")
st.write(
    "Тук можете да преглеждате и редактирате складовата наличност в реално време."
)

# ⚠️ ЗАМЕНЕТЕ ТАЗИ ВРЪЗКА С ВАШАТА ВРЪЗКА ОТ GOOGLE SHEETS
# Уверете се, че накрая завършва на /edit?rm=embedded
GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/ВАШИЯ_ID_ТУК/edit?rm=embedded"

# Визуализиране на онлайн таблицата вътре в сайта
st.components.v1.iframe(GOOGLE_SHEET_URL, height=750, scrolling=True)
