import streamlit as st
from utils.gemini import gemini_call
from utils.logo import generate_logo
from utils.prompts import get_market_prompt, get_strategy_prompt, get_tech_stack_prompt

st.set_page_config(page_title="Startup AI Agent", layout="wide")

st.title("🚀 AI Agent for Startup Development")

idea = st.text_area("Describe your startup idea", height=150)

if st.button("Generate Everything"):
    with st.spinner("Doing market research..."):
        market = gemini_call(get_market_prompt(idea))
    with st.spinner("Creating marketing strategy..."):
        strategy = gemini_call(get_strategy_prompt(idea))
    with st.spinner("Designing tech stack..."):
        tech_stack = gemini_call(get_tech_stack_prompt(idea))
    with st.spinner("Generating logo..."):
        logo_img = generate_logo(idea)

    st.subheader("📊 Market Research")
    st.markdown(market)

    st.subheader("🎯 Marketing Strategy")
    st.markdown(strategy)

    st.subheader("💻 Tech Stack")
    st.markdown(tech_stack)

    st.subheader("🎨 Suggested Logo")
    st.image(logo_img, caption="Generated Logo", use_column_width=True)

    st.success("All components generated! 🚀")
