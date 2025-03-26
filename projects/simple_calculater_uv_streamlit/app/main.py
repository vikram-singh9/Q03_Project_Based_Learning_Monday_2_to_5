import streamlit as st

def main():
    st.title("Simple Calculater")
    st.write("Enter two numbers and select the operation!!!")

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter Number one: ", value= 0)
    
    with col2:
        num2 = st.number_input("Enter Number two: ", value=0)


    operation = st.selectbox("select operation", ["Add", "Substract", "Multiply", "Division", "Square", "Remainder"])

    if st.button("Calculate"):
        try:
            if operation == "Add":
                sum = num1 + num2
                st.success(sum)
            elif operation == "Substract":
                sub = num1 - num2
                st.success(sub)
            elif operation == "Multiply":
                mul = num1 * num2
                st.success(mul)
            elif operation == "Division":
                div = num1 / num2
                st.success(div)
                if num1 == 0:
                    st.error("Divided by zero")
            elif operation == "Square":
                sq = num1 ** num2
                st.success(sq)
            elif operation == "Remainder":
                re = num1 % num2
                st.success(re)
        except Exception as e:
            st.success(f"an error ocurred {e}")





if __name__ == "__main__":
    main()