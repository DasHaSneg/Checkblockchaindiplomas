from cert_core import Chain, UnknownChainError


def get_tx_lookup_chain(chain, txid):
    if chain == Chain.bitcoin_testnet:
        return 'https://live.blockcypher.com/btc-testnet/tx/' + txid
    elif chain == Chain.bitcoin_mainnet:
        return 'https://blockchain.info/tx/' + txid
    elif chain == Chain.bitcoin_regtest or chain == Chain.mockchain:
        return 'This has not been issued on a blockchain and is for testing only'
    else:
        raise UnknownChainError(
            'unsupported chain (%s) requested with blockcypher collector. Currently only testnet and mainnet are supported' % chain)
