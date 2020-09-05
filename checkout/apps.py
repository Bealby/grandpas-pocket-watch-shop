from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    #Let djange know the is a new signals module with listeners in it
    def ready(self):
        import checkout.signals
