import os

from django.db.models import Q
from .models import Product
from django.core.mail import EmailMultiAlternatives


def search_products(query):
    """Return a list of products that match the specified query.

        Args:
            query (str): The search query.

        Returns:
            QuerySet: A filtered queryset of Product objects that match the search query.
        """

    products = Product.objects.filter(
        Q(Name__icontains=query) |
        Q(Manufacturer__icontains=query)
    ).distinct()
    return products


def send_email():
    subject = "Expired Products"
    body = "list"  # list products about to expire here
    sender = os.environ.get("EMAIL_HOST_USER")
    receivers = [os.environ.get("EMAIL_HOST_USER")]
    try:
        messsage = EmailMultiAlternatives(
            subject, body, sender, receivers
        )
        messsage.attach_alternative(body, 'text/html')
        messsage.send()
        return True
    except Exception as e:
        return False
