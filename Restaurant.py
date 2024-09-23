import streamlit as st

# Menu dictionary with items and prices
menu = {
    'pizza': 50,
    'pasta': 500,
    'burger': 900,
    'salad': 896,
    'coffee': 822,
}

# Displaying the menu to the user
st.title("Welcome to the Restaurant")
st.subheader("Menu")
for item, price in menu.items():
    st.write(f"{item.capitalize()}: {price}")

# Initializing the total order amount
order_total = 0

# First item order
item_1 = st.text_input('Enter the name of the item you want:').lower()

# Checking if the item exists in the menu
if item_1:
    if item_1 in menu:
        order_total += menu[item_1]
        st.success(f"Your item '{item_1}' has been added.")
    else:
        st.error(f"Order item '{item_1}' is not on the menu.")

# Asking if the user wants to order another item
another_order = st.radio("Do you want to order another item?", ('No', 'Yes'))

# Handling the second item order if the user wants
if another_order == 'Yes':
    item_2 = st.text_input("Enter the name of the second item:").lower()
    if item_2:
        if item_2 in menu:
            order_total += menu[item_2]
            st.success(f"Item '{item_2}' has been added.")
        else:
            st.error(f"Order item '{item_2}' is not available.")

# Displaying the total amount of the order
st.write(f"The total amount of your order is {order_total}.")
