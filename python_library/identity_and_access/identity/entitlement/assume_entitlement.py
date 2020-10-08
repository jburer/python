""" Assume Entitlement Module """

import boto3
import boto3.session
from python_library.product_service.operations.event.log import log

my_session=boto3.session.Session(profile_name='User2')

# The calls to AWS STS AssumeRole must be signed with the access key ID
# and secret access key of an existing IAM user or by using existing temporary
# credentials such as those from another role. (You cannot call AssumeRole
# with the access key for the root account.) The credentials can be in
# environment variables or in a configuration file and will be discovered
# automatically by the boto3.client() function. For more information, see the
# Python SDK documentation:
# http://boto3.readthedocs.io/en/latest/reference/services/sts.html#client

def assume_role_def(ra, rsn, sn, tc):
    """ Assume role """
    # create an STS client object that represents a live connection to the
    # STS service
    sts_client = my_session.client('sts')

    print('\n')
    print(sts_client.get_caller_identity())
    print('\n')

    # Call the assume_role method of the STSConnection object and pass the role
    # ARN and a role session name.
    assumed_role_object=sts_client.assume_role(
        #RoleArn="arn:aws:iam::562241862267:role/IAMSystemAdministrationRole",
        #RoleSessionName="AssumeRoleSession1",
        #SerialNumber="arn:aws:iam::562241862267:mfa/User2",
        #TokenCode="338564"
        RoleArn=ra,
        RoleSessionName=rsn,
        SerialNumber=sn,
        TokenCode=tc
    )

    print('\n')
    print(assumed_role_object)
    print('\n')

    # From the response that contains the assumed role, get the temporary
    # credentials that can be used to make subsequent API calls
    credentials=assumed_role_object['Credentials']

    print('\n')
    print(credentials)
    print('\n')

    return credentials

def assume_entitlement_def(role_arn, role_session_name, serial_number, token_code):
    """ Assume Entitlement Function """

    try:
        assume_role_credentials = assume_role_def(role_arn, role_session_name, serial_number, token_code)
        return assume_role_credentials
    except Exception as err:
        log.logger.debug(err, exc_info=True)
