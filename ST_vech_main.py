import streamlit as st

st.beta_set_page_config(
    page_title="Your App Title",  # Set your app title here
    page_icon=None,  # Remove the Streamlit page icon
    layout="wide",  # Set the layout of your app ("wide" or "centered")
    initial_sidebar_state="expanded"  # Set the initial state of the sidebar ("expanded" or "collapsed")
)

NUM_VEHICLE_TYPES = 5
NUM_SUBTYPES_PER_TYPE = 3

VEHICLE_TYPES = [
    "Car",
    "Truck",
    "Bicycle",
    "Motorcycle",
    "Plane"
]

SUBTYPE_NAMES = [
    ["Sedan", "SUV", "Coupe"],  # Car
    ["Pickup", "Box Truck", "Dump Truck"],  # Truck
    ["Road", "Mountain", "Hybrid"],  # Bicycle
    ["Sport", "Cruiser", "Tour"],  # Motorcycle
    ["Single-Engine", "Jet", "Helicopter"]  # Plane
]

MAINTENANCE_INTERVALS = [
    [16000, 24000, 12000],  # Car
    [32000, 48000, 64000],  # Truck
    [1600, 800, 400],  # Bicycle
    [8000, 16000, 24000],  # Motorcycle
    [160000, 800000, 1600000]  # Plane
]


def calculate_maintenance_status(user_name, vehicle_type, subtype, current_kilometers, last_kilometers):
    if current_kilometers < last_kilometers:
        return "Error: Current kilometers cannot be less than last recorded kilometers."

    kilometers_since_last_maintenance = current_kilometers - last_kilometers

    maintenance_interval = MAINTENANCE_INTERVALS[VEHICLE_TYPES.index(
        vehicle_type)][SUBTYPE_NAMES[VEHICLE_TYPES.index(vehicle_type)].index(subtype)]

    if kilometers_since_last_maintenance >= maintenance_interval:
        return f"Hi {user_name}, based on the maintenance intervals for this type of vehicle, it is time for maintenance."
    else:
        return f"Hi {user_name}, based on the maintenance intervals for this type of vehicle, maintenance is not needed."


def main():
    st.title("Vehicle Maintenance Checker")

    # Input user's name
    user_name = st.text_input("Enter your name:")

    # Input vehicle type
    vehicle_type = st.selectbox("Select the type of vehicle:", VEHICLE_TYPES)

    # Input vehicle subtype
    subtype = st.selectbox(
        f"Select the subtype of {vehicle_type}:", SUBTYPE_NAMES[VEHICLE_TYPES.index(vehicle_type)])

    # Input current and last recorded kilometers
    current_kilometers = st.number_input(
        f"Enter the current kilometers of the {subtype} {vehicle_type}:")
    last_kilometers = st.number_input(
        f"Enter the last recorded kilometers of the {subtype} {vehicle_type}:")

    # Show result on submit
    if st.button("Submit"):
        result = calculate_maintenance_status(
            user_name, vehicle_type, subtype, current_kilometers, last_kilometers)
        st.write(result)


if __name__ == "__main__":
    main()
