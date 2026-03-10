import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/plan-trip"

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("✈️ AI Travel Planner")
st.caption("Plan flights, hotels, budgets and full itineraries using AI")

st.divider()

# --------------------------------------------------
# TABS
# --------------------------------------------------

tab1, tab2 = st.tabs(["Trip Planner", "AI Travel Chat"])

# --------------------------------------------------
# TRIP PLANNER TAB
# --------------------------------------------------

with tab1:

    if "destination" not in st.session_state:
        st.session_state.destination = ""

    # --------------------------------------------------
    # POPULAR DESTINATIONS
    # --------------------------------------------------

    st.subheader("🌍 Popular Destinations")

    d1, d2, d3, d4, d5 = st.columns(5)

    with d1:
        st.image("https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg", use_container_width=True)
        st.markdown("**Paris**")
        if st.button("Select Paris"):
            st.session_state.destination = "Paris"

    with d2:
        st.image("https://images.pexels.com/photos/2506923/pexels-photo-2506923.jpeg", use_container_width=True)
        st.markdown("**Tokyo**")
        if st.button("Select Tokyo"):
            st.session_state.destination = "Tokyo"

    with d3:
        st.image("https://images.pexels.com/photos/466685/pexels-photo-466685.jpeg", use_container_width=True)
        st.markdown("**New York**")
        if st.button("Select New York"):
            st.session_state.destination = "New York"

    with d4:
        st.image("https://images.pexels.com/photos/823696/pexels-photo-823696.jpeg", use_container_width=True)
        st.markdown("**Dubai**")
        if st.button("Select Dubai"):
            st.session_state.destination = "Dubai"

    with d5:
        st.image("https://images.pexels.com/photos/1797161/pexels-photo-1797161.jpeg", use_container_width=True)
        st.markdown("**Rome**")
        if st.button("Select Rome"):
            st.session_state.destination = "Rome"

    st.divider()

    # --------------------------------------------------
    # TRIP INPUT
    # --------------------------------------------------

    st.subheader("Plan Your Trip")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        origin = st.text_input("Origin")

    with col2:
        destination = st.text_input(
            "Destination",
            value=st.session_state.destination
        )

    with col3:
        travelers = st.number_input("Travelers", min_value=1)

    with col4:
        days = st.number_input("Trip Duration (Days)", min_value=1)

    st.write("")

    if st.button("Generate Trip Plan"):

        payload = {
            "origin": origin,
            "destination": destination,
            "travelers": travelers,
            "days": days
        }

        with st.spinner("AI is planning your trip..."):
            st.write("🔎 Searching flights...")
            st.write("🏨 Finding hotels...")
            st.write("💰 Calculating trip budget...")
            st.write("🧠 Generating itinerary...")

            response = requests.post(API_URL, json=payload)
            result = response.json()

        st.success("Trip generated successfully!")

        st.divider()

        # --------------------------------------------------
        # DESTINATION PREVIEW
        # --------------------------------------------------

        st.subheader(f"Destination Preview: {destination}")

        st.image(
            "https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg",
            use_container_width=True
        )

        st.divider()

        # --------------------------------------------------
        # SUMMARY
        # --------------------------------------------------

        st.subheader("Trip Summary")

        m1, m2, m3, m4 = st.columns(4)

        m1.metric("Travelers", travelers)
        m2.metric("Days", days)
        m3.metric("Flight Cost", result["budget"]["flight_total"])
        m4.metric("Total Budget", result["budget"]["total_trip_cost"])

        st.divider()

        # --------------------------------------------------
        # FLIGHTS
        # --------------------------------------------------

        st.subheader("✈️ Flights")
        st.markdown(result["flight_info"])

        st.divider()

        # --------------------------------------------------
        # HOTELS
        # --------------------------------------------------

        st.subheader("🏨 Hotels")
        st.markdown(result["hotel_info"])

        st.divider()

        # --------------------------------------------------
        # BUDGET
        # --------------------------------------------------

        st.subheader("💰 Budget Breakdown")
        st.json(result["budget"])

        st.divider()

        # --------------------------------------------------
        # ITINERARY
        # --------------------------------------------------

        st.subheader("🗺️ Travel Itinerary")
        st.markdown(result["itinerary"])


# --------------------------------------------------
# CHAT TAB
# --------------------------------------------------

with tab2:

    st.subheader("💬 Travel Assistant")

    user_input = st.text_input(
        "Ask something like: Plan a 5 day trip from Berlin to Rome for 2 people"
    )

    if st.button("Ask Assistant"):
        st.info("Chat assistant integration coming next.")