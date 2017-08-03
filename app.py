from sanic import Sanic
from sanic import response

import aiohttp


app = Sanic()


async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.json()


@app.route("/")
async def handle_request(request):
    url = 'https://api.github.com/users/mpicard'

    async with aiohttp.ClientSession() as session:
        resp = await fetch(session, url)
        return response.json(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=2)
