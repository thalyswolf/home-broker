
class NotFoundException(Exception):

    """Exception raised for not found errors """

    def __init__(self, message="Not found", http_status=404):
        self.message = message
        self.http_status = http_status
        
        super().__init__(self.message)
