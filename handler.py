from functions.aws_utils import get_prefix_s3
from functions.remove_prefix import get_removal_prefix
from functions.aws_utils import delete_old_data


def delete(event, context):
    result = get_prefix_s3()
    remove_prefixes = get_removal_prefix(result)
    delete_old_data(remove_prefixes)
