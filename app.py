import streamlit as st

GF_NAME = "Selene"
MY_NAME = "Aditya"

st.set_page_config(page_title=f"For {GF_NAME}", page_icon="🌙", layout="centered")

# ---------- state ----------
if "page" not in st.session_state:
    st.session_state.page = 1
if "asked" not in st.session_state:
    st.session_state.asked = False


def go(page):
    st.session_state.page = page
    st.session_state.asked = False


def ask():
    st.session_state.asked = True


# ---------- style ----------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Nunito:wght@400;600&display=swap');

#MainMenu, header, footer {visibility: hidden;}

.stApp {
    background:
        radial-gradient(1.5px 1.5px at 12% 18%, #fff 50%, transparent 52%),
        radial-gradient(1px 1px at 78% 12%, #fff 50%, transparent 52%),
        radial-gradient(1.5px 1.5px at 88% 46%, #fff 50%, transparent 52%),
        radial-gradient(1px 1px at 22% 62%, #fff 50%, transparent 52%),
        radial-gradient(1.5px 1.5px at 64% 80%, #fff 50%, transparent 52%),
        radial-gradient(1px 1px at 8% 90%, #fff 50%, transparent 52%),
        linear-gradient(180deg, #17122b 0%, #241b45 100%);
    background-attachment: fixed;
}

.block-container {max-width: 640px; padding-top: 3rem; padding-bottom: 4rem;}

.moon {
    width: 96px; height: 96px; border-radius: 50%; margin: 0 auto 1.6rem auto;
    background: radial-gradient(circle at 35% 32%, #fffdf6 0%, #e4dff3 60%, #c9c2e4 100%);
    box-shadow: 0 0 70px rgba(233, 228, 245, 0.45);
}

.big {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-weight: 600; font-size: 3.4rem; line-height: 1.1;
    color: #f4efff; text-align: center; margin: 0 0 0.3rem 0;
}
.sub {
    font-family: 'Nunito', sans-serif; font-size: 1.1rem;
    color: #e8a0b8; text-align: center; margin-bottom: 2.2rem;
}

.line {
    font-family: 'Nunito', sans-serif; font-size: 1.15rem; line-height: 1.75;
    color: #e9e4f5; margin: 0 0 1.15rem 0;
}
.center {text-align: center;}
.strong {color: #fff; font-weight: 600;}
.sign {
    font-family: 'Cormorant Garamond', Georgia, serif; font-size: 1.5rem;
    color: #e8a0b8; text-align: right; margin-top: 1.5rem;
}
.answer {
    font-family: 'Cormorant Garamond', Georgia, serif; font-size: 1.7rem;
    color: #f4efff; text-align: center; margin-top: 1.5rem; line-height: 1.4;
}

.stButton {text-align: center;}
.stButton > button {
    background: #e8a0b8; color: #2a1d3d; border: none; border-radius: 999px;
    padding: 0.65rem 2rem; font-family: 'Nunito', sans-serif; font-weight: 600;
    font-size: 1.05rem; margin-top: 0.8rem;
}
.stButton > button p {color: #2a1d3d;}
.stButton > button:hover, .stButton > button:focus {
    background: #f2b6c9; color: #2a1d3d; border: none;
}
.stButton > button:focus-visible {outline: 2px solid #f4efff; outline-offset: 3px;}
</style>
""",
    unsafe_allow_html=True,
)


def lines(items, css="line"):
    return "".join(f'<p class="{css}">{t}</p>' for t in items)


# ---------- page 1 : romantic ----------
def page_one():
    st.markdown(
        f"""
<div class="moon"></div>
<p class="big">{GF_NAME}</p>
<p class="sub">my moon, my love</p>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        lines(
            [
                "Your name is moon, and for me you are really my moon.",
                "In my dark days, you come and everything become bright.",
                "When you smile, my whole day become good.",
                "I can look at you for hours and I never get bored.",
                "With you, I feel like I have everything in this world.",
                "Even when we fight, I only think about you.",
                '<span class="strong">You are my home, Selene.</span>',
            ],
            "line center",
        ),
        unsafe_allow_html=True,
    )

    st.button("Next 🌙", on_click=go, args=(2,), key="next")


# ---------- page 2 : apology ----------
def page_two():
    st.markdown(
        f"""
<p class="big" style="text-align:left; font-size:2.6rem;">I am sorry, {GF_NAME}</p>
<p class="sub" style="text-align:left; margin-bottom:1.8rem;">I know I hurt you.</p>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        lines(
            [
                '<span class="strong">I was a jerk. I know it.</span>',
                "I said things which I should never say to you. "
                "Those words was wrong, and I cannot take them back.",
                "I feel very very guilty. Every time I think about it, "
                "my heart become heavy.",
                "I was angry, but angry is not a reason to hurt the person "
                "I love the most.",
                "You don't deserve this. You deserve someone who respect you "
                "and talk to you with love.",
                "I want to be that person. I will think before I speak, "
                "and I will listen to you more.",
                "I am not asking you to forget it. I only ask you for one "
                "more chance to make it right.",
                '<span class="strong">I love you, Selene. '
                "I am really, really sorry.</span>",
            ]
        )
        + f'<p class="sign">{MY_NAME}</p>',
        unsafe_allow_html=True,
    )

    if not st.session_state.asked:
        st.button(f"{GF_NAME}, will you forgive me?", on_click=ask, key="ask")
    else:
        st.markdown(
            """
<p class="answer">Thank you for reading this.<br>
I will wait for you, as long as you need. 🌙</p>
""",
            unsafe_allow_html=True,
        )

    st.button("← Back", on_click=go, args=(1,), key="back")


# ---------- router ----------
if st.session_state.page == 1:
    page_one()
else:
    page_two()
