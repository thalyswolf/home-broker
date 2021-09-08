class Stocks:
    _id: str
    company_name: str
    ticket: str
    line_of_business: str
    price_sell: str
    price_buy: str

    def __init__(self, company_name: str, ticket:str, line_of_business:str, price_sell: str, price_buy: str) -> None:
        self.company_name = company_name
        self.ticket = ticket
        self.line_of_business = line_of_business
        self.price_sell = price_sell
        self.price_buy = price_buy
