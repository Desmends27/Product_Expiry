"""
This file is used to create tasks for the userprofiles app using Celery.
"""


from celery import shared_task
from django.template.loader import render_to_string

from apps.notifications.utilities import send_email


@shared_task
def notify_user_upon_account_creation(username, receiver):
    """
    Task that notifies user when an account is created.
    """
    subject = "Your account has been created"
    html_content = render_to_string(
        "email/create_user_notification.html", {"username": username}
    )
    receivers = [receiver]

    # Send email to user
    send_email(subject, html_content, receivers)

    return f"Sent notifications to {username} for creating account"


@shared_task
def notify_account_unfollowed(
        current_user_name,
        user_to_unfollow_email,
        user_to_unfollow_name
):
    """
    Task that notifies the account that was unfollowed.
    """
    subject = "You lost a follower"
    html_content = render_to_string(
        "email/unfollow_notification.html",
        {"current_user_name": current_user_name, "user_to_unfollow_name": user_to_unfollow_name}
    )
    receivers = [user_to_unfollow_email]

    # Send email to user
    send_email(subject, html_content, receivers)

    return f"Sent notifications to {user_to_unfollow_name} for being unfollowed by {current_user_name}"


@shared_task
def notify_account_the_current_user_followed(
        current_user_name,
        user_to_follow_name,
        user_to_follow_email
):
    """
    Task that notifies user when someone follows user.
    """
    subject = "Gained a new follower"
    html_content = render_to_string(
        "email/gained_a_follower_notification.html",
        {"current_user_name": current_user_name, "user_to_follow_name": user_to_follow_name}
    )
    receivers = [user_to_follow_email]

    # Send email to user
    send_email(subject, html_content, receivers)

    return f"Sent notifications to {user_to_follow_name} for being followed by {current_user_name}"
