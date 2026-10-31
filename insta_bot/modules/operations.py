"""Bound each explicitly requested social operation to 1 batch."""


def perform_batch(action, count):
    """Return the actual count without retrying partial or empty batches.

    The page action closes its dialog after each batch. Retrying automatically
    can exceed the requested count or loop forever against a closed dialog.
    """
    if not isinstance(count, int) or isinstance(count, bool) or count <= 0:
        raise ValueError("Choose a positive number of accounts")
    completed = action(count=count)
    if not isinstance(completed, int) or isinstance(completed, bool):
        raise RuntimeError("The operation did not return a completed count")
    if not 0 <= completed <= count:
        raise RuntimeError("The reported count is outside the requested limit")
    return completed
