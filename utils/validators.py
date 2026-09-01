"""Input Validation Utilities"""
import re
from typing import List, Optional


def validate_email(email: str) -> bool:
    """Validate email address.

    Args:
        email: Email to validate

    Returns:
        True if valid
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def validate_url(url: str) -> bool:
    """Validate URL.

    Args:
        url: URL to validate

    Returns:
        True if valid
    """
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}.*$"
    return re.match(pattern, url) is not None


def validate_not_empty(value: str, field_name: str = "Field") -> bool:
    """Validate not empty.

    Args:
        value: Value to validate
        field_name: Field name for error message

    Returns:
        True if not empty

    Raises:
        ValueError: If empty
    """
    if not value or not value.strip():
        raise ValueError(f"{field_name} cannot be empty")
    return True


def validate_platform(platform: str, valid_platforms: Optional[List[str]] = None) -> bool:
    """Validate platform name.

    Args:
        platform: Platform to validate
        valid_platforms: List of valid platforms

    Returns:
        True if valid
    """
    default_platforms = ["twitter", "linkedin", "instagram", "facebook", "tiktok"]
    valid = valid_platforms or default_platforms
    return platform.lower() in valid
