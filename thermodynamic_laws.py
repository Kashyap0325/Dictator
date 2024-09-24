import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Boyle's Law
def boyles_law():
    st.subheader("Boyle's Law: P1 * V1 = P2 * V2")

    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.write("### Theory & Images")
        st.write("""
            **Explanation:**
            Boyle's Law states that for a given mass of gas at constant temperature, the pressure of the gas is inversely proportional to its volume. 
            In other words, when the volume increases, the pressure decreases, and vice versa, as long as the temperature remains constant.
        """)
        # Display practical image
        st.image('https://miro.medium.com/v2/resize:fit:1200/1*bX_xy5gj_Bp9LS3fsvjDvg.jpeg', caption="Practical Example for Boyle's Law", use_column_width=True)

    with col2:
        st.write("### Input Data")
        P1 = st.number_input("Enter initial pressure (P1) in atm:", value=1.0)
        V1 = st.number_input("Enter initial volume (V1) in liters:", value=1.0)
        
        choice = st.selectbox("Do you want to calculate final pressure (P2) or final volume (V2)?", ['Final Pressure (P2)', 'Final Volume (V2)'])
        
        if choice == 'Final Pressure (P2)':
            V2 = st.number_input("Enter final volume (V2) in liters:", value=1.0)
            P2 = (P1 * V1) / V2
            st.markdown(f"<h3 style='text-align: center;'><b>Final pressure (P2) is: {P2:.2f} atm</b></h3>", unsafe_allow_html=True)
            volumes = [V1, V2]
            pressures = [P1, P2]
        else:
            P2 = st.number_input("Enter final pressure (P2) in atm:", value=1.0)
            V2 = (P1 * V1) / P2
            st.markdown(f"<h3 style='text-align: center;'><b>Final volume (V2) is: {V2:.2f} liters</b></h3>", unsafe_allow_html=True)
            volumes = [V1, V2]
            pressures = [P1, P2]

    with col3:
        st.write("### Boyle's Law Chart")
        fig, ax = plt.subplots()
        ax.plot(volumes, pressures, marker='o')
        ax.set_title("Boyle's Law")
        ax.set_xlabel("Volume (liters)")
        ax.set_ylabel("Pressure (atm)")
        ax.grid(True)
        st.pyplot(fig)


# Charles's Law
def charles_law():
    st.subheader("Charles's Law: V1/T1 = V2/T2")

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.write("### Theory & Images")
        st.write("""
            **Explanation:**
            Charles's Law states that the volume of a gas is directly proportional to its temperature, as long as the pressure is constant.
            In other words, if the temperature increases, the volume increases as well, and if the temperature decreases, the volume decreases.
        """)
        # Display practical image
        st.image('https://miro.medium.com/v2/resize:fit:800/1*Tepq6VPx4Wz87w3Jx86qoA.jpeg', caption="Practical Example for Charles's Law", use_column_width=True)

    with col2:
        st.write("### Input Data")
        V1 = st.number_input("Enter initial volume (V1) in liters:", value=1.0)
        T1_C = st.number_input("Enter initial temperature (T1) in °C:", value=0.0)
        T1 = T1_C + 273.15  # Convert Celsius to Kelvin
        
        choice = st.selectbox("Do you want to calculate final volume (V2) or final temperature (T2)?", ['Final Volume (V2)', 'Final Temperature (T2)'])
        
        if choice == 'Final Volume (V2)':
            T2_C = st.number_input("Enter final temperature (T2) in °C:", value=0.0)
            T2 = T2_C + 273.15  # Convert Celsius to Kelvin
            V2 = (V1 * T2) / T1
            st.markdown(f"<h3 style='text-align: center;'><b>Final volume (V2) is: {V2:.2f} liters</b></h3>", unsafe_allow_html=True)
            temperatures = [T1, T2]
            volumes = [V1, V2]
        else:
            V2 = st.number_input("Enter final volume (V2) in liters:", value=1.0)
            T2 = (T1 * V2) / V1
            T2_C = T2 - 273.15  # Convert Kelvin back to Celsius for display
            st.markdown(f"<h3 style='text-align: center;'><b>Final temperature (T2) is: {T2_C:.2f} °C</b></h3>", unsafe_allow_html=True)
            temperatures = [T1, T2]
            volumes = [V1, V2]

    with col3:
        st.write("### Charles's Law Chart")
        fig, ax = plt.subplots()
        ax.plot(temperatures, volumes, marker='o')
        ax.set_title("Charles's Law")
        ax.set_xlabel("Temperature (K)")
        ax.set_ylabel("Volume (liters)")
        ax.grid(True)
        st.pyplot(fig)


# Gay-Lussac's Law
def gay_lussac_law():
    st.subheader("Gay-Lussac's Law: P1/T1 = P2/T2")

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.write("### Theory & Images")
        st.write("""
            **Explanation:**
            Gay-Lussac's Law states that the pressure of a gas is directly proportional to its temperature, provided the volume remains constant. 
            This means that as the temperature increases, the pressure increases, and as the temperature decreases, the pressure decreases.
        """)
        # Display practical image
        st.image('https://www.chemistrylearner.com/wp-content/uploads/2024/03/Gay-Lussacs-Law.jpg', caption="Practical Example for Gay-Lussac's Law", use_column_width=True)

    with col2:
        st.write("### Input Data")
        P1 = st.number_input("Enter initial pressure (P1) in atm:", value=1.0)
        T1_C = st.number_input("Enter initial temperature (T1) in °C:", value=0.0)
        T1 = T1_C + 273.15  # Convert Celsius to Kelvin
        
        choice = st.selectbox("Do you want to calculate final pressure (P2) or final temperature (T2)?", ['Final Pressure (P2)', 'Final Temperature (T2)'])
        
        if choice == 'Final Pressure (P2)':
            T2_C = st.number_input("Enter final temperature (T2) in °C:", value=0.0)
            T2 = T2_C + 273.15  # Convert Celsius to Kelvin
            P2 = (P1 * T2) / T1
            st.markdown(f"<h3 style='text-align: center;'><b>Final pressure (P2) is: {P2:.2f} atm</b></h3>", unsafe_allow_html=True)
            temperatures = [T1, T2]
            pressures = [P1, P2]
        else:
            P2 = st.number_input("Enter final pressure (P2) in atm:", value=1.0)
            T2 = (T1 * P2) / P1
            T2_C = T2 - 273.15  # Convert Kelvin back to Celsius for display
            st.markdown(f"<h3 style='text-align: center;'><b>Final temperature (T2) is: {T2_C:.2f} °C</b></h3>", unsafe_allow_html=True)
            temperatures = [T1, T2]
            pressures = [P1, P2]

    with col3:
        st.write("### Gay-Lussac's Law Chart")
        fig, ax = plt.subplots()
        ax.plot(temperatures, pressures, marker='o')
        ax.set_title("Gay-Lussac's Law")
        ax.set_xlabel("Temperature (K)")
        ax.set_ylabel("Pressure (atm)")
        ax.grid(True)
        st.pyplot(fig)


# Streamlit app layout
st.title("Thermodynamic Laws Simulator")

# Dropdown to select law
law = st.selectbox("Select a thermodynamic law:", ["Boyle's Law", "Charles's Law", "Gay-Lussac's Law"])

# Display corresponding law
if law == "Boyle's Law":
    boyles_law()
elif law == "Charles's Law":
    charles_law()
elif law == "Gay-Lussac's Law":
    gay_lussac_law()
