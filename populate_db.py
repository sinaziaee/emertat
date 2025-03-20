from info.models import Person, Contact
from django.core.files import File

info_list = [
    {"first_name": "Rahim", "last_name": "Norikhani", "email": "Rahim.Norikhani@emertatfarabar.com", "role": "Chairman", "img": "profiles/1.jpg"},
    {"first_name": "Omid", "last_name": "Eslami", "email": "Omid.Eslami@emertatfarabar.com", "role": "CEO", "img": "profiles/6.jpg"},
    {"first_name": "Ramin", "last_name": "Eslami", "email": "Ramin.Eslami@emertatfarabar.com", "role": "Account Expert", "img": "profiles/5.jpg"},
    {"first_name": "Makan", "last_name": "Alavi", "email": "Makan.Alavi@emertatfarabar.com", "role": "Operation Manager", "img": "profiles/4.jpg"},
    {"first_name": "Karim", "last_name": "Bayati", "email": "Karim.Bayati@emertatfarabar.com", "role": "Facility Manager", "img": "profiles/2.jpg"},
    {"first_name": "Javad", "last_name": "Eslami", "email": "Javad.Eslami@emertatfarabar.com", "role": "Accountant manager", "img": "profiles/3.jpg"},
    {"first_name": "Negin", "last_name": "Norikhani", "email": "Negin.Norikhani@emertatfarabar.com", "role": "Communications Officer", "img": "profiles/7.jpg"},
    {"first_name": "Niusha", "last_name": "Norikhani", "email": "Niusha.Norikhani@emertatfarabar.com", "role": "Sales and Marketing Executive", "img": "profiles/8.jpg"},
]

for item in info_list:
    person = Person(
        first_name=item["first_name"],
        last_name=item["last_name"],
        email=item["email"],
        phone="",
        role=item["role"],
    )
    # Open the image file and save it to the model's ImageField.
    with open(item["img"], 'rb') as image_file:
        person.img.save(f'{item["first_name"]} {item["last_name"]}.jpg', File(image_file))
    person.save()

# Create and save a new Contact instance.
contact = Contact(
    phone1="+98 992 265 1974",
    phone2="+98 917 361 9345",
    email1="social.emertatfarabar@gmail.com",
    email2="contact@emertatfarabar.com",
    email3="sales@emertatfarabar.com",
    website="https://www.emertatfarabar.com",
    social1="https://www.instagram.com/emertatfarabar/",
    social2="https://www.facebook.com/emertatfarabar/",
    social3="https://www.linkedin.com/company/emertat-farabar/"
)
contact.save()
