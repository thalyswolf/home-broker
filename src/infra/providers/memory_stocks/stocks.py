from typing import List

from src.contracts.providers import StocksProvidersContract
from src.handlers.not_found_exception import NotFoundException
from src.infra.providers.memory_stocks.helpers import generate_random_float_value
from src.adapter.providers.memory_stocks_adapter import MemoryStocksAdapter
from src.core.entity import Stocks


class MemoryStocksProvider(StocksProvidersContract):


    stocks = [
        {
            "ticket": "ABEV3",
            "name": "AMBEV S/A",
            "lineOfBusiness": "Consumo não Cíclico / Bebidas / Cervejas e Refrigerantes",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "AZUL4",
            "name": "AZUL",
            "lineOfBusiness": "Bens Industriais / Transporte / Transporte Aéreo",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "B3SA3",
            "name": "B3",
            "lineOfBusiness": "Financeiro e Outros / Serviços Financeiros Diversos / Serviços Financeiros Diversos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "BBAS3",
            "name": "BANCO DO BRASIL",
            "lineOfBusiness": "Financeiro e Outros / Intermediários Financeiros / Bancos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "BBDC3",
            "name": "BRADESCO",
            "lineOfBusiness": "Financeiro e Outros / Intermediários Financeiros / Bancos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "BBSE3",
            "name": "BBSEGURIDADE",
            "lineOfBusiness": "Financeiro e Outros / Previdência e Seguros / Seguradoras",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "BEEF3",
            "name": "MINERVA",
            "lineOfBusiness": "Consumo não Cíclico / Alimentos Processados / Carnes e Derivados",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "BPAC11",
            "name": "BTGP BANCO",
            "lineOfBusiness": "Financeiro e Outros / Intermediários Financeiros / Bancos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "BRAP4",
            "name": "BRADESPAR",
            "lineOfBusiness": "Materiais Básicos / Mineração / Minerais Metálicos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "BRDT3",
            "name": "PETROBRAS BR",
            "lineOfBusiness": "Petróleo. Gás e Biocombustíveis",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "BRFS3",
            "name": "BRF SA",
            "lineOfBusiness": "Consumo não Cíclico / Alimentos Processados / Carnes e Derivados",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "BRKM5",
            "name": "BRASKEM",
            "lineOfBusiness": "Materiais Básicos / Químicos / Petroquímicos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "BRML3",
            "name": "BR MALLS PAR",
            "lineOfBusiness": "Financeiro e Outros / Exploração de Imóveis",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "BTOW3",
            "name": "B2W DIGITAL",
            "lineOfBusiness": "Consumo Cíclico / Comércio",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "CCRO3",
            "name": "CCR SA",
            "lineOfBusiness": "Bens Industriais / Transporte / Exploração de Rodovias",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "CIEL3",
            "name": "CIELO",
            "lineOfBusiness": "Financeiro e Outros / Serviços Financeiros Diversos / Serviços Financeiros Diversos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "CMIG4",
            "name": "CEMIG",
            "lineOfBusiness": "Utilidade Pública / Energia Elétrica",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "COGN3",
            "name": "COGNA ON",
            "lineOfBusiness": "Consumo Cíclico / Diversos / Serviços Educacionais",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "CPFE3",
            "name": "CPFL ENERGIA",
            "lineOfBusiness": "Utilidade Pública / Energia Elétrica / Energia Elétrica",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "CRFB3",
            "name": "CARREFOUR BR",
            "lineOfBusiness": "Consumo não Cíclico / Comércio e Distribuição / Alimentos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "CSAN3",
            "name": "COSAN",
            "lineOfBusiness": "Petróleo. Gás e Biocombustíveis",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "CSNA3",
            "name": "SID NACIONAL",
            "lineOfBusiness": "Materiais Básicos / Siderurgia e Metalurgia / Siderurgia",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "CVCB3",
            "name": "CVC BRASIL",
            "lineOfBusiness": "Consumo Cíclico / Viagens e Lazer / Viagens e Turismo",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "CYRE3",
            "name": "CYRELA REALT",
            "lineOfBusiness": "Consumo Cíclico / Construção Civil / Edificações",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "ECOR3",
            "name": "ECORODOVIAS",
            "lineOfBusiness": "Bens Industriais / Transporte / Exploração de Rodovias",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "EGIE3",
            "name": "ENGIE BRASIL",
            "lineOfBusiness": "Utilidade Pública / Energia Elétrica",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "ELET3",
            "name": "ELETROBRAS",
            "lineOfBusiness": "Utilidade Pública / Energia Elétrica",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "EMBR3",
            "name": "EMBRAER",
            "lineOfBusiness": "Bens Industriais / Material de Transporte",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "ENBR3",
            "name": "ENERGIAS BR",
            "lineOfBusiness": "Utilidade Pública / Energia Elétrica",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "ENGI11",
            "name": "ENERGISA",
            "lineOfBusiness": "Utilidade Pública / Energia Elétrica",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "EQTL3",
            "name": "EQUATORIAL",
            "lineOfBusiness": "Utilidade Pública / Energia Elétrica",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "FLRY3",
            "name": "FLEURY",
            "lineOfBusiness": "Saúde / Serv.Méd.Hospit..Análises e Diagnósticos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "GGBR4",
            "name": "GERDAU",
            "lineOfBusiness": "Materiais Básicos / Siderurgia e Metalurgia / Siderurgia",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "GNDI3",
            "name": "INTERMEDICA",
            "lineOfBusiness": "Saúde / Serv.Méd.Hospit..Análises e Diagnósticos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "GOAU4",
            "name": "GERDAU MET",
            "lineOfBusiness": "Materiais Básicos / Siderurgia e Metalurgia / Siderurgia",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "GOLL4",
            "name": "GOL",
            "lineOfBusiness": "Bens Industriais / Transporte / Transporte Aéreo",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "HAPV3",
            "name": "HAPVIDA",
            "lineOfBusiness": "Saúde / Serv.Méd.Hospit..Análises e Diagnósticos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "HGTX3",
            "name": "CIA HERING",
            "lineOfBusiness": "Consumo Cíclico / Tecidos. Vestuário e Calçados / Vestuário",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "HYPE3",
            "name": "HYPERA",
            "lineOfBusiness": "Saúde / Comércio e Distribuição",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "IGTA3",
            "name": "IGUATEMI",
            "lineOfBusiness": "Financeiro e Outros / Exploração de Imóveis",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "IRBR3",
            "name": "IRBBRASIL RE",
            "lineOfBusiness": "Financeiro / Previdência e Seguros / Seguradoras",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "ITSA4",
            "name": "ITAUSA",
            "lineOfBusiness": "Financeiro e Outros / Intermediários Financeiros / Bancos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "ITUB4",
            "name": "ITAUUNIBANCO",
            "lineOfBusiness": "Financeiro e Outros / Intermediários Financeiros / Bancos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "JBSS3",
            "name": "JBS",
            "lineOfBusiness": "Consumo não Cíclico / Alimentos Processados / Carnes e Derivados",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "KLBN11",
            "name": "KLABIN S/A",
            "lineOfBusiness": "Materiais Básicos / Papel e Celulose",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "LAME4",
            "name": "LOJAS AMERIC",
            "lineOfBusiness": "Consumo Cíclico / Comércio",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "LREN3",
            "name": "LOJAS RENNER",
            "lineOfBusiness": "Consumo Cíclico / Comércio",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "MGLU3",
            "name": "MAGAZ LUIZA",
            "lineOfBusiness": "Consumo Cíclico / Comércio",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "MRFG3",
            "name": "MARFRIG",
            "lineOfBusiness": "Consumo não Cíclico / Alimentos Processados / Carnes e Derivados",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "MRVE3",
            "name": "MRV",
            "lineOfBusiness": "Consumo Cíclico / Construção Civil / Edificações",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "MULT3",
            "name": "MULTIPLAN",
            "lineOfBusiness": "Financeiro e Outros / Exploração de Imóveis",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "NTCO3",
            "name": "NATURA",
            "lineOfBusiness": "Consumo não Cíclico / Produtos de Uso Pessoal e de Limpeza",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "PCAR3",
            "name": "P.ACUCAR-CBD",
            "lineOfBusiness": "Consumo não Cíclico / Comércio e Distribuição / Alimentos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "PETR3",
            "name": "PETROBRAS",
            "lineOfBusiness": "Petróleo. Gás e Biocombustíveis",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "QUAL3",
            "name": "QUALICORP",
            "lineOfBusiness": "Saúde / Serv.Méd.Hospit..Análises e Diagnósticos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "RADL3",
            "name": "RAIADROGASIL",
            "lineOfBusiness": "Saúde / Comércio e Distribuição",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "RAIL3",
            "name": "RUMO S.A.",
            "lineOfBusiness": "Bens Industriais / Transporte / Transporte Ferroviário",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "RENT3",
            "name": "LOCALIZA",
            "lineOfBusiness": "Consumo Cíclico / Aluguel de carros",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "SANB11",
            "name": "SANTANDER BR",
            "lineOfBusiness": "Financeiro e Outros / Intermediários Financeiros / Bancos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "SBSP3",
            "name": "SABESP",
            "lineOfBusiness": "Utilidade Pública / Água e Saneamento",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "SULA11",
            "name": "SUL AMERICA",
            "lineOfBusiness": "Financeiro / Previdência e Seguros / Seguradoras",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "SUZB3",
            "name": "SUZANO S.A.",
            "lineOfBusiness": "Materiais Básicos / Papel e Celulose",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "TAEE11",
            "name": "TAESA",
            "lineOfBusiness": "Utilidade Pública / Energia Elétrica",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "TIMP3",
            "name": "TIM PART S/A",
            "lineOfBusiness": "Telecomunicações",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "TOTS3",
            "name": "TOTVS",
            "lineOfBusiness": "Tecnologia da Informação / Programas e Serviços",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "UGPA3",
            "name": "ULTRAPAR",
            "lineOfBusiness": "Petróleo. Gás e Biocombustíveis",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "USIM5",
            "name": "USIMINAS",
            "lineOfBusiness": "Materiais Básicos / Siderurgia e Metalurgia / Siderurgia",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "VALE3",
            "name": "VALE",
            "lineOfBusiness": "Materiais Básicos / Mineração / Minerais Metálicos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "VIVT4",
            "name": "TELEF BRASIL",
            "lineOfBusiness": "Telecomunicações",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "VVAR3",
            "name": "VIAVAREJO",
            "lineOfBusiness": "Consumo Cíclico / Comércio",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "WEGE3",
            "name": "WEG",
            "lineOfBusiness": "Bens Industriais / Máquinas e Equipamentos",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        },
        {
            "ticket": "YDUQ3",
            "name": "YDUQS PART",
            "lineOfBusiness": "Consumo Cíclico / Serviços Educacionais",
            "priceBuy": generate_random_float_value(),
            "priceSell": generate_random_float_value()
        }
    ]


    def list_all_stocks(self) -> List[Stocks]:
        return map(lambda x: MemoryStocksAdapter.create(x), self.stocks)


    def get_stock_by_ticket(self, ticket: str) -> Stocks:
        stock = list(filter(lambda x: x['ticket'] == ticket, self.stocks))

        if len(stock) > 0:
            return MemoryStocksAdapter.create(stock[0])
        else:
            raise NotFoundException('The ticket not founded in stocks list')

