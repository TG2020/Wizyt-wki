from faker import Faker

fake = Faker('pl_PL')


class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    @property
    def label_length(self):
        return len(self.first_name + self.last_name)

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}")


class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone, email, job, company, business_phone):
        super().__init__(first_name, last_name, phone, email)
        self.job = job
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        print(f"Wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name} z firmy {self.company}")


def create_contacts(contact_type, quantity):
    contacts = []
    for _ in range(quantity):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone = fake.phone_number()
        email = fake.email()
        job = fake.job()
        company = fake.company()
        business_phone = fake.phone_number()

        if contact_type == "base":
            contact = BaseContact(first_name, last_name, phone, email)
        else:
            contact = BusinessContact(first_name, last_name, phone, email, job, company, business_phone)

        contacts.append(contact)

    return contacts


if __name__ == '__main__':
    base_contacts = create_contacts("base", 5)
    for contact in base_contacts:
        contact.contact()

    business_contacts = create_contacts("business", 5)
    for contact in business_contacts:
        contact.contact()