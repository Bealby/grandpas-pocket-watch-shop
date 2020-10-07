from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    # Lets Djange know that there is a new signal module with listeners in it
    def ready(self):
        import checkout.signals
