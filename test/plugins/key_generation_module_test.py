import json
import bandit
from bandit.core import test_properties as test

@test.checks('Call')
@test.test_id('B355b')
def key_generation_module_test(context):
    if isinstance(context.call_function_name_qual, str):
        qualname_list = context.call_function_name_qual.split('.')
        func = qualname_list[-1]
        if 'key_generation' in qualname_list and func == 'key_generation_def':

            with open("./policy/policy.json", "r") as policy:
                    policy_dict = json.load(policy)
            if policy_dict['policy']['identity_and_access']['identity']['authenticator']['key']:
                key_generation_module = policy_dict['policy']['identity_and_access']['identity']['authenticator']['key']['key_generation_module']

            args = context.call_args
            keywords = context.call_keywords
            #name = args[0] if args else keywords['name']

            return bandit.Issue(
                severity = bandit.LOW,
                confidence = bandit.LOW,
                text = 'INFORMATIONAL:  The approved modules for secure pseudorandom number generation are: ' + 
                    str(key_generation_module) + 
                    ' Please review to validate you are using one.  If so, please consider this informational.',
                    lineno=context.node.lineno
            )
        