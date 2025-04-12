import csv

# Define the header row for your CSV
header = ['Venue (Banquet or Lawn)', 'Location', 'Guests Capacity', 'Vendors', 'Budget']

# --- Venue Data (Compiled from Search Results) ---
# Format: [Name, Location, Capacity String, Type (Hotel/Banquet/Lawn/Venue), Vendors (Optional), Budget (Optional)]
# Capacity is stored as found in search results - VERIFY WITH VENUE.
venue_data = [
    ["The St. Regis Mumbai", "Lower Parel, Mumbai", "Up to 1000 (Reception)", "Hotel", "Catering, Decor, DJ", "₹5 Lakhs - ₹15 Lakhs+"],
    ["ITC Maratha, a Luxury Collection Hotel", "Andheri East, Mumbai", "600-1200 (Max)", "Hotel", "Catering, Decor, DJ, Photography", "₹4 Lakhs - ₹12 Lakhs+"],
    ["JW Marriott Mumbai Sahar", "Andheri East, Mumbai", "Up to 3750 (Max)", "Hotel", "Catering, Decor, DJ, Photography, Orchestra", "₹6 Lakhs - ₹20 Lakhs+"],
    ["ITC Grand Central, a Luxury Collection Hotel", "Parel, Mumbai", "Up to 500", "Hotel", "Catering, Decor, DJ", "₹3 Lakhs - ₹10 Lakhs+"],
    ["Taj Mahal Palace Hotel", "Colaba, Mumbai", "Up to 1000+", "Hotel", "Catering, Decor, DJ, Photography", "₹7 Lakhs - ₹25 Lakhs+"],
    ["Grand Hyatt Mumbai", "Santacruz East, Mumbai", "Large Capacity (Verify)", "Hotel", "Catering, Decor, DJ, Photography, Orchestra", "₹5 Lakhs - ₹18 Lakhs+"],
    ["Fairfield by Marriott Mumbai International Airport", "Andheri East, Mumbai", "50-1150", "Hotel", "Catering, Decor, DJ", "₹2 Lakhs - ₹6 Lakhs"],
    ["The Leela Mumbai", "Andheri East, Mumbai", "Large Capacity (Verify)", "Hotel", "Catering, Decor, DJ, Photography", "₹4 Lakhs - ₹15 Lakhs+"],
    ["Sun n Sand Hotel", "Juhu, Mumbai", "20-700", "Hotel", "Catering, Decor, DJ", "₹3 Lakhs - ₹9 Lakhs"],
    ["The Orchid Hotel Mumbai Vile Parle", "Vile Parle East, Mumbai", "70-800", "Hotel", "Catering, Decor, DJ, Photography", "₹2.5 Lakhs - ₹7 Lakhs"],
    ["Kohinoor Continental", "Andheri East, Mumbai", "50-450", "Hotel/Banquet", "Catering, Decor, DJ", "₹1.5 Lakhs - ₹5 Lakhs"],
    ["Goldfinch Hotel", "Andheri East, Mumbai", "100-700 (Overall)", "Hotel/Banquet", "Catering, Decor, DJ", "₹2 Lakhs - ₹6 Lakhs"],
    ["Hotel Sahara Star", "Vile Parle East, Mumbai", "250-400", "Hotel/Banquet", "Catering, Decor, DJ, Photography", "₹3 Lakhs - ₹8 Lakhs"],
    ["Jade Luxury Banquets", "Worli, Mumbai", "150-1000 (Range)", "Banquet/Lawn", "Catering, Decor, DJ", "₹2.5 Lakhs - ₹7 Lakhs"],
    ["The Palace Halls", "Worli, Mumbai", "300-500", "Banquet", "Catering, Decor, DJ", "₹2 Lakhs - ₹6 Lakhs"],
    ["Golden Leaf Banquet", "Malad West, Mumbai", "150-600", "Banquet", "Catering, Decor, DJ", "₹1 Lakh - ₹4 Lakhs"],
    ["Blue Sea Banquets", "Worli, Mumbai", "180-550", "Banquet/Lawn", "Catering, Decor, DJ", "₹2 Lakhs - ₹5.5 Lakhs"],
    ["Royal Halls NSCI", "Worli, Mumbai", "300-800", "Banquet", "Catering, Decor, DJ", "₹2.5 Lakhs - ₹7 Lakhs"],
    ["Breeze Banquets", "Powai, Mumbai", "400-800", "Banquet", "Catering, Decor, DJ", "₹1.8 Lakhs - ₹5 Lakhs"],
    ["GCC Hotel and Club", "Mira Road, Thane (Near Mumbai)", "100-1000+ (Multiple Venues)", "Venue/Hotel/Lawn", "Catering, Decor, DJ, Photography", "₹1.5 Lakhs - ₹6 Lakhs"],
    ["Galaxy Banquet", "Saki Naka, Mumbai", "100-1200 (Range)", "Banquet", "Catering, Decor, DJ", "₹1 Lakh - ₹4 Lakhs"],
    ["Jainam Banquet Hall", "Bhandup West, Mumbai", "500-1500", "Banquet", "Catering, Decor, DJ", "₹1.5 Lakhs - ₹5 Lakhs"],
    ["Anant Royal Banquet", "Kandivali West, Mumbai", "100-1000+", "Banquet/Lawn", "Catering, Decor, DJ", "₹1.2 Lakhs - ₹4.5 Lakhs"],
    ["Kora Kendra Grounds", "Borivali West, Mumbai", "1000+ (Verify)", "Lawn/Ground", "Decor, DJ", "₹80,000 - ₹3 Lakhs"],
    ["Shagun Party Lawn", "Chembur East, Mumbai", "1000+ (Verify)", "Lawn", "Decor, DJ", "₹70,000 - ₹2.5 Lakhs"],
    ["Samarambh Lawns & Banquets", "Owale, Thane West (Near Mumbai)", "1000+ (Verify)", "Lawn/Banquet", "Catering, Decor, DJ", "₹1 Lakh - ₹4 Lakhs"],
    ["The Courtyard", "Owale, Thane West (Near Mumbai)", "80-700", "Venue/Lawn/Banquet", "Catering, Decor, DJ", "₹90,000 - ₹3.5 Lakhs"],
    ["Vows Banquet", "Prabhadevi, Mumbai", "250-500 (Range)", "Banquet/Lawn", "Catering, Decor, DJ", "₹1.8 Lakhs - ₹5 Lakhs"],
    ["Scout Banquet Hall", "Dadar West, Mumbai", "200-600", "Banquet/Lawn", "Catering, Decor, DJ", "₹1.5 Lakhs - ₹4.5 Lakhs"],
    ["The Catholic Gymkhana Limited", "Marine Lines, Mumbai", "300-900", "Venue/Lawn/Banquet", "Catering, Decor, DJ", "₹2 Lakhs - ₹6 Lakhs"],
    ["Kino Cottage", "Versova, Andheri West", "Needs Checking", "Venue", "", ""],
    ["Juhu Club Millennium", "Juhu, Mumbai", "Needs Checking", "Venue", "", ""],
    ["Vivette Banquet", "Malad West, Mumbai", "Needs Checking", "Banquet", "", ""],
    ["Blossoms Lawn", "Andheri East, Mumbai", "Needs Checking", "Lawn", "", ""],
    ["Bayview Lawns", "Mazgaon, Mumbai", "Needs Checking", "Lawn", "", ""],
    ["Chandan Lawns", "Chembur, Mumbai", "Needs Checking", "Lawn", "", ""],
    ["Gawand Lawns", "Thane West", "Needs Checking", "Lawn", "", ""],
    ["Flag's Banquet", "Lokhandwala, Andheri West", "Needs Checking", "Banquet", "", ""],
    ["Malad De Grande - Best Venues", "Malad West", "Needs Checking", "Venue", "", ""],
    ["Legacy Banquets", "Borivali West", "Needs Checking", "Banquet", "", ""],
    ["The Qube Banquet Hall", "Marol, Andheri East", "Needs Checking", "Banquet", "", ""],
    ["Vanita Samaj Hall", "Dadar West, Mumbai", "100-600", "Banquet/Lawn", "Catering, Decor, DJ", "₹1 Lakh - ₹3.5 Lakhs"],
    ["Ashoka Banquet", "Vashi, Mumbai", "100-750", "Banquet", "Catering, Decor, DJ", "₹1 Lakh - ₹4 Lakhs"],
    ["Vidhi Banquets", "Kopar Khairane, Mumbai", "50-900 (Multiple Halls)", "Banquet", "Catering, Decor, DJ", "₹90,000 - ₹3 Lakhs"],
    ["Cava Lounge", "Malad West, Mumbai", "30-200", "Venue/Lounge", "DJ", "₹50,000 - ₹1.5 Lakhs"],
    ["Axis Lawns", "Ghodbunder Road, Owale", "1001-1500 (Verify)", "Lawn", "Decor, DJ", "₹1.2 Lakhs - ₹4 Lakhs"],
    ["Legacy Banquets", "Borivali West", "Needs Checking", "Banquet", "", ""],
    ["The Qube Banquet Hall", "Marol, Andheri East", "Needs Checking", "Banquet", "", ""],
    ["Vanita Samaj Hall", "Dadar West, Mumbai", "100-600", "Banquet/Lawn", "Catering, Decor, DJ", "₹1 Lakh - ₹3.5 Lakhs"],
    ["Ashoka Banquet", "Vashi, Mumbai", "100-750", "Banquet", "Catering, Decor, DJ", "₹1 Lakh - ₹4 Lakhs"],
    ["Vidhi Banquets", "Kopar Khairane, Mumbai", "50-900 (Multiple Halls)", "Banquet", "Catering, Decor, DJ", "₹90,000 - ₹3 Lakhs"],
    ["Cava Lounge", "Malad West, Mumbai", "30-200", "Venue/Lounge", "DJ", "₹50,000 - ₹1.5 Lakhs"],
    ["Axis Lawns", "Ghodbunder Road, Owale", "1001-1500 (Verify)", "Lawn", "Decor, DJ", "₹1.2 Lakhs - ₹4 Lakhs"],
    # Add more venues from the previous list if needed
]

# --- End of Venue Data ---

# --- Navi Mumbai Venue Data ---
navi_mumbai_venues_list = [
    ['The Park Navi Mumbai', 'Navi Mumbai', '60-250'],
    ['Grand Golden Banquet Hall', 'Vashi, Navi Mumbai', '400-1000'],
    ['CIDCO Convention Centre', 'Vashi, Navi Mumbai', '150-8000'],
    ['Siddhivinayak Banquet', 'Navi Mumbai', '50-300'],
    ['Chandan Banquets', 'Sanpada, Navi Mumbai', '100-700'],
    ['Airoli Sports Association', 'Airoli, Navi Mumbai', '150-300'],
    ['Rose Pettals Banquet', 'Sanpada, Navi Mumbai', '300-500'],
    ['Emerald Door', 'Sanpada, Navi Mumbai', '250-400'],
    ['Vidhi Banquets', 'Kopar Khairane, Navi Mumbai', '80-900'],
    ['SRSM Banquet Kharghar', 'Kharghar, Navi Mumbai', '700-1000'],
    ['The Fern Residency, Turbhe', 'Turbhe, Navi Mumbai', '250-1000'],
    ['Hotel Royal Park Residency', 'Airoli, Navi Mumbai', '180-1000'],
    ['Fortune Select Exotica', 'Vashi, Navi Mumbai', '100-1150'],
    ['B.K. Satra Banquets', 'Airoli, Navi Mumbai', '700-1200'],
    ['Ramada, Navi Mumbai', 'Navi Mumbai', '60-500'],
    ['Shree Krupa Banquets', 'Panvel, Navi Mumbai', '150-600'],
    ['Imperial Banquets', 'Vashi, Navi Mumbai', '1000-1200'],
    ['Hotel Royal Tulip', 'Kharghar, Navi Mumbai', '1000-1200'],
    ['Marriott Executive Apartments', 'Navi Mumbai', '80-1000'],
    ['Sai Nandan Banquet Hall', 'Panvel, Navi Mumbai', '50-700'],
    ['Supreme Banquets', 'Navi Mumbai', '100-800'],
    ['Mastiff Grand', 'Navi Mumbai', '100-600'],
    ['Anchaviyo Resort', 'Navi Mumbai', '60-500'],
    ['The Cliff Resort and Spa', 'Navi Mumbai', '112-250'],
    ['The Forest Club Resort', 'Navi Mumbai', '100-300'],
    ['Tropical Retreat', 'Navi Mumbai', '25-1500'],
    ['De Grandeur Hotel', 'Thane', '30-600'], # May need verification
    ['Kalidas Marriage Hall', 'Navi Mumbai', '100-2500'],
    ['Hotel Khandesh Residency', 'Panvel, Navi Mumbai', '200-300'],
    ['Mumbra Wedding Hall', 'Mumbra, Navi Mumbai', '1500-1800'], # May need verification
    ['Shri Balaji Banquet', 'Panvel, Navi Mumbai', '400-1000'],
    ['Hotel Satkar Residency', 'Navi Mumbai', 'Various'],
    ['O2 Banquets', 'Navi Mumbai', 'Various'],
    ['Abbott Hotel', 'Vashi, Navi Mumbai', 'Up to 350'],
    ['The Regenza by Tunga', 'Navi Mumbai', 'Various'],
    ['Emerald Banquets', 'Navi Mumbai', 'Various'],
    ['Four Points by Sheraton', 'Vashi, Navi Mumbai', '50-1000'],
    ['Palm Courtyard Banquet', 'Navi Mumbai', 'Various'],
    ['Club Emerald', 'Navi Mumbai', 'Various'],
    ['The Thane Club', 'Thane', 'Various'], # May need verification
    ['Kumar Resort by TURTLE', 'Navi Mumbai', '80-2000'],
    ['Pushpam Lords Resort', 'Karjat', '60-4500'], # May be outside Navi Mumbai
    ['Seasons Hotel', 'Navi Mumbai', 'Up to 500'],
    ['Sterling Banquet & Lawn', 'Nerul East, Navi Mumbai', 'Up to 1500'],
    ['Centurion Banquet Hall', 'Navi Mumbai', 'Up to 400'],
    ['Mangal Sabhagruh', 'Navi Mumbai', 'Up to 750'],
    ['K Star Hotel', 'Navi Mumbai', 'Up to 400'],
    ['Sutra Banquets', 'Navi Mumbai', 'Up to 300'],
    ['Jat Samaj Hall', 'Navi Mumbai', 'Up to 500'],
    ['Palm Beach Lawn & Banquets', 'Navi Mumbai', 'Up to 1200'],
    ['Occassion Pus Banquet', 'Kharghar, Navi Mumbai', 'Up to 600'],
    ['Bliss Banquet Hall', 'Navi Mumbai', 'Up to 700'],
    ['Hotel Yogi Metropolitan', 'Navi Mumbai', 'Up to 300'],
    ['Celebration Banquets', 'Navi Mumbai', 'Up to 1050'],
    ['Pacific Banquets', 'Kharghar, Navi Mumbai', 'Up to 1000'],
    ['Hotel Yogi Executive', 'Navi Mumbai', 'Up to 450'],
    ['Imperial Banquets', 'Vashi, Navi Mumbai', 'Up to 750'],
    ['The Frontier Banquets', 'Navi Mumbai', 'Up to 200'],
    ['Royal Orchid Central Grazia', 'Navi Mumbai', 'Up to 500'],
    ['Gurav Marriage Hall', 'Vashi, Navi Mumbai', 'Up to 500'],
    ['Shiv Vishnu Mandir', 'Navi Mumbai', 'Up to 1500'],
    ['Sai Heritage Banquets', 'Vashi, Navi Mumbai', 'Up to 800'],
    ['Vista Banquet and Suites', 'Vashi, Navi Mumbai', 'Up to 1000'],
    ['Grand Lotus Banquet Hall', 'Kharghar, Navi Mumbai', 'Up to 500'],
    ['Tithee Banquets', 'Panvel, Navi Mumbai', 'Up to 300'],
    ['Masala Mantra Banquet', 'Kamothe, Navi Mumbai', 'Up to 600'],
    ['Shrusti The Village', 'Panvel, Navi Mumbai', '100-1200'],
    ['Pushp Vatika Resort', 'Panvel, Navi Mumbai', '30-800'],
    ['Alfiya Wedding Hall', 'Mumbra, Navi Mumbai', '350-500'], # May need verification
    ['Green Lawn Hall', 'Mumbra, Navi Mumbai', '400-500'], # May need verification
    ['Royal Garden Lawns & Banquet', 'Panvel, Navi Mumbai', '500-4000'],
    ['S. M. Farm', 'Mumbai', '500-800'], # Verify if in Navi Mumbai
    ['Sudama Event Garden', 'Thane', '800-1000'], # May need verification
    ['Royaleventz', 'Panvel, Navi Mumbai', '250-700'],
    ['Grandiose', 'Navi Mumbai', '500-800'],
    ['Wedding Land', 'Navi Mumbai', '650-1000'],
    ['B K Resort', 'Thane', '1000-3000'], # May need verification
    ['Occassion Plus Banquets', 'Kharghar, Navi Mumbai', 'Various'],
    ['Hotel Country Inn & Suites', 'Navi Mumbai', 'Various'],
    ['V Banquet & Lawn', 'Nerul, Navi Mumbai', 'Various'],
    ['Shri Swami Narayan Banquet Hall', 'Navi Mumbai', 'Various'],
    ['Santoshi Mata Banquet Hall', 'Navi Mumbai', 'Various'],
    ['Talisman Banquets', 'Navi Mumbai', 'Various'],
    ['Jalsa Banquet', 'Navi Mumbai', 'Various'],
    ['Sanai Banquet Hall', 'Navi Mumbai', 'Various'],
    ['Sejj Banquets', 'Navi Mumbai', 'Various'],
    ['Aditi Banquet Hall', 'Navi Mumbai', 'Various'],
    ['Shubh Banquets', 'Navi Mumbai', 'Various'],
    ["Neelam Punjab Banquet's Hall", 'Navi Mumbai', 'Various'],
    ['Hemali Hall', 'Nalasopara', 'Various'], # Likely outside Navi Mumbai
    ['Sr Resort Panvel', 'Panvel, Navi Mumbai', 'Various'],
    ['Sahara Marriage Hall', 'Navi Mumbai', 'Various'],
    ['Pushp Vatika Resort & Lawns', 'Panvel, Navi Mumbai', 'Various'],
    ['The Heritage Banquet Hall and Lawn', 'Navi Mumbai', 'Various'],
    ['Shagun Party Lawn', 'Navi Mumbai', 'Various'],
    ['Kalidas Marriage Hall', 'Navi Mumbai', 'Various'],
    ['Sarovar Farmhouse', 'Mumbai', 'Various'], # Verify if in Navi Mumbai
    ['Mayur Residency', 'Navi Mumbai', 'Various'],
    ['Green Heritage Lawns', 'Navi Mumbai', 'Various'],
    ['Gopal Banquets & Lawns', 'Mumbai', 'Various'], # Likely outside Navi Mumbai
]
# --- End of Navi Mumbai Venue Data ---

# Extend the venue_data list with the navi_mumbai_venues_list
for venue in navi_mumbai_venues_list:
    # Assuming budget based on general knowledge - PLEASE UPDATE THESE MANUALLY
    venue_name, location, capacity = venue
    budget_range = "₹1 Lakh - ₹5 Lakhs" # Default budget - NEEDS MANUAL UPDATE
    if "Hotel" in venue_name or "Resort" in venue_name:
        budget_range = "₹2 Lakhs - ₹8 Lakhs"
    elif "Lawn" in venue_name:
        budget_range = "₹80,000 - ₹3 Lakhs"
    elif "Various" in capacity:
        budget_range = "Needs Verification"

    venue_data.append([venue_name, location, capacity, "Banquet", "Catering, Decor, DJ", budget_range]) # Default vendors and budget

# Define the output CSV filename
filename = 'wedding_venues.csv'

# Write data to the CSV file
try:
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header
        writer.writerow(header)

        # Write the venue data
        for item in venue_data:
            # Now each 'item' in venue_data will have 6 elements
            name, location, capacity, venue_type, vendors, budget = item

            # Format the first column
            if venue_type in ["Banquet", "Lawn"]:
                first_column_value = f"{name} ({venue_type})"
            elif venue_type == "Hotel/Banquet":
                first_column_value = f"{name} (Hotel/Banquet)"
            elif venue_type == "Banquet/Lawn":
                first_column_value = f"{name} (Banquet/Lawn)"
            else: # Hotel, Venue, Ground etc.
                first_column_value = f"{name} ({venue_type})"

            # Create the row: Venue, Location, Capacity, Vendors, Budget
            row = [first_column_value, location, capacity, vendors, budget]
            writer.writerow(row)

    print(f"Successfully created CSV file: {filename}")
    print(f"Populated {len(venue_data)} venues.")
    print("\nPlease verify guest capacities, vendors, and **manually fill in the 'Budget' column with accurate ranges.**")
    print("\nNote: Navi Mumbai venues have been added with a default type of 'Banquet', basic vendor list, and **placeholder budget ranges. Please adjust these if necessary.**")

except Exception as e:
    print(f"An error occurred while writing the CSV: {e}")
