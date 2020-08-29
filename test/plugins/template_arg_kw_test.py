import bandit
from bandit.core import test_properties as test

@test.checks('Call')
@test.test_id('B352')
def hash_alt_test(context):
    if isinstance(context.call_function_name_qual, str):
        qualname_list = context.call_function_name_qual.split('.')
        func = qualname_list[-1]
        if ('zlib' in qualname_list and func == 'adler32'):
            args = context.call_args
            keywords = context.call_keywords
            name = args[0] if args else keywords['name']
            if name.lower() in ('adler32', 'crc32', 'hash'):
                return bandit.Issue(
                    severity = bandit.LOW,
                    confidence = bandit.LOW,
                    text = 'Hash functions of this type should only be used for checksums. ' +  
                        'This algorithm is not cryptographically strong and should not be used ' +
                        'for authentication or digital signatures. ' + 
                        'Use secure hash functions for anything cryptographic in nature.',
                        lineno=context.node.lineno
                )