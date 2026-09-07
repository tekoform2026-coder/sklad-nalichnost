import hmac
import streamlit as st

# Настройка на заглавието и оформлението на страницата
st.set_page_config(
    page_title="Складова Наличност",
    page_icon="📦",
    layout="wide"
)

# === СИСТЕМА ЗА ЗАЩИТА С ПАРОЛА ===
def check_password():
    """Връща True, ако потребителят е въвел правилна парола."""
    def password_entered():
        user_pass = str(st.session_state.get("password_input", ""))
        secret_pass = str(st.secrets.get("password", "")) if "password" in st.secrets else ""
        
        if secret_pass and hmac.compare_digest(user_pass, secret_pass):
            st.session_state["password_correct"] = True
            if "password_input" in st.session_state:
                del st.session_state["password_input"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.title("🔒 Вход в системата TEKO")
        st.text_input("🔑 Въведете парола за достъп:", type="password", on_change=password_entered, key="password_input")
        return False
    elif not st.session_state["password_correct"]:
        st.title("🔒 Вход в системата TEKO")
        st.text_input("🔑 Въведете парола за достъп:", type="password", on_change=password_entered, key="password_input")
        st.error("❌ Грешна парола! Опитайте отново.")
        return False
    return True
if not check_password():
    st.stop()
# ==================================

# Заглавие на приложението
st.title("📦 Онлайн Складова Наличност")
st.write("Тук можете да преглеждате и редактирате складовата наличност в реално време. Всички направени промени се запазват автоматично.")

# Точен линк към вашата Google Таблица за вграждане
GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/1qKUg1jWk5BbxI1Rt9JAGGXF8MXYnMX52X5yx2c-xyIw/edit?gid=1779602527&rm=embedded"

# Визуализация на таблицата в уеб страницата
st.components.v1.iframe(GOOGLE_SHEET_URL, height=800, scrolling=True)
