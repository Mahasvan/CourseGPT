import aiohttp


class Internet:
    # This is a singleton class
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Internet, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def get_text(self, url: str, **kwargs):
        async with self.session.get(url, **kwargs) as response:
            response = (await response.content.read()).decode('utf-8')
        return response

    async def get_binary(self, url: str, **kwargs):
        async with self.session.get(url, **kwargs) as response:
            response = (await response.content.read())
        return response

    async def get_json(self, url: str, **kwargs):
        async with self.session.get(url, **kwargs) as response:
            if (await response.text()).lower() == "internal server error":
                return {"response": "Internal Server Error"}
            response = (await response.json())
        return response

    async def post(self, url: str, data: dict = None, params: dict = None):
        async with self.session.post(url, data=data, params=params) as response:
            response = (await response.content.read()).decode('utf-8')
        return response

    async def post_binary(self, url: str, data: dict = None, params: dict = None):
        async with self.session.post(url, data=data, params=params) as response:
            response = (await response.content.read())
        return response

    async def post_json(self, url: str, headers: dict = None, data: dict = None, params: dict = None):
        async with self.session.post(url, headers=headers, data=data, params=params) as response:
            if (await response.text()).lower() == "internal server error":
                return {"response": "Internal Server Error"}
            response = (await response.json())
        return response
