import streamlit as st

# Настройка на заглавието и оформлението на страницата
st.set_page_config(
    page_title="Складова Наличност",
    page_icon="📦",
    layout="wide"
)

# Заглавие на приложението
st.title("📦 Онлайн Складова Наличност")
st.write("Тук можете да преглеждате и редактирате складовата наличност в реално време. Всички направени промени се запазват автоматично.")

# Точен линк към вашата Google Таблица за вграждане
GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/1qKUg1jWk5BbxI1Rt9JAGGXF8MXYnMX52X5yx2c-xyIw/edit?gid=1779602527&rm=embedded"

# Визуализация на таблицата в уеб страницата
st.components.v1.iframe(GOOGLE_SHEET_URL, height=800, scrolling=True)
