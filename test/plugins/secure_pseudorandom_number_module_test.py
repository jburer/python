import json
import bandit
from bandit.core import test_properties as test

@test.checks('Call')
@test.test_id('B351b')
def secure_pseudorandom_number_module_test(context):
    if isinstance(context.call_function_name_qual, str):
        qualname_list = context.call_function_name_qual.split('.')
        func = qualname_list[-1]
        if 'secure_pseudorandom_number' in qualname_list and func == 'secure_pseudorandom_number_def':

            with open("./policy/policy.json", "r") as policy:
                    policy_dict = json.load(policy)
            if policy_dict['policy']['data']['information']['algorithm']['random_number']['pseudorandom_number']['secure_pseudorandom_number']:
                secure_pseudorandom_number_module = policy_dict['policy']['data']['information']['algorithm']['random_number']['pseudorandom_number']['secure_pseudorandom_number']['secure_pseudorandom_number_module']
            
            args = context.call_args
            keywords = context.call_keywords
            name = args[0] if args else keywords['name']

            return bandit.Issue(
                severity = bandit.LOW,
                confidence = bandit.LOW,
                text = 'The approved modules for secure pseudorandom number generation are: ' + 
                    str(secure_pseudorandom_number_module) + 
                    ' Please review to validate you are using one.',
                    lineno=context.node.lineno
            )
        