import streamlit as st
import os

def calculate(gradeType, num1, num2, num3, num4, weight1, weight2, weight3, weight4):
    num1 = float(num1)
    num2 = float(num2)
    num3 = float(num3)
    num4 = float(num4)
    weight1 = float(weight1)
    weight2 = float(weight2)
    weight3 = float(weight3)
    weight4 = float(weight4)

    if gradeType == "Number Grade":
        final = num1 * weight1 + num2 * weight2 + num3 * weight3 + num4 * weight4
    elif gradeType == "Letter Grade":
        grade = num1 * weight1 + num2 * weight2 + num3 * weight3 + num4 * weight4
        total_weight = weight1 + weight2 + weight3 + weight4
        final = grade / total_weight

        if final >= 90:
            final = "A"
            st.image("images/A.png", use_column_width=True)
        elif final >= 80:
            final = "B"
            st.image("images/B.png", use_column_width=True)
        elif final >= 70:
            final = "C"
            st.image("images/C.png", use_column_width=True)
        else:
            final = "F"
            st.image("images/F.png", use_column_width=True)
    return final

st.title("Grade Calculator") #NEW
st.write("---")

num1 = st.text_input(label="Grade (%)", key="1")
weight1 = st.text_input(label="Weight (decimal)", key="2")
num2 = st.text_input(label="Grade (%)", key="3")
weight2 = st.text_input(label="Weight (decimal)", key="4")
num3 = st.text_input(label="Grade (%)", key="5")
weight3 = st.text_input(label="Weight (decimal)", key="6")
num4 = st.text_input(label="Grade (%)", key="7")
weight4 = st.text_input(label="Weight (decimal)", key="8")

gradeType = st.radio("What type of grade do you want?", ("Number Grade", "Letter Grade"))

if st.button("Calculate Grade"): #NEW
    result = calculate(gradeType, num1, num2, num3, num4, weight1, weight2, weight3, weight4)
    st.success(f"Answer = {result}") #NEW
