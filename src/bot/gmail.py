from typing import Any


def ensure_label(service: Any, label_name: str) -> str:
    # Placeholder: create/find Gmail label and return id
    _ = (service, label_name)
    return label_name


def insert_inbox_message(
    service: Any,
    from_email: str,
    to_email: str,
    subject: str,
    body: str,
    label_id: str,
) -> None:
    # Placeholder: insert a message into INBOX, mark UNREAD, apply label.
    _ = (service, from_email, to_email, subject, body, label_id)
