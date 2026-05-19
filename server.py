#!/usr/bin/env python3
"""
Blood Bank Matching System - Python Backend
SDG 3 Hackathon Project

This file handles the server-side logic for blood bank operations.
"""

# ============================================
# BLOOD COMPATIBILITY DATABASE
# ============================================

# Which blood types can receive from which donors
RECIPIENT_COMPATIBILITY = {
    'A+': ['A+', 'A-', 'O+', 'O-'],
    'A-': ['A-', 'O-'],
    'B+': ['B+', 'B-', 'O+', 'O-'],
    'B-': ['B-', 'O-'],
    'O+': ['O+', 'O-'],
    'O-': ['O-'],        # O- can only receive O-
    'AB+': ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'],  # Universal recipient
    'AB-': ['A-', 'B-', 'O-', 'AB-']
}


# ============================================
# BLOOD BANK CLASS
# ============================================

class BloodBank:
    """Main blood bank database class"""
    
    def __init__(self):
        # Initialize with some sample donations
        self.donations = [
            {'id': 1, 'blood_type': 'O-', 'units': 3, 'city': 'New York', 
             'donor': 'John Smith', 'contact': '555-0101', 'status': 'Available'},
            {'id': 2, 'blood_type': 'A+', 'units': 2, 'city': 'New York', 
             'donor': 'Jane Doe', 'contact': '555-0102', 'status': 'Available'},
            {'id': 3, 'blood_type': 'B+', 'units': 1, 'city': 'Los Angeles', 
             'donor': 'Mike Johnson', 'contact': '555-0103', 'status': 'Available'},
            {'id': 4, 'blood_type': 'AB+', 'units': 2, 'city': 'Chicago', 
             'donor': 'Sarah Williams', 'contact': '555-0104', 'status': 'Available'},
            {'id': 5, 'blood_type': 'O+', 'units': 4, 'city': 'Houston', 
             'donor': 'Tom Brown', 'contact': '555-0105', 'status': 'Available'},
        ]
        self.next_id = 6
    
    def add_donation(self, blood_type, units, city, donor, contact):
        """Register a new blood donation"""
        donation = {
            'id': self.next_id,
            'blood_type': blood_type,
            'units': units,
            'city': city,
            'donor': donor,
            'contact': contact,
            'status': 'Available'
        }
        self.donations.append(donation)
        self.next_id += 1
        return donation
    
    def find_matching_blood(self, required_type, units_needed):
        """Find compatible blood for a given blood type"""
        # Get compatible donor types
        compatible_types = RECIPIENT_COMPATIBILITY.get(required_type, [])
        
        # Find available donations
        matches = []
        for donation in self.donations:
            if (donation['status'] == 'Available' and 
                donation['blood_type'] in compatible_types):
                matches.append(donation)
        
        return matches
    
    def allocate_blood(self, matches, units_needed):
        """Mark blood as allocated/matched"""
        allocated = 0
        for donation in matches:
            if allocated < units_needed:
                take = min(donation['units'], units_needed - allocated)
                donation['units'] -= take
                allocated += take
                
                if donation['units'] == 0:
                    donation['status'] = 'Matched'
        
        return allocated
    
    def get_inventory(self):
        """Get all blood donations"""
        return self.donations


# ============================================
# SIMPLE TEST FUNCTIONS
# ============================================

def main():
    """Test the blood bank system"""
    # Create blood bank
    bb = BloodBank()
    
    print("=" * 50)
    print("🩸 BLOOD BANK MATCHING SYSTEM")
    print("=" * 50)
    
    # Test 1: Show current inventory
    print("\n📋 Current Inventory:")
    print("-" * 50)
    for d in bb.get_inventory():
        print(f"ID: {d['id']} | {d['blood_type']} | {d['units']} units | "
              f"{d['city']} | {d['donor']} | {d['status']}")
    
    # Test 2: Register new donor
    print("\n📝 Registering new donor...")
    new_d = bb.add_donation('A-', 2, 'Miami', 'Alice Green', '555-0200')
    print(f"Added: {new_d['donor']} - {new_d['blood_type']}")
    
    # Test 3: Find matching blood for A+ patient
    print("\n🏥 Finding blood for A+ patient...")
    matches = bb.find_matching_blood('A+', 2)
    
    if matches:
        print(f"Found {len(matches)} matching donations:")
        for m in matches:
            print(f"  - {m['blood_type']} from {m['donor']} ({m['units']} units)")
        
        # Allocate blood
        allocated = bb.allocate_blood(matches, 2)
        print(f"Allocated {allocated} units successfully!")
    else:
        print("No matching blood found!")
    
    # Test 4: Show updated inventory
    print("\n📋 Updated Inventory:")
    print("-" * 50)
    for d in bb.get_inventory():
        print(f"ID: {d['id']} | {d['blood_type']} | {d['units']} units | "
              f"{d['status']}")


# Run the program
if __name__ == "__main__":
    main()
