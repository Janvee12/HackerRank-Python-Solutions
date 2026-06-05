# ============================
# PLATFORM:
# HackerRank
# (Python - Validating Email Addresses)
# ============================

# ============================
# PROBLEM:
# ============================
# You are given a list of emails.
#
# A valid email must satisfy:
#
# 1. Format: username@website.extension
#
# 2. username:
#    - only alphanumeric OR
#      contains '_' or '-'
#
# 3. website:
#    - only alphanumeric
#
# 4. extension:
#    - length ≤ 3
#
# Return only valid emails.
# ============================

# ============================
# APPROACH:
# ============================
#
# Step 1:
# Split email into:
#   username and domain
#
# Step 2:
# Split domain into:
#   website and extension
#
# Step 3:
# Validate each part:
#   - username rules
#   - website rules
#   - extension length
#
# Step 4:
# If any rule fails → False
# else → True
# ============================

def fun(s):

    try:
        username, url = s.split('@')
        website, extension = url.split('.')

    except ValueError:
        return False

    # ============================
    # CHECK USERNAME
    # ============================
    if username.replace('-', '').replace('_', '').isalnum() is False:
        return False

    # ============================
    # CHECK WEBSITE
    # ============================
    elif website.isalnum() is False:
        return False

    # ============================
    # CHECK EXTENSION LENGTH
    # ============================
    elif len(extension) > 3:
        return False

    else:
        return True


# ============================
# FILTER FUNCTION
# ============================
def filter_mail(emails):

    return list(filter(fun, emails))