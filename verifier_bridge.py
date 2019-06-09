from cert_verifier import verifier


def verify(certificate_uid):
    from app import cert_store
    certificate = cert_store.get_certificate(certificate_uid)
    if certificate:
        options={'etherscan_api_token':''}
        verify_response = verifier.verify_certificate(certificate, options=options)
        return verify_response
    else:
        raise Exception('Cannot find certificate with uid=%s', certificate_uid)
