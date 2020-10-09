"""Classes for melon orders."""

class AbstractMelonOrder():

    def __init__(self, species, quantity):

        self.species = species
        self.quantity = quantity
        self.shipped = False
        
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        
        if self.species == "Christmas Melon":
            base_price = base_price * 1.5
 
        if self.order_type == 'International' and self.quantity < 10:
            base_price = base_price + 3
            
        total = (1 + self.tax) * self.quantity * base_price

        return total
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, quantity):
        super().__init__(species, quantity)

        self.order_type = 'Domestic'
        self.tax = 0.05


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, quantity, country_code):
        super().__init__(species, quantity)

        self.order_type = 'International'
        self.tax = 0.17
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code





    