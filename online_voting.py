import streamlit as st
import mysql.connector

if "clicked" not in st.session_state:
    st.session_state.clicked = False
if "input1" not in st.session_state:
    st.session_state.input1 = 1 
if "input2" not in st.session_state:
    st.session_state.input2 = ""
if "input3" not in st.session_state:
    st.session_state.input3 = ""
if "input4" not in st.session_state:
    st.session_state.input4 = ""

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="vote"
)
mycursor = mydb.cursor()

admin_menu = {
    1: "Register candidate",
    2: "Register voter",
    3: "View results",
    4: "Exit"
}
def authenticate(user_name,password):
    m


def register_voter(vid, name, address, gender):
    try:
        query = "INSERT INTO voter (vid, name, address, gender) VALUES (%s, %s, %s, %s);"
        values = (vid, name, address, gender)
        mycursor.execute(query, values)
        mydb.commit()
        st.success("Voter registered successfully!")
    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")

def register_candidate(sl_no, name):
    try:
        query = "INSERT INTO candidates (sl_no, name) VALUES (%s, %s);"
        values = (sl_no, name)
        mycursor.execute(query, values)
        mydb.commit()
        st.success("Candidate registered successfully!")
    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")

st.table([{"sl_no": key, "menu": value} for key, value in admin_menu.items()])
opt = st.number_input("Enter the correct option:", min_value=1, max_value=4, step=1)

if st.button("Submit", key="sub1"):
    st.session_state.clicked = True

if st.session_state.clicked:
    if opt == 1:
        st.write("Register candidate")
        st.session_state.input1 = int(st.number_input("Enter candidate ID:", value=st.session_state.input1, key="cand_id"))
        st.session_state.input2 = st.text_input("Enter candidate name:", value=st.session_state.input2, key="cand_name")
        if st.button("Register Candidate", key="register_cand"):
            register_candidate(st.session_state.input1, st.session_state.input2)

    elif opt == 2:
        st.write("Register voter")
        st.session_state.input1 = int(st.text_input("Enter your voter ID:", value=str(st.session_state.input1), key="voter_id"))
        st.session_state.input2 = st.text_input("Enter your name:", value=st.session_state.input2, key="voter_name")
        st.session_state.input3 = st.text_input("Enter your address:", value=st.session_state.input3, key="voter_address")
        st.session_state.input4 = st.text_input("Enter your gender:", value=st.session_state.input4, key="voter_gender")
        if st.button("Register voter", key="register_voter"):
            register_voter(st.session_state.input1, st.session_state.input2, st.session_state.input3, st.session_state.input4)

    elif opt == 3:
        st.write("View results")
        mycursor.execute("SELECT sl_no, name FROM candidates WHERE sl_no IN (SELECT sl_no FROM votes WHERE total_votes=(SELECT MAX(total_votes) FROM votes));")
        for result in mycursor:
            st.header(f"The winner is: {result[1]} with ID {result[0]}")

    elif opt == 4:
        st.write("Exit")
        st.stop()

    else:
        st.error("Invalid option! Please choose a valid menu item.")
