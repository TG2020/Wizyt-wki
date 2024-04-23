from faker import Faker


class BaseContact:
    def __init__(self, first_name, last_name, private_phone, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.private_phone = private_phone
        self.email_address = email_address

    def contact(self):
        return f"Wybieram numer {self.private_phone} i dzwonię do {self.first_name} {self.last_name}."

    @property
    def label_length(self):
        full_name = self.first_name + " " + self.last_name
        return len(full_name)


class BusinessContact(BaseContact):
    def __init__(self, position, company, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.company_phone = company_phone

    def contact(self):
        return f"Wybieram numer {self.company_phone} i dzwonię do {self.first_name} {self.last_name} z firmy  {self.company}."
def create_contacts() -> list[BaseContact]:
    fake = Faker()
    contacts = []
    for _ in range(1):
        private_contact = BaseContact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            private_phone=fake.phone_number(),
            email_address=fake.free_email(),
        )
        contacts.append(private_contact)

        company_contact = BusinessContact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            private_phone=fake.phone_number(),
            email_address=fake.company_email(),
            position=fake.job(),
            company=fake.company(),
            company_phone=fake.phone_number(),
        )
        contacts.append(company_contact)

    return contacts


def main() -> None:
    contacts = create_contacts()

    for contact in contacts:
        print(contact.contact())
        print(f"Imię i nazwisko składa się z {contact.label_length}. liter.")


if __name__ == "__main__":
    main()  