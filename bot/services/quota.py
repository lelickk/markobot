"""Placeholder for quota logic."""


def can_request_more(used_minutes: int, used_requests: int) -> bool:
    """Return True when daily limits are not exceeded."""
    return used_minutes < 180 and used_requests < 5
