#coding=utf-8

import bairros_barreiro
import bairros_centrosul
import bairros_leste
import bairros_nordeste
import bairros_noroeste
import bairros_norte
import bairros_oeste
import bairros_pampulha
import bairros_vendanova
import bairros_unknown

def get_map_bairro_regional(module, nome_regional):
    return map (
        lambda x: (getattr(module, x), nome_regional),
        filter (
            lambda x: type(getattr(module, x)) == str and x not in ('__file__', '__name__'),
            dir(module)
        )
    )

DICT_BAIRRO_REGIONAL = dict(
    get_map_bairro_regional(bairros_barreiro, 'Barreiro') +
    get_map_bairro_regional(bairros_centrosul, 'Centro-Sul') +
    get_map_bairro_regional(bairros_leste, 'Leste') +
    get_map_bairro_regional(bairros_nordeste, 'Nordeste') +
    get_map_bairro_regional(bairros_noroeste, 'Noroeste') +
    get_map_bairro_regional(bairros_norte, 'Norte') +
    get_map_bairro_regional(bairros_oeste, 'Oeste') +
    get_map_bairro_regional(bairros_pampulha, 'Pampulha') +
    get_map_bairro_regional(bairros_vendanova, 'Venda Nova')
)

def get_regional(bairro):
    return DICT_BAIRRO_REGIONAL.get(bairro)
