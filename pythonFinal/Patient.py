class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number,
                 emergency_contact_name, emergency_contact_phone):
        # Initialize a Patient instance with the provided data.

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone

    def get_full_name(self):
        # Get the full name of the patient.

        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def get_address(self):
        # Get the formatted address of the patient.

        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"

    def get_phone_number(self):
        # Get the phone number of the patient.

        return self.phone_number

    def get_emergency_contact(self):
        # Get the formatted emergency contact information.

        return f"{self.emergency_contact_name} - {self.emergency_contact_phone}"


class Procedure:
    def __init__(self, procedure_name, procedure_date, practitioner_name, procedure_charge):
        # Initialize a Procedure instance with the provided data.

        self.procedure_name = procedure_name
        self.procedure_date = procedure_date
        self.practitioner_name = practitioner_name
        self.procedure_charge = procedure_charge

    def get_procedure_info(self):
        # Get the information about the medical procedure in a formatted way.

        return f"Name: {self.procedure_name}\nDate: {self.procedure_date}\nPractitioner: {self.practitioner_name}\nCharge: ${self.procedure_charge}"


def main():
    # Create an instance of the Patient class with sample data
    patient = Patient("Dilek", "Ozge", "Yilmaz", "333 Merkez Cad.", "Istanbul", "Turkiye", "34840", "050505",
                      "Ozgur Yilmaz", "050404")

    # Create three instances of the Procedure class with sample data
    procedures = [
        Procedure("Physical Exam", "2024-01-05", "Dr. Irvine", 250.00),
        Procedure("X-ray", "2024-01-05", "Dr. Jamison", 500.00),
        Procedure("Blood test", "2024-01-05", "Dr. Smith", 200.00)
    ]

    # Display patient information
    print("Patient Information:")
    print("Name:", patient.get_full_name())
    print("Address:", patient.get_address())
    print("Phone Number:", patient.get_phone_number())
    print("Emergency Contact:", patient.get_emergency_contact())
    print()

    # Display information about the procedures
    print("Procedure Information:")
    for i, procedure in enumerate(procedures, start=1):
        print(f"Procedure {i}:\n{procedure.get_procedure_info()}\n")

    # Display total charges of the procedures
    total_charges = sum(procedure.procedure_charge for procedure in procedures)
    print("Total Charges for the Procedures: $", total_charges)


if __name__ == "__main__":
    main()

