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


# ==================================================
# TRIP PLANNER TAB
# ==================================================

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
        if st.button("Paris"):
            st.session_state.destination = "Paris"

    with d2:
        st.image("https://images.pexels.com/photos/2506923/pexels-photo-2506923.jpeg", use_container_width=True)
        if st.button("Tokyo"):
            st.session_state.destination = "Tokyo"

    with d3:
        st.image("https://images.pexels.com/photos/466685/pexels-photo-466685.jpeg", use_container_width=True)
        if st.button("New York"):
            st.session_state.destination = "New York"

    with d4:
        st.image("https://images.pexels.com/photos/823696/pexels-photo-823696.jpeg", use_container_width=True)
        if st.button("Dubai"):
            st.session_state.destination = "Dubai"

    with d5:
        st.image("https://images.pexels.com/photos/1797161/pexels-photo-1797161.jpeg", use_container_width=True)
        if st.button("Rome"):
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

    # --------------------------------------------------
    # GENERATE TRIP
    # --------------------------------------------------

    if st.button("Generate Trip Plan"):

        payload = {
            "origin": origin,
            "destination": destination,
            "travelers": travelers,
            "days": days
        }

        try:

            with st.spinner("AI is planning your trip..."):

                st.write("🔎 Searching flights...")
                st.write("🏨 Finding hotels...")
                st.write("💰 Calculating trip budget...")
                st.write("🧠 Generating itinerary...")

                response = requests.post(API_URL, json=payload, timeout=120)

                if response.status_code != 200:
                    raise Exception("Backend error")

                result = response.json()

            st.success("Trip generated successfully!")

        except Exception:
            st.error("⚠️ Could not generate trip. Please try again.")
            st.stop()

        st.divider()

        # --------------------------------------------------
        # SUMMARY
        # --------------------------------------------------

        budget = result.get("budget", {})

        st.subheader("Trip Summary")

        m1, m2, m3, m4 = st.columns(4)

        m1.metric("Travelers", travelers)
        m2.metric("Days", days)
        m3.metric("Flight Cost", f"${budget.get('flight_total','N/A')}")
        m4.metric("Total Budget", f"${budget.get('total_trip_cost','N/A')}")

        st.divider()

        # --------------------------------------------------
        # FLIGHTS
        # --------------------------------------------------

        st.subheader("✈️ Flights")
        st.markdown(result.get("flight_info", "No flight data available."))

        st.divider()

        # --------------------------------------------------
        # HOTELS
        # --------------------------------------------------

        st.subheader("🏨 Hotels")
        st.markdown(result.get("hotel_info", "No hotel data available."))

        st.divider()

        # --------------------------------------------------
        # BUDGET
        # --------------------------------------------------

        st.subheader("💰 Budget Breakdown")

        st.markdown(f"""
• ✈️ Flight Cost: **${budget.get("flight_total", "N/A")}**  
• 🏨 Hotel Cost: **${budget.get("hotel_total", "N/A")}**  
• 🚕 Transport: **${budget.get("transport_estimate", "N/A")}**  
• 🎟 Activities: **${budget.get("activities_estimate", "N/A")}**

### 💵 Total Trip Cost: **${budget.get("total_trip_cost", "N/A")}**
""")

        st.divider()

        # --------------------------------------------------
        # ITINERARY
        # --------------------------------------------------

        st.subheader("🗺️ Travel Itinerary")
        st.markdown(result.get("itinerary", "Itinerary could not be generated."))


# ==================================================
# CHAT TAB
# ==================================================

with tab2:

    st.subheader("💬 Travel Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input(
        "Ask something like: Plan a 5 day trip from Berlin to Rome for 2 people"
    )

    if prompt:

        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        assistant_reply = ""

        with st.chat_message("assistant"):

            with st.spinner("🤖 AI is planning your trip..."):

                try:

                    payload = {"query": prompt}

                    response = requests.post(
                        "http://127.0.0.1:8000/chat-plan",
                        json=payload,
                        timeout=120
                    )

                    if response.status_code != 200:
                        raise Exception("Backend error")

                    result = response.json()

                    budget = result.get("budget", {})

                    assistant_reply = f"""
### ✈️ Flights
{result.get("flight_info", "No flight data available.")}

---

### 🏨 Hotels
{result.get("hotel_info", "No hotel data available.")}

---

### 🗺️ Travel Itinerary
{result.get("itinerary", "Itinerary could not be generated.")}
"""

                    st.markdown(assistant_reply)

                    st.divider()
                    st.markdown("### 💰 Budget Breakdown")

                    col1, col2, col3, col4 = st.columns(4)

                    col1.metric("✈️ Flights", f"${budget.get('flight_total','N/A')}")
                    col2.metric("🏨 Hotels", f"${budget.get('hotel_total','N/A')}")
                    col3.metric("🚕 Transport", f"${budget.get('transport_estimate','N/A')}")
                    col4.metric("🎟 Activities", f"${budget.get('activities_estimate','N/A')}")

                    st.metric("💵 Total Trip Cost", f"${budget.get('total_trip_cost','N/A')}")

                except Exception:

                    assistant_reply = "⚠️ Something went wrong while generating the trip. Please try again."
                    st.error(assistant_reply)

        st.session_state.messages.append({
            "role": "assistant",
            "content": assistant_reply
        })