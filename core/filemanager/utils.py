class paramutils:
    @staticmethod
    def validate_params(request: dict, params: list) -> bool:
        """
        Validate if all params exist in the request content
        
        :param request: Request dict
        :param params: Needed params
        :return:
        """
        for param in params:
            temp = request.get(param)
            if not param:
                return False
        return True
