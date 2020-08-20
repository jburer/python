import json
import bandit
from bandit.core import test_properties as test

@test.checks('Call')
@test.test_id('B351a')
def secure_pseudorandom_number_length_test(context):
    if isinstance(context.call_function_name_qual, str):
        qualname_list = context.call_function_name_qual.split('.')
        func = qualname_list[-1]
        if 'secure_pseudorandom_number' in qualname_list and func == 'secure_pseudorandom_number_def':

            with open("./policy/policy.json", "r") as policy:
                policy_dict = json.load(policy)
            if policy_dict['policy']['data']['information']['algorithm']['random_number']['pseudorandom_number']['secure_pseudorandom_number']:
                secure_pseudorandom_number_length = policy_dict['policy']['data']['information']['algorithm']['random_number']['pseudorandom_number']['secure_pseudorandom_number']['secure_pseudorandom_number_length']

            args = context.call_args
            keywords = context.call_keywords
            name = args[0] if args else keywords['name']
            if name <= secure_pseudorandom_number_length:
                return bandit.Issue(
                    severity = bandit.HIGH,
                    confidence = bandit.HIGH,
                    text = 'The pseduorandom number is too small to be used in a security context.' +  
                        'Pseudorandom numbers must be at least ' + str(secure_pseudorandom_number_length) + 
                        ' bytes to be considered secure.',
                        lineno=context.node.lineno
                )
