import factory
from faker import Faker
from myapp.models import Product  # Adjust the import to your project's structure

fake = Faker()

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.LazyAttribute(lambda x: fake.word())
    description = factory.LazyAttribute(lambda x: fake.text())
    price = factory.LazyAttribute(lambda x: round(fake.pyfloat(left_digits=2, right_digits=2, positive=True), 2))
    stock = factory.LazyAttribute(lambda x: fake.random_int(min=0, max=100))

# Example usage:
if __name__ == "__main__":
    # Generate a single fake product
    product = ProductFactory()
    print(product.name, product.description, product.price, product.stock)

    # Generate a list of fake products
    products = ProductFactory.create_batch(10)
    for product in products:
        print(product.name, product.description, product.price, product.stock)
