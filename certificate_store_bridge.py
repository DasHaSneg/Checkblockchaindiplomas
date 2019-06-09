def award(certificate_uid):
    from app import cert_store
    import certificate_formatter
    award, verification_info = certificate_formatter.get_formatted_award_and_verification_info(cert_store,
                                                                                               certificate_uid)
    return {'award': award,
            'verification_info': verification_info}



