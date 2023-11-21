class OrderConfirmation():
    def __init__(self,takeaway,phone):
        self.takeaway = takeaway
        self.phone = phone

    def send_confirmation(self):
        # Twilio API details in here.
        # Send to self.phone: "Thank you! Your order was placed and will be delivered before 18:52"
        return True