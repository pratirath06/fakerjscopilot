from Docs.person import load_faker_person_docs
from Docs.vehicle import load_faker_vehicle_docs
from Docs.string import load_faker_string_docs
from Docs.lorem import load_faker_lorem_docs
from Docs.number import load_faker_number_docs
from Docs.music import load_faker_music_docs
from Docs.location import load_faker_location_docs
from Docs.internet import load_faker_internet_docs
from Docs.image import load_faker_image_docs
from Docs.helper import load_faker_helper_docs
from Docs.git import load_faker_git_docs
from Docs.food import load_faker_food_docs
from Docs.database import load_faker_database_docs
from Docs.datatype import load_faker_datatype_docs
from Docs.company import load_faker_company_docs
from Docs.color import load_faker_color_docs
from Docs.commerce import load_faker_commerce_docs
from Docs.book import load_faker_book_docs
from Docs.animal import load_faker_animal_docs
from Docs.airline import load_faker_airline_docs
from Docs.system import load_faker_system_docs
from Docs.science import load_faker_science_docs
from Docs.phone import load_faker_phone_docs
def merge_faker_docs():
   docs = {}
   docs.update(load_faker_person_docs())
   docs.update(load_faker_vehicle_docs())
   docs.update(load_faker_string_docs())
   docs.update(load_faker_lorem_docs())
   docs.update(load_faker_number_docs())
   docs.update(load_faker_music_docs())
   docs.update(load_faker_location_docs())
   docs.update(load_faker_internet_docs())
   docs.update(load_faker_image_docs())
   docs.update(load_faker_helper_docs())
   docs.update(load_faker_git_docs())
   docs.update(load_faker_food_docs())
   docs.update(load_faker_database_docs())
   docs.update(load_faker_datatype_docs())
   docs.update(load_faker_company_docs())
   docs.update(load_faker_color_docs())
   docs.update(load_faker_commerce_docs())
   docs.update(load_faker_book_docs())
   docs.update(load_faker_animal_docs())
   docs.update(load_faker_airline_docs())
   docs.update(load_faker_system_docs())
   docs.update(load_faker_science_docs())
   docs.update(load_faker_phone_docs())
   return docs
