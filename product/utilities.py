import os
from django.template.loader import render_to_string
from django.db.models import Q
from .models import Product
from django.core.mail import EmailMultiAlternatives
from dotenv import load_dotenv

load_dotenv()


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


def notify_admin(subject, products):
    """
    Task that notifies admin about expired products.
    """
    html_content = render_to_string(
        "email/email_expired_products.html", {"products": products}
    )
    body = "List of expiring products"
    sender = os.environ.get("EMAIL_HOST_USER")
    receivers = [os.environ.get("EMAIL_HOST_USER")]
    try:
        messsage = EmailMultiAlternatives(
            subject, body, sender, receivers
        )
        messsage.attach_alternative(html_content, 'text/html')
        messsage.send()
        return True
    except Exception as e:
        return False
