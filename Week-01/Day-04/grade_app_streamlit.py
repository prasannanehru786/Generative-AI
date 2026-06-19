import streamlit as st


def calculate_grade(mark):
    """Return grade based on mark."""
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark <= 89:
        return "B"
    elif 70 <= mark <= 79:
        return "C"
    elif 60 <= mark <= 69:
        return "D"
    else:
        return "E"


# Page Configuration
st.set_page_config(
    page_title="Student Grade Calculator",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Grade Calculator")
st.write("Enter a mark between **0 and 100** to find the grade.")

# Input Widget
mark = st.number_input(
    "Enter your mark:",
    min_value=0.0,
    max_value=100.0,
    step=1.0,
    value=None,
    placeholder="Type a mark between 0 and 100"
)

# Button
if st.button("Calculate Grade"):

    if mark is None:
        st.warning("⚠️ Please enter a mark.")
    else:
        grade = calculate_grade(mark)

        st.success("Grade Calculated Successfully!")

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Mark", f"{mark:.0f}")

        with col2:
            st.metric("Grade", grade)

        # Additional message
        if grade == "A":
            st.balloons()
            st.info("🌟 Excellent Performance!")
        elif grade == "B":
            st.info("👍 Very Good!")
        elif grade == "C":
            st.info("🙂 Good Job!")
        elif grade == "D":
            st.info("📚 Keep Practicing!")
        else:
            st.info("💪 Work Hard and Try Again!")