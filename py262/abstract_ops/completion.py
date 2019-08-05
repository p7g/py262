from py262.completion import Completion, CompletionType


def update_empty(completion, value):
    assert completion.value is not None if completion.type in [
        CompletionType.RETURN,
        CompletionType.THROW,
    ] else True

    if completion.value is not None:
        return completion
    return Completion(completion.type, value, completion.target)
