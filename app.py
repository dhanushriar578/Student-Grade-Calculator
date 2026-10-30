import streamlit as st

st.set_page_config(
    page_title="Student Grade Calculator",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Grade Calculator")
st.write("Enter your marks below to calculate your total, percentage, grade, and result.")

st.divider()

student_name = st.text_input("Student Name")

subjects = ["Tamil", "English", "Mathematics", "Science", "Social Science"]
marks = {}

st.subheader("Enter Subject Marks")

for subject in subjects:
    marks[subject] = st.number_input(
        f"{subject} (out of 100)",
        min_value=0,
        max_value=100,
        value=0,
        step=1,
        key=subject
    )

if st.button("Calculate Result", type="primary", use_container_width=True):
    if not student_name.strip():
        st.error("Please enter the student's name.")
    else:
        total = sum(marks.values())
        percentage = total / len(subjects)
        passed = all(mark >= 35 for mark in marks.values())

        if not passed:
            grade = "F"
            result = "FAIL"
        elif percentage >= 90:
            grade = "A+"
            result = "PASS"
        elif percentage >= 80:
            grade = "A"
            result = "PASS"
        elif percentage >= 70:
            grade = "B"
            result = "PASS"
        elif percentage >= 60:
            grade = "C"
            result = "PASS"
        elif percentage >= 50:
            grade = "D"
            result = "PASS"
        else:
            grade = "E"
            result = "PASS"

        st.divider()
        st.subheader("📊 Student Result")
        st.write(f"**Student Name:** {student_name.strip()}")

        col1, col2 = st.columns(2)
        col1.metric("Total Marks", f"{total} / 500")
        col2.metric("Percentage", f"{percentage:.2f}%")

        col3, col4 = st.columns(2)
        col3.metric("Grade", grade)
        col4.metric("Result", result)

        st.subheader("Subject-wise Marks")
        for subject, mark in marks.items():
            status = "Pass" if mark >= 35 else "Fail"
            st.write(f"- **{subject}:** {mark}/100 — {status}")

        if passed:
            st.success(f"Congratulations, {student_name.strip()}! You have passed.")
        else:
            failed_subjects = [subject for subject, mark in marks.items() if mark < 35]
            st.error("You have failed in: " + ", ".join(failed_subjects))

st.divider()
st.caption("Student Grade Calculator | Created using Python and Streamlit")
