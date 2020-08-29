import json
import bandit
from bandit.core import test_properties as test

@test.checks('Call')
@test.test_id('B355a')
def key_generation_length_test(context):
    if isinstance(context.call_function_name_qual, str):
        qualname_list = context.call_function_name_qual.split('.')
        func = qualname_list[-1]
        if 'key_generation' in qualname_list and func == 'key_generation_def':

            with open("./policy/policy.json", "r") as policy:
                policy_dict = json.load(policy)
            if policy_dict['policy']['identity_and_access']['identity']['authenticator']['key']:
                key_generation_length = policy_dict['policy']['identity_and_access']['identity']['authenticator']['key']['key_generation_length']

            args = context.call_args
            keywords = context.call_keywords
            #name = args[0] if args else keywords['name']
            
            return bandit.Issue(
                severity = bandit.LOW,
                confidence = bandit.LOW,
                text = 'INFORMATIONAL:  Cryptographic keys must be at least ' + str(key_generation_length) + 
                    ' bytes to be considered secure.  Please review to validate.',
                    lineno=context.node.lineno
            )
