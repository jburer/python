import json
import bandit
from bandit.core import test_properties as test

@test.checks('Call')
@test.test_id('B353')
def secure_hash_test(context):
    if isinstance(context.call_function_name_qual, str):
        qualname_list = context.call_function_name_qual.split('.')
        func = qualname_list[-1]
        if ('secure_hash' in qualname_list and func == 'secure_hash_def'):
            args = context.call_args
            keywords = context.call_keywords
            name = args[0] if args else keywords['name']

            with open("./policy/policy.json", "r") as policy:
                policy_dict = json.load(policy)

            if policy_dict['policy']['data']['data_transformation']['data_confidentiality']['hash']['secure_hash']:
                secure_hash_algorithm = policy_dict['policy']['data']['data_transformation']['data_confidentiality']['hash']['secure_hash']

            if name.lower() not in secure_hash_algorithm:
                return bandit.Issue(
                    severity = bandit.HIGH,
                    confidence = bandit.HIGH,
                    text = 'Cryptographically weak hash algorithm detected. ' +
                    name + ' is considered weak and should not be used for cryptographic purposes. ' +
                    'Please consult policy for acceptable secure hash algorithms.',
                    lineno=context.node.lineno
                )
