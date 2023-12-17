import random
import datetime
import uuid

def generate_sap_event_log(num_entries):
    # Customized activities for the Death Star project
    activities = [
        "Strategic Empire Analysis During Death Star Study Phase",
        "Developing Business Case for Death Star Project Proposal",
        "Architecting Intergalactic Superweapon Solution",
        "Planning Major Construction Phase for Orbital Battle Station",
        "Mitigating Risks in Death Star's Troubled Project Areas",
        "Initiating New Galactic Domination Program",
        "Creating Work Breakdown Structure for Superlaser Development",
        "Determining Resource Dependencies Across Star Systems",
        "Sequencing Intergalactic Construction Activities",
        "Scheduling Imperial Fleet Mobilization for Material Transport",
        "Implementing Risk Management for Rebel Incursion Scenarios",
        "Preparing Detailed Activity List for Imperial Engineering Corps"
    ]

    # Resources relevant to the Star Wars universe
    resources = [
        "Darth Vader", "Emperor Palpatine", "Grand Moff Tarkin",
        "Imperial Droid #1", "Imperial Engineer", "Stormtrooper Squad Leader",
        "Imperial Fleet Commander", "TIE Fighter Pilot"
    ]

    # Start date for the project
    start_date = datetime.datetime(3, 1, 1)  # Galactic Standard Calendar

    # Initialize the list for log entries
    log_entries = []

    for _ in range(num_entries):
        # Random date within a specified timeframe
        days_offset = random.randint(0, 364)
        event_date = start_date + datetime.timedelta(days=days_offset)

        # Random activity and resource
        activity = random.choice(activities)
        resource = random.choice(resources)

        # Additional attributes and status information
        additional_attributes = "Location: Unknown sector of the galaxy"
        status_info = random.choice(["Pending", "Completed", "In Progress"])

        # Synthetic SAP log entry
        log_entry = {
            "Case ID": str(uuid.uuid4()),
            "Event ID": str(uuid.uuid4()),
            "Timestamp": event_date.strftime("%Y-%m-%d %H:%M:%S"),
            "Activity": activity,
            "Resource": resource,
            "Additional Attributes": additional_attributes,
            "Status Information": status_info,
            "Data Payload": f"{activity} executed by {resource}. Status: {status_info}."
        }

        log_entries.append(log_entry)

    return log_entries

# Generate 10 synthetic SAP event log entries
synthetic_sap_logs = generate_sap_event_log(3)
print(synthetic_sap_logs)

def generate_material_procurement_log(num_entries):
    # Define materials and suppliers for the Death Star project
    materials = [
        "Durasteel Plating", "Hyperdrive Components", "Turbolaser Cannons",
        "Deflector Shields", "Tractor Beam Projectors", "Kyber Crystals"
    ]
    suppliers = [
        "Kuat Drive Yards", "Sienar Fleet Systems", "Corellian Engineering Corporation",
        "BlasTech Industries", "Arakyd Industries", "Imperial Armory"
    ]

    # Define activities related to material procurement
    activities = [
        "Material Order Placement", "Supplier Contract Negotiation",
        "Delivery Schedule Coordination", "Quality Inspection of Materials",
        "Inventory Management", "Emergency Resupply Request"
    ]

    # Define resources involved in material procurement
    resources = [
        "Imperial Logistics Officer", "Procurement Droid", "Imperial Supply Captain",
        "Quality Control Specialist", "Imperial Quartermaster", "Fleet Supply Officer"
    ]

    # Start date for material procurement activities
    start_date = datetime.datetime(3, 1, 1)  # Galactic Standard Calendar

    # Initialize the list for log entries
    log_entries = []

    for _ in range(num_entries):
        # Random date within a specified timeframe
        days_offset = random.randint(0, 364)
        event_date = start_date + datetime.timedelta(days=days_offset)

        # Random activity, material, supplier, and resource
        activity = random.choice(activities)
        material = random.choice(materials)
        supplier = random.choice(suppliers)
        resource = random.choice(resources)

        # Additional attributes and status information
        additional_attributes = f"Material: {material}, Supplier: {supplier}"
        status_info = random.choice(["Order Placed", "In Transit", "Delivered", "Delayed"])

        # Data payload
        payload = f"{activity} for {material} with {supplier}. Handled by {resource}. Status: {status_info}."

        # Synthetic SAP log entry for material procurement
        log_entry = {
            "Case ID": str(uuid.uuid4()),
            "Event ID": str(uuid.uuid4()),
            "Timestamp": event_date.strftime("%Y-%m-%d %H:%M:%S"),
            "Activity": activity,
            "Resource": resource,
            "Additional Attributes": additional_attributes,
            "Status Information": status_info,
            "Data Payload": payload
        }

        log_entries.append(log_entry)

    return log_entries

# Example usage: generate_material_procurement_log(10) will generate 10 log entries
# Note: Running this function will produce different outputs each time due to the randomization.
synthetic_sap_logs = generate_material_procurement_log(3)
print(synthetic_sap_logs)
