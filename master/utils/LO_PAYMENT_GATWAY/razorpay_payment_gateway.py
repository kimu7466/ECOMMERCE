from django.conf import settings
import razorpay

razorpay_client = razorpay.Client(
    auth=('rzp_test_mURR0ARMkJjisn', 'RjWpOCol6z8wykWHat6DA4EY'))