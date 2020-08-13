import json
import bandit
from bandit.core import test_properties as test

@test.checks('Call')
@test.test_id('B351')
def secure_pseudorandom_number_test(context):
    if context.call_function_name == 'secure_pseudorandom_number_def':

        with open("./policy/policy.json", "r") as policy:
            policy_dict = json.load(policy)

        if policy_dict['policy']['secure_pseudorandom_number_byte_size']:
            secure_pseudorandom_number_byte_size = policy_dict['policy']['secure_pseudorandom_number_byte_size']

        if context.get_call_arg_value('byte_size') <= secure_pseudorandom_number_byte_size:
            return bandit.Issue(
                severity = bandit.HIGH,
                confidence = bandit.HIGH,
                text = 'The pseduorandom number is too small to be used in a security context.' +  
                    'Pseudorandom numbers must be at least ' + str(secure_pseudorandom_number_byte_size) + 
                    ' bytes to be considered secure.'
            )